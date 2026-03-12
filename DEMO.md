# PRTG Skill Demo Script

A scripted walkthrough showing what the PRTG skill for Claude Code can do.
Each section is a prompt you type, followed by what Claude does behind the scenes and what the audience sees.

---

## Prerequisites

1. PRTG skill installed at `~/.claude/skills/prtg`
2. A `prtg.env` file in the working directory with `PRTG_HOST` and `PRTG_API_KEY`
3. Spectrum CSS downloaded (`python3 ~/.claude/skills/prtg/scripts/fetch_spectrum.py`)
4. A PRTG instance with some devices, sensors, and ideally a few in DOWN/WARNING state

---

## Act 1: Orientation — "What are we working with?"

### Prompt 1: Get the lay of the land

```
/prtg Give me a high-level overview of this PRTG installation. How many probes,
groups, devices, and sensors are there? Summarize the health — how many sensors
are up, down, warning, and paused?
```

**What happens:** Claude queries `/experimental/probes`, `/experimental/groups`,
`/experimental/devices?include=sensor_status_summary`, and
`/experimental/sensors` with `limit=3000`. It aggregates totals and status
breakdowns, then prints a concise summary table.

**Why it's cool:** One natural-language sentence replaces clicking through the
PRTG UI and mentally tallying numbers across pages.

---

## Act 2: Triage — "What's broken right now?"

### Prompt 2: Find all problems

```
/prtg Show me everything that's currently down or in a warning state.
Group the results by device so I can see which devices are most affected.
```

**What happens:** Claude queries sensors filtered by `status = down` and
`status = warning`, fetches parent device info, and groups the output by device.
Each device shows its affected sensors with their status, kind, and last value.

**Why it's cool:** This is the "9 AM Monday morning" use case — a single prompt
replaces navigating the sensor tree and mentally grouping problems.

---

### Prompt 3: Investigate a problem device

```
/prtg That device with the most down sensors — give me the full picture. Show me
all its sensors (including healthy ones), when each status started, and pull the
last 2 days of timeseries data for any sensor that's currently down.
```

**What happens:** Claude identifies the worst device from the previous results,
queries all its sensors via `parentid` filter, fetches `status_since` from the
experimental endpoint, then pulls timeseries data (`/experimental/timeseries/{id}/short`)
for each down sensor, mapping channel IDs to human-readable names.

**Why it's cool:** Multi-step investigation that would take several minutes of
clicking in the PRTG UI — done in seconds with full context carried forward from
the previous question.

---

## Act 3: Take Action — "Fix it"

### Prompt 4: Acknowledge alarms

```
/prtg Acknowledge all the down sensors on that device with the message
"Investigating — ticket INC-4521 opened". Then pause the device itself so we
don't get more alerts while we troubleshoot.
```

**What happens:** Claude calls `POST /sensors/{id}/acknowledge` for each down
sensor with the acknowledgment message, then calls `POST /devices/{id}/pause`
on the parent device. It confirms each action and summarizes what was done.

**Why it's cool:** Write operations! The skill isn't read-only — it can take
real action. Acknowledging + pausing in one prompt is a workflow that normally
requires multiple clicks per sensor.

---

### Prompt 5: Create new monitoring

```
/prtg Pick a device that's currently healthy and add a new Ping sensor to it
called "Uptime Watchdog". Then trigger an immediate scan so we can see the
first result.
```

**What happens:** Claude picks an UP device, calls
`POST /experimental/devices/{id}/sensor?kindid=ping` with the name in the body,
then calls `POST /sensors/{id}/scan` on the new sensor. It reports back the new
sensor ID and first reading.

**Why it's cool:** Provisioning new monitoring through conversation. No need to
navigate the "Add Sensor" wizard.

---

## Act 4: The Dashboard — "Make it visual"

### Prompt 6: Build a live status dashboard

```
/prtg Build me a Spectrum-themed HTML dashboard that shows:
1. A summary bar at the top with total counts (devices, sensors by status)
2. A device health grid — one card per device, colored by worst sensor status,
   showing sensor count breakdown
3. A "Problem List" section at the bottom with every down/warning sensor
Save it as dashboard.html.
```

**What happens:** Claude reads the Spectrum design system reference, queries all
devices with `include=sensor_status_summary`, queries down/warning sensors, then
generates a single-file HTML page using Spectrum CSS custom properties for
colors, typography, and spacing. Status colors map to the official PRTG palette
(green/red/orange/grey).

**Why it's cool:** This is the visual showstopper. The dashboard looks
professional and matches PRTG's own design language because it uses the real
Spectrum tokens. It's a self-contained HTML file — no build step, no framework,
just open it in a browser.

---

### Prompt 7: Add timeseries charts

```
/prtg Now enhance the dashboard. Add an expandable "Trend" section to each
device card. When I click a device, it should expand to show a Chart.js line
chart with the last 30 days of timeseries data for each sensor on that device.
Use the Spectrum chart color palette. Label the channels by name, not ID.
```

**What happens:** Claude modifies `dashboard.html` to include Chart.js via CDN,
adds click-to-expand behavior on device cards, and for each device embeds the
timeseries data (fetched via `/experimental/timeseries/{id}/medium`). Channel
IDs are mapped to names via the channels endpoint. Charts use the Spectrum
60-level palette (blue, green, dark-orange, cyan, purple, magenta).

**Why it's cool:** Interactive charts with real historical data, styled to match
PRTG's design language, generated from a single English sentence. This is
usually a multi-day project — here it takes one prompt.

---

## Visualization Upgrade Prompts (Optional)

Use these after Prompt 7 when you want broader visual coverage:

### Prompt A: Status heatmap + triage matrix

```
/prtg Add two modules: (1) a group/device status heatmap and (2) a matrix that
counts sensors by status and sensor type. Keep Spectrum colors and add tooltips.
```

### Prompt B: SLA and flapping focus

```
/prtg Add SLA-style uptime bars by group and a top-15 flapping sensor leaderboard
for the last 24 hours. Mark any module that needed API v1 fallback.
```

### Prompt C: Capacity and risk

```
/prtg Add capacity forecast charts (disk and memory) and an SSL risk tier panel
(expired, <30d, <180d, healthy) with clickable drill-down rows.
```

These prompts map to the visualization presets in
`references/visualization-patterns.md` and keep API v2 as the default source.

---

## Act 5: Clean Up — "Undo the demo"

### Prompt 8: Resume the paused device and remove the test sensor

```
/prtg Resume the device we paused earlier. Also delete the "Uptime Watchdog"
sensor we created — it was just for the demo.
```

**What happens:** Claude calls `POST /devices/{id}/resume` and
`DELETE /experimental/sensors/{id}`, confirming each action.

**Why it's cool:** Clean teardown shows the skill handles the full lifecycle:
create, modify, delete.

---

## Recap for the Audience

| Act | What We Did | Key Capability |
|-----|-------------|---------------|
| 1 | High-level infrastructure overview | Multi-endpoint aggregation |
| 2 | Triage — find & group all problems | Filtered queries + grouping |
| 3 | Deep investigation with timeseries | Multi-step analysis, context carryover |
| 4 | Acknowledge alarms + pause device | Write operations (POST) |
| 5 | Create new sensor + trigger scan | Provisioning (POST + create) |
| 6 | Spectrum-themed status dashboard | HTML generation with design system |
| 7 | Interactive timeseries charts | Chart.js + channel name mapping |
| 8 | Clean up demo artifacts | Delete + resume lifecycle |

**Total prompts:** 8
**Total time:** ~10 minutes
**What it replaces:** Hours of UI navigation, manual data aggregation, and custom dashboard development.

---

## Tips for Running the Demo

- **Have some problems.** If your PRTG instance is 100% green, the triage
  section is boring. Pause a few sensors beforehand to create interesting state.
- **Use a group with 5-15 devices.** Too few and the dashboard is sparse; too
  many and API calls take longer.
- **Pre-download spectrum.css.** The `fetch_spectrum.py` step can take a moment
  and isn't interesting to watch.
- **Have a browser open.** After Prompt 6, open `dashboard.html` immediately so
  the audience sees the visual result.
- **The prompts build on each other.** Each one references results from the
  previous step. Run them in order within a single Claude Code session.
