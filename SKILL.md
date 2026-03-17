---
name: prtg
description: Use when working with PRTG Network Monitor via API v2 — querying devices/sensors, creating and editing monitoring objects, building Spectrum-themed dashboards, or exploring network data.
argument-hint: <task description>
allowed-tools: Read, Bash, Write, Edit, Glob, Grep
disable-model-invocation: true
---

# PRTG Network Monitor — API v2 Skill

## Setup

Credentials are stored in a `*.env` file in the working directory. Format:

```
PRTG_HOST=https://your-prtg-server
PRTG_API_KEY=your-api-token
```

**CRITICAL — Windows/Git Bash:** `source file.env` silently fails when the path contains spaces. **Never use bash `source` or `$VAR` substitution for credentials.** Always use Python to load credentials and call APIs:

```python
import subprocess, json, glob

# Load credentials — works regardless of spaces in path
# Sorted + .env.example excluded so selection is deterministic
env_files = sorted(p for p in glob.glob('*.env') if p != '.env.example')
if not env_files:
    raise FileNotFoundError("No *.env file found. Create one with PRTG_HOST and PRTG_API_KEY.")
env = dict(line.strip().split('=', 1) for line in open(env_files[0]) if '=' in line and not line.startswith('#'))
HOST, KEY = env['PRTG_HOST'].rstrip('/'), env['PRTG_API_KEY']

def prtg_get(path):
    r = subprocess.run(
        ['curl', '-s', '-k', f'{HOST}/api/v2/{path}', '-H', f'Authorization: Bearer {KEY}'],
        capture_output=True, text=True, timeout=30)
    if not r.stdout.strip():
        raise RuntimeError(f"Empty response from PRTG (path={path}). stderr: {r.stderr[:200]}")
    return json.loads(r.stdout)

def prtg_request(method, path, body=None):
    """For POST/PATCH/DELETE. Returns parsed JSON, or None for 204 No Content."""
    cmd = ['curl', '-s', '-k', '-X', method.upper(),
           f'{HOST}/api/v2/{path}', '-H', f'Authorization: Bearer {KEY}']
    if body is not None:
        cmd += ['-H', 'Content-Type: application/json', '-d', json.dumps(body)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if not r.stdout.strip():
        return None  # 204 No Content
    return json.loads(r.stdout)

# Example
devices = prtg_get('experimental/devices?limit=3000')
```

Authenticate with: `Authorization: Bearer <api_key>` header. Use `curl -s -k` (allow insecure for internal servers). Base URL: `{host}/api/v2`

## Key References

Read these files on-demand (they are large — only read what you need):

- **`${CLAUDE_SKILL_DIR}/references/api-endpoints.md`** — All endpoint paths, HTTP methods, parameters, and response codes. Read this when you need to know what endpoints exist or their parameters.
- **`${CLAUDE_SKILL_DIR}/references/api-filtering.md`** — Filter syntax, operators, filterable properties, enum values, and common pitfalls. Read this before constructing any `filter=` query.
- **`${CLAUDE_SKILL_DIR}/references/api-schemas.md`** — Request/response body schemas with field names, types, and descriptions. Read this when you need to construct a request body or understand a response.
- **`${CLAUDE_SKILL_DIR}/references/spectrum-design-system.md`** — Spectrum design token reference (colors, typography, spacing, status mappings). **Read this before generating any frontend/dashboard code.**
- **`${CLAUDE_SKILL_DIR}/references/visualization-patterns.md`** — Visualization module catalog with v2-first query plans and v1 fallback triggers. Read this for richer dashboards (heatmaps, timeline stacks, SLA bars, flap ranking, dependency views).

## Critical Gotchas & Lessons Learned

1. **Filter syntax is NOT OData.** Use `=`, `!=`, `contains`, `matches` — not `eq`, `ne`. See `references/api-filtering.md` for full reference.
2. **Text values must be double-quoted** in filter expressions: `name = "Ping v2"`, not `name = Ping v2`.
3. **Enum values are bare identifiers:** `status = up`, not `status = "up"`.
4. **`sensor_kind` is not filterable.** You must filter client-side or use `basic.tags contains` as an approximation.
5. **`matches` operator is unreliable** — may return incomplete results. Prefer exact match or `contains`.
6. **Default limit is 100.** Always set `limit=3000` (or appropriate value) to avoid truncated results.
7. **Device status values in responses are prefixed with `SUMMED_INFO_`** (e.g. `SUMMED_INFO_UP`), while sensor statuses are plain (e.g. `UP`). **However, filter expressions always use lowercase without prefix** — `filter=status = down`, NOT `filter=status = SUMMED_INFO_DOWN`.
8. **Path array** on sensors/devices gives the full tree path from root. Extract the parent device with `type == "REFERENCED_DEVICE"`.
9. **The `type` field doesn't exist on individual endpoint responses** (e.g. `/sensors`). It's only available on `/objects`. Sensors have `sensor_kind` instead.
10. **Settings are dynamic and sectioned** — schemas must be fetched from schema endpoints, as they vary by object type. By default, schema and GET endpoints only return the `basic` section. Use `?include=all_sections` to get all available setting sections (e.g. `discoverytypegroup`, `intervalgroup`, `snmpversiongroup`, etc.). You can also include specific sections: `?include=discoverytypegroup,intervalgroup`.
11. **Sensor PATCH uses singular path (bug)** — `PATCH /experimental/sensor/{id}` works, but `PATCH /experimental/sensors/{id}` does not. All other resources use plural consistently. This is a known inconsistency.
12. **Schema endpoint requires a real object ID** — `/experimental/schemas/{id}/patch` needs an actual ID (e.g. `2490`), not a type name.
13. **`parentid` is direct-parent only** — Sensors are children of devices, not groups. To find sensors in a group, first get devices, then query sensors by device IDs.
14. **Experimental sensors have extra fields** — `kind`, `kind_name`, `parent`, `status_since`. Prefer experimental endpoints.
15. **Sensor creation uses `kindid` query param** — `POST /experimental/devices/{id}/sensor?kindid=ping`. The kind goes in the URL, not the body.
16. **POST schema endpoint differs from PATCH schema** — POST uses `GET /experimental/schemas/{parent_id}/post?kind=ping`. PATCH uses `GET /experimental/schemas/{object_id}/patch`.
17. **List endpoints return plain JSON arrays** — `[{...}, {...}]`, NOT `{"items": [...]}`.
18. **IDs are always strings** — `parentid in ["2490","2491"]`, not `parentid in [2490]`.
19. **`parent.id` is NOT filterable** on channels — use `parentid` (flat field).
20. **`parentid = value` requires text** — `parentid = "2490"`, not `parentid = 2490`.
21. **`status_since`** (experimental only) — ISO 8601 timestamp for when current status began.
22. **`last_measurement.display_value`** is numeric — combine with `basic.displayunit` for display.
23. **Timeseries headers are channel IDs, not names** — map via `/experimental/channels?filter=parentid in ["{sensorId}"]`.
24. **`include=all_sections` is needed for full settings** — Schema endpoints (`/experimental/schemas/{id}/patch`) and GET endpoints only return `basic` by default. Add `?include=all_sections` to see all configurable sections. Use `?include=section1,section2` for specific ones.
25. **`discoverytypegroup` = Auto-Discovery settings** — The section name is not intuitive. Key fields: `discoverytype` (`"0"`=off, `"1"`=default, `"2"`=with templates, `"3"`=detailed) and `discoveryschedule` (`"0"`=once, `"1"`=hourly, `"2"`=daily, `"3"`=weekly).
26. **Non-experimental PATCH supports more sections** — `PATCH /devices/{id}` accepts sections like `discoverytypegroup` that may return 501 on the experimental singular endpoint (`/experimental/sensor/{id}`).
27. **`include=sensor_status_summary` for device sensor counts** — By default, device list/read endpoints do NOT return sensor status breakdowns. Add `?include=sensor_status_summary` to get a `sensor_status_summary` object on each device with fields: `calculated_status`, `total`, `down`, `down_acknowledged`, `down_partial`, `warning`, `up`, `paused_by_user`, `paused_by_dependency`, `paused_by_schedule`, `unusual`, `unknown`, `collecting`, etc. Use this to find devices with down sensors without querying sensors separately. You can also use `include=*` as a wildcard for all extra data.
28. **Four distinct schema endpoints** — `GET /experimental/schemas/{parentId}` (list creatable kinds), `GET /experimental/schemas/{parentId}/post?kind={kind}` (POST body schema), `GET /experimental/schemas/{objectId}/patch?include=all_sections` (PATCH schema), `GET /experimental/schemas/{objectId}/get?include=all_sections` (GET schema). All responses are OAS 3.0.3 docs; the actual schema is always at `components.schemas.modifyItemSchema`.
29. **`x-prtg-meta` drives field rendering** — Every schema field carries an `x-prtg-meta` object. `class` determines input type (`edit`, `integer`, `combo`, `radio`, `tags`, `lookuplist`, `lookupchecklistbox`, `lookupfilelist`, `password`, `information`, `section`). `required: true` means provide the field even if a default exists. **`information` class fields are read-only display text — never prompt for them.**
30. **POST schema only shows `basic` + optional metascan picker** — Sensor-specific settings use server defaults at creation time. Configure them afterwards via PATCH. Only `name` (required), `priority`, and `tags` need to be provided on creation.
31. **Sensor PATCH 501 for non-basic sections** — `PATCH /experimental/sensor/{id}` currently only implements the `basic` section. All other sections return `501 METHOD_NOT_IMPLEMENTED: "section X is not yet supported"`. Handle this gracefully — report it to the user rather than failing hard.
32. **Inheritance requires `include=inheritance`** — Without this flag, `_inherited`, `_inheritancesource`, and `_shadowed` are absent from the response. It is impossible to tell whether a value is inherited or locally set without it. Always use `?include=all_sections,inheritance` for a full settings view.
33. **Metascan requires POST with a JSON body** — `GET /experimental/devices/{id}/metascan` returns `404`. `POST` with no body returns `400 EOF`. Always send at minimum `{}`. Only applicable to kinds with `HasMetaScan` in their `flags`.
34. **`metascan_href` values in schema responses are wrong (bug)** — The kind listing omits the `/api/v2` prefix; the POST schema's `x-prtg-meta.href` uses the wrong path (`/device/` instead of `/experimental/devices/`). **Never use these hrefs.** Always construct the metascan URL yourself: `POST /api/v2/experimental/devices/{deviceId}/metascan?kind={kind}`.
35. **Setting lookups: send `info.C0`, not the full key** — For `lookuplist` fields, resolve options via `GET /setting-lookups/{lookupkey}?id={objectId}`. The value to send in PATCH is `info.C0` (e.g. `"60"`), not the full key string (e.g. `"60;60 seconds;"`). The display label is `info.C1`.

## Endpoint Naming: Plural vs Singular

**Critical:** Endpoint paths vary by resource type — do NOT assume a uniform singular/plural pattern. Check `references/api-endpoints.md` when unsure.

All resource types use **plural** paths for all operations:

| Operation  | Sensors                                          | Devices                              | Groups                               | Probes                               |
|------------|--------------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| **List**   | `GET /experimental/sensors`                      | `GET /experimental/devices`          | `GET /experimental/groups`           | `GET /experimental/probes`           |
| **Read**   | `GET /experimental/sensors/{id}`                 | `GET /experimental/devices/{id}`     | `GET /experimental/groups/{id}`      | `GET /experimental/probes/{id}`      |
| **Create** | `POST /experimental/devices/{id}/sensor?kindid=` | —                                    | —                                    | —                                    |
| **Edit**   | `PATCH /experimental/sensor/{id}` *(singular!)*  | `PATCH /devices/{id}`                | `PATCH /experimental/groups/{id}`    | —                                    |
| **Delete** | `DELETE /experimental/sensors/{id}`              | `DELETE /experimental/devices/{id}`  | `DELETE /experimental/groups/{id}`   | `DELETE /experimental/probes/{id}`   |

> **Known bug:** Sensor PATCH requires the **singular** path (`/experimental/sensor/{id}`). See gotcha #11.

## Response Format

**List endpoints return plain JSON arrays**, not wrapped objects:

```python
# CORRECT:
data = prtg_get('experimental/sensors?limit=3000')
# data is a list: [{"id": "1002", "name": "Core Health", ...}, ...]

# WRONG — there is no "items" wrapper:
# data.get("items", [])  # This won't work!
```

## Practical API Patterns

### List all devices
```python
devices = prtg_get('experimental/devices?limit=3000')
```

### List sensors filtered by status
```python
import urllib.parse
params = urllib.parse.urlencode({'filter': 'status = down', 'limit': '3000'})
sensors = prtg_get(f'experimental/sensors?{params}')
```

### Find sensors on a specific device
```python
import urllib.parse
params = urllib.parse.urlencode({'filter': 'parentid = "40"', 'limit': '3000'})
sensors = prtg_get(f'experimental/sensors?{params}')
```

### Create a ping sensor on a device
```python
result = prtg_request('POST', f'experimental/devices/{device_id}/sensor?kindid=ping',
                      {"basic": {"name": "My Ping Sensor"}})
```

### Rename a sensor (use singular path — see gotcha #11)
```python
prtg_request('PATCH', f'experimental/sensor/{sensor_id}', {"basic": {"name": "New Name Here"}})
```

### Find sensors in a group (two-step)
```python
import urllib.parse

# Step 1: Get device IDs in the group
params = urllib.parse.urlencode({'filter': 'parentid = "53"', 'limit': '3000'})
devices = prtg_get(f'experimental/devices?{params}')
device_ids = [f'"{d["id"]}"' for d in devices]

# Step 2: Get sensors on those devices
params2 = urllib.parse.urlencode({'filter': f'parentid in [{",".join(device_ids)}]', 'limit': '3000'})
sensors = prtg_get(f'experimental/sensors?{params2}')
```

### Find devices with down sensors
```python
devices = prtg_get('experimental/devices?limit=3000&include=sensor_status_summary')
down_devices = [d for d in devices if d.get('sensor_status_summary', {}).get('down', 0) > 0]
```

### Fetch channel names for timeseries
```python
import urllib.parse
sensor_ids = ["2490", "2491", "2492"]
ids_str = ",".join(f'"{sid}"' for sid in sensor_ids)
params = urllib.parse.urlencode({'filter': f'primary = true and parentid in [{ids_str}]', 'limit': '3000'})
channels = prtg_get(f'experimental/channels?{params}')
channel_map = {str(ch['id']): ch['name'] for ch in channels}
```

### Fetch timeseries data for a sensor
```python
import urllib.parse

sensor_id = "2490"

# Step 1: Get channel IDs for this sensor
params = urllib.parse.urlencode({'filter': f'parentid = "{sensor_id}"', 'limit': '3000'})
channels = prtg_get(f'experimental/channels?{params}')
channel_map = {str(ch['id']): ch['name'] for ch in channels}  # e.g. {"2490.1": "Response Time"}

# Step 2: Fetch timeseries — use type= for predefined windows:
#   live (last 4h), short (last 2d), medium (last 30d), long (last 365d)
# Optionally restrict to specific channels with ?channels=2490.1,2490.2
channel_ids = ",".join(channel_map.keys())
params2 = urllib.parse.urlencode({'channels': channel_ids})
rows = prtg_get(f'experimental/timeseries/{sensor_id}/short?{params2}')

# rows is a list of dicts; each row has a 'datetime' key and channel-ID keys for values:
# [{"datetime": "2024-01-01T00:00:00Z", "2490.1": 12.3, "2490.2": 0.0}, ...]

# Step 3: Remap channel IDs to names for display
named_rows = []
for row in rows:
    named = {"datetime": row["datetime"]}
    for cid, name in channel_map.items():
        if cid in row:
            named[name] = row[cid]
    named_rows.append(named)
```

### Complete settings wizard flow

```python
# 1. What can be created under this parent?
kinds = prtg_get(f'experimental/schemas/{parent_id}')
# kinds is a list; filter to creatable=True and check flags

# 2. Get the POST schema for the chosen kind
schema_doc = prtg_get(f'experimental/schemas/{parent_id}/post?kind={kind}')
# schema is at schema_doc['components']['schemas']['modifyItemSchema']

# 3. Trigger metascan if needed (HasMetaScan in flags)
if 'HasMetaScan' in selected_kind['flags']:
    items = prtg_request('POST', f'experimental/devices/{device_id}/metascan?kind={kind}', {})

# 4. Create the sensor
body = {"basic": {"name": "My Sensor"}}
# For metascan sensors, add the selection using metascan_field path:
# e.g. metascan_field="diskfree.disk" → body["diskfree"] = {"disk": "C:"}
new_sensor = prtg_request('POST', f'experimental/devices/{device_id}/sensor?kindid={kind}', body)

# 5. Read current settings for editing (with full sections + inheritance)
settings = prtg_get(f'sensors/{sensor_id}?include=all_sections,inheritance')
patch_schema = prtg_get(f'experimental/schemas/{sensor_id}/patch?include=all_sections')

# 6. Resolve lookup options for lookuplist fields
lookups = prtg_get(f'setting-lookups/{lookupkey}?id={sensor_id}')
options = {item['info']['C0']: item['info']['C1'] for item in lookups}

# 7. Apply settings edit (handle 501 gracefully — not all sections implemented yet)
result = prtg_request('PATCH', f'experimental/sensor/{sensor_id}',
    {"intervalgroup": {"_inherited": False, "interval": "300"}})
```

### Paginate large result sets
```python
import urllib.parse

# Use offset + limit to page through results exceeding 3000
all_devices = []
offset = 0
page_size = 3000
while True:
    params = urllib.parse.urlencode({'limit': page_size, 'offset': offset})
    page = prtg_get(f'experimental/devices?{params}')
    all_devices.extend(page)
    if len(page) < page_size:
        break  # Last page
    offset += page_size
```

## Dashboard / Frontend Guidelines

**Always read `${CLAUDE_SKILL_DIR}/references/spectrum-design-system.md` before generating any HTML/CSS.**

- Link `spectrum.css` (must be in the same directory as generated HTML):
  ```html
  <link rel="stylesheet" href="spectrum.css">
  ```
  Download with: `python3 ${CLAUDE_SKILL_DIR}/scripts/fetch_spectrum.py`
- Use Spectrum design tokens via CSS custom properties (`var(--token-name)`)
- Use semantic color tokens, not hardcoded hex values
- PRTG status → Spectrum color mapping:
  - UP → `fill-color-success` / `background-color-success-soft` (green)
  - DOWN → `fill-color-danger` / `background-color-danger-soft` (red)
  - WARNING → `fill-color-warning` / `background-color-warning-soft` (orange)
  - PAUSED/UNKNOWN → `text-color-disabled` / `background-color-disabled` (grey)
- Font stack: Roboto, "Segoe UI", Tahoma, Arial, Helvetica, Verdana, sans-serif
- Base font size: 14px. Spacing unit: 4px multiples.

### Charts & Timeseries
- Use **Chart.js via CDN** (`chart.js` + `chartjs-adapter-date-fns`). No build step required.
- Chart line colors (Spectrum 60-level palette): blue-60 `#0F67FF`, green-60 `#A4AD19`, dark-orange-60 `#DE6800`, cyan-60 `#0097B2`, purple-60 `#8A3FFC`, magenta-60 `#D12771`
- Grid lines: `#F1F1F3`. Font: Roboto.
- **Always label channels by name** (e.g. "Response Time"), not by channel ID (e.g. "2490.0"). Map `channel_id → name` via the channels endpoint before rendering.
- When rendering charts in expandable/hidden containers: wrap each `<canvas>` in a fixed-height `<div>` with `overflow: hidden; position: relative`. Create charts with `requestAnimationFrame` after the container becomes visible.

### Visualization Presets (v2 First)

When a user asks for "more visuals", pick one preset and compose modules from `references/visualization-patterns.md`:

- `exec-view`: status heatmap + blast radius + top incident list
- `ops-view`: 24h status timeline + flapping leaderboard + capacity forecast
- `security-view`: SSL expiry tiers + vulnerable endpoints + cert trend

For each module:

1. List the exact endpoints used.
2. State data source as `v2` or `v1-fallback`.
3. Keep color/status mapping Spectrum-compliant.

### API v1 Fallback Policy

- Default to API v2 for all reads/writes.
- Use API v1 only when v2 cannot serve the required visualization (for example endpoint `404/501` or missing required fields).
- If any module uses v1, explicitly disclose it in output.
- Do not switch the whole task to v1 if only one module needs fallback.

Minimal fallback pattern:

```python
import subprocess, json

def prtg_get_v1(path):
    # Uses the same token, but v1 expects query params.
    r = subprocess.run(
        ['curl', '-s', '-k', f'{HOST}/api/{path}&apitoken={KEY}'],
        capture_output=True, text=True, timeout=30)
    if not r.stdout.strip():
        raise RuntimeError(f"Empty v1 response (path={path})")
    return json.loads(r.stdout)
```

Common v1 fallback endpoints for visuals:

- Object tables: `table.json?content=sensors|devices|groups&output=json`
- Historic series: `historicdata.json?id=<sensorid>&avg=<seconds>&sdate=<start>&edate=<end>`

---

## Schema Endpoints

Four distinct endpoints — use the right one for the right purpose:

| Endpoint | Purpose |
|----------|---------|
| `GET /experimental/schemas/{parentId}` | List all sensor kinds creatable under a parent |
| `GET /experimental/schemas/{parentId}/post?kind={kind}` | POST body schema for creating a specific kind |
| `GET /experimental/schemas/{objectId}/patch?include=all_sections` | PATCH schema for an existing object |
| `GET /experimental/schemas/{objectId}/get?include=all_sections` | GET schema for an existing object |

All responses are OAS 3.0.3 documents. The actual schema is always at `components.schemas.modifyItemSchema`.

### Kind listing (`GET /experimental/schemas/{parentId}`)

Returns an array. Key fields per entry:

```json
{
  "creatable": true,
  "hints": ["CredentialsMissing"],
  "kind": "snmpdiskfree",
  "name": "SNMP Disk Free",
  "flags": ["NeedsProbe", "HasMetaScan", "NeedsCredentials"],
  "metascan_field": "diskfree.disk",
  "credential_group": "snmpcredentials",
  "metascan_href": "/experimental/devices/40/metascan?kind=snmpdiskfree"
}
```

- **`flags`**: `HasMetaScan` = requires metascan before creation; `NeedsCredentials` = device must have `credential_group` configured
- **`metascan_field`**: dot-notation path in the POST body where the metascan selection goes (e.g. `"diskfree.disk"` → `body["diskfree"]["disk"]`)
- **`metascan_href`**: **broken — missing `/api/v2` prefix** (see gotcha #34). Construct the URL yourself.
- **`hints`** when `creatable: false`: `CredentialsMissing`, `ProbeIsDisconnected`, `SensorNeedsLocalProbe`, `MissingCredentialGroup`, etc.

### x-prtg-meta extension

Every schema field carries an `x-prtg-meta` object — the primary source of truth for rendering:

| field | Meaning |
|-------|---------|
| `class` | Input type: `edit`, `integer`, `combo`, `radio`, `tags`, `lookuplist`, `lookupchecklistbox`, `lookupfilelist`, `password`, `information` (read-only — never prompt), `section` |
| `required` | `true` = must provide even if a default exists |
| `sortIndex` | Display order within the section |
| `options` | For `combo`/`radio`: `{"0": "Off", "1": "On"}` |
| `lookupkey` | For `lookuplist`: key to pass to `GET /setting-lookups/{key}` |
| `inheritable` | On a section object: the section can inherit from parent |
| `editOnRequest` | Metascan must be triggered before values are available |

---

## Inheritance

### Fetching with inheritance metadata

Add `inheritance` to the `include` parameter alongside any sections you want:

```python
device = prtg_get('devices/40?include=intervalgroup,inheritance')
sensor = prtg_get('sensors/11476?include=all_sections,inheritance')
```

This adds three fields inside each inheritable section:

```json
"intervalgroup": {
  "_inherited": true,
  "_inheritancesource": { "id": "2993", "name": "MyGroup", "type": "REFERENCED_GROUP", "href": "/api/v2/groups/2993" },
  "_shadowed": { "interval": "60" },
  "interval": "3600"
}
```

| Field | Meaning |
|-------|---------|
| `_inherited` | `true` = currently using the parent's value |
| `_inheritancesource` | The ancestor providing the value (id, name, type, href) |
| `_shadowed` | Previously-set local override, preserved server-side when inheritance was re-enabled |
| effective values | The actual values in effect (whether inherited or local) |

**Without `include=inheritance`**, only effective values are returned — you cannot tell if a value is inherited or local.

### Patching inheritance

```python
# Override: stop inheriting, set own value
prtg_request('PATCH', f'experimental/sensor/{sensor_id}',
    {"intervalgroup": {"_inherited": False, "interval": "300"}})

# Restore: switch back to inheriting from parent
prtg_request('PATCH', f'experimental/sensor/{sensor_id}',
    {"intervalgroup": {"_inherited": True}})
```

### Display logic for a settings wizard

- `_inherited: true` → show `"Inheriting '3600' from MyGroup"`, offer override option
- `_shadowed` present → additionally offer `"Restore previous value: 60"`
- `_inherited: false` → show current value, allow edit, offer `"Reset to inherit"`

---

## Metascan

A server-side discovery operation: the probe connects to the target device and enumerates available resources (disks, scripts, SNMP OIDs, etc.) to populate the sensor's key configuration field before creation.

### How to call it

```python
# Must be POST. Must have a JSON body (even {}).
result = prtg_request('POST', f'experimental/devices/{device_id}/metascan?kind={kind}', {})
```

- `GET` returns `404`
- `POST` with no body returns `400 EOF`
- Kind must have `HasMetaScan` in its flags — otherwise `400: "sensor kind does not support metascan"`
- Device must be reachable with appropriate credentials

### Response

Array of discovered items. Shape varies by kind. Example for `snmpdiskfree`:

```json
[
  { "disk": "C:", "info": { "disk": "C:", "type": "Fixed" } },
  { "disk": "D:", "info": { "disk": "D:", "type": "Fixed" } }
]
```

The field name (e.g. `disk`) matches the `required` array in the POST schema's metascan item schema. `info` provides human-readable display values.

### Including metascan selection in the POST body

The `metascan_field` from the kind listing gives you the dot-notation path:

```python
# metascan_field = "diskfree.disk" → body["diskfree"]["disk"] = selected value
body = {
    "basic": {"name": "Disk Free C:"},
    "diskfree": {"disk": "C:"}
}
prtg_request('POST', f'experimental/devices/{device_id}/sensor?kindid=snmpdiskfree', body)
```

---

## Setting Lookups

Fields with `class: lookuplist` in `x-prtg-meta` can be resolved to human-readable options:

```python
lookups = prtg_get(f'setting-lookups/{lookupkey}?id={object_id}')
# Returns: [{"intervalid": "60;60 seconds;", "info": {"C0": "60", "C1": "60 seconds"}}, ...]

# Build options dict for display
options = {item['info']['C0']: item['info']['C1'] for item in lookups}
# {"60": "60 seconds", "300": "5 minutes", ...}
```

- **`info.C0`** = the value to send in PATCH (e.g. `"60"`)
- **`info.C1`** = the display label (e.g. `"60 seconds"`)
- **Never** send the full key string (e.g. `"60;60 seconds;"`) as the value

```python
# Send C0 value in PATCH
prtg_request('PATCH', f'experimental/sensor/{sensor_id}',
    {"intervalgroup": {"_inherited": False, "interval": "300"}})
```

---

## Scripts

- **`${CLAUDE_SKILL_DIR}/scripts/update_docs.py`** — Refresh API docs from the live PRTG server. Run from your working directory (where the `*.env` file is). Outputs to `docs/` and `prtg_api_resolved.yaml` in the CWD.
  ```bash
  python3 "${CLAUDE_SKILL_DIR}/scripts/update_docs.py"
  ```
- **`${CLAUDE_SKILL_DIR}/scripts/fetch_spectrum.py`** — Download `spectrum.css` from your PRTG server. Run from your working directory.
  ```bash
  python3 "${CLAUDE_SKILL_DIR}/scripts/fetch_spectrum.py"
  ```

---

## Task

$ARGUMENTS
