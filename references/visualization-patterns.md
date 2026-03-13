# Visualization Patterns (API v2 First)

Use this reference when users ask for richer dashboard visuals beyond KPI cards and basic line charts.

## Rules

- Default to API v2 (`/api/v2`) for all data access.
- Fall back to API v1 (`/api`) only when a required v2 endpoint is unavailable, incomplete, or returns a server-side unsupported error.
- When falling back, state clearly which visualization uses v1 and why.
- Keep status colors aligned with Spectrum tokens from `spectrum-design-system.md`.

## Recommended Visualization Modules

| Pattern | What it answers | Preferred data (v2) | Optional fallback (v1) |
|---|---|---|---|
| Probe/Group Status Heatmap | "Where are problems concentrated?" | `/experimental/devices?include=sensor_status_summary` | `/api/table.json?content=devices` |
| 24h Status Timeline (stacked area) | "Are alerts rising or recovering?" | `/experimental/timeseries/{sensorId}/{window}` + `/experimental/channels` | `/api/historicdata.json?id={sensorId}` |
| Top N Flapping Sensors | "Which sensors keep changing state?" | `/experimental/sensors` + `status_since` sampling over time | `/api/table.json?content=sensors` snapshots |
| SLA/Uptime by Group (bullet bars) | "Which groups miss target?" | `/experimental/devices` + status summaries | `/api/table.json?content=devices` |
| Latency Percentile Bands (p50/p95) | "Is performance degrading before outage?" | Timeseries from selected latency sensors | `/api/historicdata.json` |
| Dependency Blast Radius (node-link) | "If this device fails, what is impacted?" | `/experimental/objects` path hierarchy | `/api/table.json?content=groups,devices,sensors` |
| Capacity Forecast (disk/memory trendline) | "When do we run out?" | Timeseries + linear projection in JS | `/api/historicdata.json` |
| Alert Triage Matrix (status x kind) | "What kind of failures dominate?" | `/experimental/sensors` (`status`, `kind_name`) | `/api/table.json?content=sensors` |

## Baking Into The Skill

Add a "visualization preset" concept to prompt handling. Ask (or infer) one of:

- `exec-view`: incident triage, high-level health, blast radius
- `ops-view`: performance trends, flapping sensors, capacity forecast
- `security-view`: SSL expiry, cert risk tiers, vulnerable endpoints

For each preset, generate:

1. Data queries (v2 first) with explicit endpoint list.
2. Transform steps (grouping, pivot, ranking, time bucketing).
3. UI blocks (cards/charts/tables) in a deterministic order.
4. Fallback markers for modules that needed v1.

## API v1 Fallback Triggers

Use fallback only if one of these happens:

- `404` or `501` from a needed v2 endpoint.
- Valid v2 response is structurally missing required fields for the selected visualization.
- Timeseries shape is incompatible and cannot be safely normalized.

Do not fallback for convenience.

## Fallback Disclosure Snippet

Use wording like:

`Used API v1 for timeseries in "Latency Percentile Bands" because v2 endpoint returned 501 on this instance. All other modules use API v2.`

## Data Contract For Generated Dashboards

When embedding data in HTML/JS, keep this normalized structure:

```json
{
  "kpis": { "devices": 0, "sensors": 0, "down": 0, "warning": 0 },
  "modules": [
    { "id": "statusHeatmap", "source": "v2", "rows": [] },
    { "id": "slaByGroup", "source": "v2", "rows": [] },
    { "id": "latencyBands", "source": "v1", "rows": [] }
  ]
}
```

This makes mixed-source dashboards explicit and easier to debug.
