# PRTG Skill Use Cases

This file is a prompt catalog for users and a behavior guide for the skill.

Scope:
- PRTG API v2 first.
- API v1 fallback only when required for missing/unsupported v2 behavior.
- Spectrum-themed output for dashboards and visual reporting.

## 1) Orientation and Inventory

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Installation overview | `/prtg Give me a high-level overview of this PRTG installation.` | Query probes, groups, devices, sensors; summarize totals and health. |
| Probe inventory | `/prtg List all probes and their current status.` | Query probes and show status distribution. |
| Group inventory | `/prtg Show all groups under each probe.` | Build hierarchical probe -> group listing. |
| Device inventory | `/prtg List all devices in group 53.` | Query devices filtered by `parentid`. |
| Sensor inventory | `/prtg List sensors for device 2490.` | Query sensors by device `parentid`. |
| Sensor type inventory | `/prtg Show me top sensor kinds by count.` | Aggregate by `kind_name`. |
| Health baseline | `/prtg What percent of sensors are UP vs DOWN/WARNING?` | Compute status percentages and counts. |
| Device health baseline | `/prtg Which devices currently have down sensors?` | Use `include=sensor_status_summary` and filter down count > 0. |
| Coverage snapshot | `/prtg How many devices have no sensors?` | Compare device count and sensor parent mappings. |
| Object path lookup | `/prtg Show full path for sensor 6859.` | Resolve `path` array and parent references. |

## 2) Triage and Incident Response

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Current incidents | `/prtg Show everything DOWN or WARNING right now.` | Query down + warning sensors, return grouped triage view. |
| Incident grouping | `/prtg Group active problems by device, then by sensor type.` | Multi-level aggregation by parent and `kind_name`. |
| Worst offenders | `/prtg Top 20 devices by number of down sensors.` | Rank devices by down counts. |
| New failures | `/prtg What turned down in the last 2 hours?` | Use `status_since` where available and filter by time window. |
| Long-running failures | `/prtg Which sensors have been down the longest?` | Sort down sensors by `status_since` ascending. |
| Ack workflow | `/prtg Acknowledge all down sensors on device 8019 with ticket INC-4521.` | POST acknowledge for matching sensors. |
| Pause noisy device | `/prtg Pause device 8019 for maintenance.` | POST pause action and confirm state. |
| Resume after maintenance | `/prtg Resume device 8019 and re-scan all sensors.` | Resume + trigger scans on sensors. |
| Partial outage mapping | `/prtg Show devices with WARNING but no DOWN sensors.` | Use status summary and filtered lists. |
| Ownership view | `/prtg Build a triage list by group owner tag.` | Use tags/metadata to organize incident queue. |

## 3) Deep Investigation

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Device deep dive | `/prtg Deep dive device 2490: all sensors, statuses, and status_since.` | Full device sensor table with timestamps and types. |
| Problem-context expansion | `/prtg For down sensors on Exchange, include sibling healthy sensors for context.` | Fetch all sensors for affected device(s). |
| Channel inspection | `/prtg Show all channels for sensor 6859 with units.` | Query channels endpoint and map display units. |
| Last value diagnostics | `/prtg Include last_measurement for each down sensor.` | Add latest numeric/display values where available. |
| Parent chain tracing | `/prtg For each down sensor, show probe/group/device path.` | Resolve parent path chain for each incident item. |
| Compare two devices | `/prtg Compare health and sensor mix for devices 2490 and 8019.` | Side-by-side tables and deltas. |
| Kind-focused drilldown | `/prtg Investigate all Ping sensors currently warning.` | Filter by status then kind client-side if needed. |
| Stability check | `/prtg Show sensors that changed status most often today.` | Build flap proxy from repeated snapshots/timeseries state transitions. |
| Warning root-cause shortlist | `/prtg For warning sensors, suggest top 3 likely causes by sensor kind.` | Heuristic mapping from kind to probable causes. |
| Dependency hints | `/prtg Cluster down sensors by shared parent path segments.` | Group incidents by topology-like path similarities. |

## 4) Timeseries and Performance Trends

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Single sensor trend | `/prtg Plot last 30 days for sensor 6859.` | Fetch medium window timeseries, map channel IDs to names. |
| Multi-sensor comparison | `/prtg Compare CPU trends for 5 key servers.` | Fetch series for each sensor and chart overlays. |
| Bandwidth trend | `/prtg Show 7-day inbound/outbound traffic trends for core switches.` | Query traffic sensors and chart key channels. |
| Ping trend | `/prtg Build a latency trend dashboard for branch sites.` | Combine ping series per site and render line chart. |
| Memory pressure trend | `/prtg Show memory utilization trend and daily peak.` | Compute aggregate stats from series. |
| Disk runway | `/prtg Estimate days until disk exhaustion for top 10 critical disks.` | Trend slope projection from disk free series. |
| Percentile analysis | `/prtg For latency, show p50/p95 over last 14 days.` | Derive percentiles from timeseries points. |
| Drift detection | `/prtg Detect sensors with sustained 20% increase from baseline.` | Baseline vs current window delta analysis. |
| Weekend pattern | `/prtg Compare weekday vs weekend traffic patterns.` | Time-bucket and compare distributions. |
| Capacity anomaly | `/prtg Flag sensors with unusual spikes in last 24h.` | Outlier logic over short window points. |

## 5) Visualization and Dashboards

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Executive dashboard | `/prtg Build an exec dashboard with KPIs and top risks.` | Generate concise high-level HTML with key charts. |
| Operations dashboard | `/prtg Build an ops dashboard with live triage and trend panels.` | Multi-panel dashboard with incidents + trends. |
| Security dashboard | `/prtg Build SSL risk dashboard with expiry tiers and vulnerable endpoints.` | SSL-focused sections and risk categorization. |
| Group status heatmap | `/prtg Add a group/device status heatmap.` | Color-intensity matrix using status counts. |
| Triage matrix | `/prtg Add status x sensor-type triage matrix.` | Crosstab heat table to prioritize work. |
| Flapping leaderboard | `/prtg Add top flapping sensors panel for last 24h.` | Rank by estimated status change frequency. |
| SLA bars | `/prtg Add uptime bars by group with target thresholds.` | Bullet/progress bars with threshold markers. |
| Blast radius panel | `/prtg Add impacted device/sensor count per major outage.` | Aggregate and link outage footprint. |
| Interactive drill-down | `/prtg Make each group row expandable to affected devices.` | Collapsible sections with details. |
| Boardroom export | `/prtg Produce a print-friendly dashboard HTML.` | Landscape/print CSS and summary-first structure. |

## 6) Provisioning and Configuration Changes

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Create ping sensor | `/prtg Add Ping sensor "Uptime Watchdog" to device 42.` | POST sensor creation with `kindid=ping`. |
| Bulk sensor creation | `/prtg Add Ping sensors to all devices in group 53.` | Iterate devices and create sensors safely. |
| Rename sensor | `/prtg Rename sensor 2490 to "Web RTT Primary".` | PATCH sensor name via correct endpoint. |
| Set scan interval | `/prtg Set scan interval to 60s for sensor 2490.` | Patch interval section where supported. |
| Pause sensor | `/prtg Pause sensor 2490 for 2 hours.` | Trigger pause action and return confirmation. |
| Resume sensor | `/prtg Resume sensor 2490 now.` | Resume action call and status check. |
| Trigger immediate scan | `/prtg Trigger scan on all warning sensors in device 8019.` | Iterate action calls for target sensors. |
| Bulk acknowledge | `/prtg Acknowledge all DOWN ping sensors with ticket INC-9001.` | Filter + bulk action with response summary. |
| Delete test sensors | `/prtg Delete sensors named "Uptime Watchdog" in group 53.` | Find by name + delete safely. |
| Safe change preview | `/prtg Dry-run: show what would be changed before applying.` | Plan list output before executing writes. |

## 7) Maintenance and Compliance Workflows

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Maintenance precheck | `/prtg Pre-maintenance report for group "Core Network".` | Snapshot health, active alerts, risky sensors. |
| Maintenance muting | `/prtg Pause all sensors on device 2490 and tag maintenance window.` | Bulk pause and annotate actions. |
| Maintenance rollback | `/prtg Resume paused sensors from today's maintenance run.` | Resume only targeted paused set. |
| SSL expiry audit | `/prtg List all SSL cert sensors expiring in <30 days.` | Pull expiry channel values and rank urgency. |
| Compliance snapshot | `/prtg Weekly compliance summary: uptime, down incidents, ack latency.` | Aggregate KPI report for governance. |
| Stale alert cleanup | `/prtg Find alerts older than 7 days without acknowledgement.` | Status age + ack state filtering. |
| Tag hygiene | `/prtg Show devices missing required tags: owner, env, criticality.` | Metadata completeness report. |
| Naming hygiene | `/prtg Find sensors with non-standard names.` | Pattern checks and rename recommendations. |
| Coverage gaps | `/prtg Show production devices missing Ping or CPU sensors.` | Coverage matrix and remediation list. |
| Policy breach alerts | `/prtg Which critical devices are paused right now?` | Filter by tags/criticality + paused state. |

## 8) Reporting and Summaries

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Daily operations brief | `/prtg Generate morning ops brief.` | Summarize overnight incidents and current risks. |
| Weekly trend report | `/prtg Build weekly health trend summary with charts.` | Produce KPI deltas + trend visuals. |
| Executive one-pager | `/prtg Create executive summary for leadership.` | Risk-focused concise narrative with metrics. |
| Team handoff note | `/prtg Draft shift handoff with open incidents and actions.` | Structured handoff text for next shift. |
| Device report card | `/prtg Build report card for device 2490.` | Availability, incidents, trend and recommendations. |
| Group report card | `/prtg Build report card for group 53.` | Aggregated health by device and sensor kind. |
| Incident timeline summary | `/prtg Summarize major incidents from last 24h.` | Chronological outage and recovery highlights. |
| Remediation impact report | `/prtg Compare health before/after maintenance on 2026-03-10.` | Time-window delta analysis. |
| Asset risk ranking | `/prtg Rank top 25 risky devices by outage frequency and severity.` | Composite scoring and sorted table. |
| Export-ready tables | `/prtg Output CSV-friendly table for all down sensors with path and owner.` | Normalized table format for export. |

## 9) Query Patterns and Discovery Helpers

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Filter syntax helper | `/prtg Build a filter for sensors named "Ping v2" that are down.` | Correct filter expression with quoting rules. |
| Parent/child lookup | `/prtg Find all sensors under group 53.` | Two-step group -> devices -> sensors query. |
| Include usage | `/prtg Which include flags are useful on devices endpoint?` | Explain `include=sensor_status_summary` and options. |
| Pagination helper | `/prtg Pull all devices even if there are more than 3000.` | Offset/limit loop query pattern. |
| Channel mapping helper | `/prtg Explain channel ID to name mapping for timeseries.` | `/experimental/channels` plus remap strategy. |
| Schema introspection | `/prtg Show patch schema sections for sensor 2490.` | Schema endpoint and section awareness. |
| Endpoint chooser | `/prtg Which endpoint should I use to rename a sensor?` | Correct singular sensor patch path guidance. |
| Status normalization | `/prtg Normalize device and sensor statuses for one report.` | Remove prefixes and unify status buckets. |
| Tag-based discovery | `/prtg Find all devices tagged "prod" and "db".` | Filter/tag query or client-side narrowing. |
| Fast health query | `/prtg Fast query: only totals and down/warning counts.` | Minimal endpoint set for low-latency answer. |

## 10) API v1 Fallback-Specific Use Cases

Use these only if v2 cannot fulfill required data shape.

| Use Case | Example Prompt | Fallback Behavior |
|---|---|---|
| Historic series fallback | `/prtg If v2 timeseries fails, fetch historic series for sensor 6859.` | Switch only this module to `historicdata.json`. |
| Table fallback for legacy data | `/prtg Use legacy table output for sensor inventory if needed.` | Use `table.json` for missing v2 fields. |
| Mixed-source dashboard | `/prtg Build dashboard, but annotate modules using v1 fallback.` | Mark each panel with source `v2` or `v1-fallback`. |
| Graceful unsupported handling | `/prtg If endpoint returns 501, continue with partial report.` | Skip failed module or fallback narrowly; keep report usable. |
| Fallback disclosure | `/prtg Tell me exactly which sections used v1 and why.` | Explicit section-level disclosure. |

## 11) Ready-to-Use Prompt Pack

Use these as drop-in prompts.

1. `/prtg Show current down/warning sensors grouped by device and sorted by impact.`
2. `/prtg Find devices with down sensors and include sensor_status_summary counts.`
3. `/prtg Deep dive on the worst device and include status_since for every sensor.`
4. `/prtg Build a Spectrum dashboard with KPIs, heatmap, triage matrix, and trends.`
5. `/prtg Add ping sensor "Uptime Watchdog" to device 42 and trigger scan.`
6. `/prtg Acknowledge all DOWN sensors in group 53 with ticket INC-4521.`
7. `/prtg Show SSL sensors with days-to-expiry and risk tiers (<0, <30, <180, healthy).`
8. `/prtg Plot 30-day CPU, memory, and traffic trends for core infrastructure.`
9. `/prtg Rank top 20 devices by outage severity score (down*3 + warning*2).`
10. `/prtg Create a morning ops brief with active incidents and overnight changes.`
11. `/prtg Compare health snapshot now vs 24 hours ago for all production groups.`
12. `/prtg Build a weekly executive summary with charts and top risks.`
13. `/prtg Find sensors that appear to flap frequently in the last day.`
14. `/prtg Show devices missing required monitoring coverage (Ping + CPU + Disk).`
15. `/prtg Pause all sensors on device 8019 for maintenance and confirm actions.`
16. `/prtg Resume maintenance-paused sensors and trigger immediate scans.`
17. `/prtg Output CSV-style rows for all active incidents with full path and kind.`
18. `/prtg If needed, fallback to v1 for timeseries only and disclose it clearly.`
19. `/prtg Build an SLA by group panel with uptime percentages and target markers.`
20. `/prtg Generate a print-friendly board report from current monitoring state.`

## 12) Scheduling and Notifications

| Use Case | Example Prompt | Expected Skill Behavior |
|---|---|---|
| Daily status digest | `/prtg Create a daily 8:00 AM ops digest with current DOWN/WARNING counts.` | Generate a scheduled-report recipe and output format for daily summary delivery. |
| Shift-start briefing | `/prtg Build a 7:00 AM handoff brief for NOC shift changes.` | Assemble overnight incident delta + current queue for scheduled use. |
| Weekly leadership summary | `/prtg Prepare a weekly Monday 9:00 AM executive health summary.` | Produce leadership-focused KPI/trend template for recurring runs. |
| Business-hours alert filter | `/prtg Notify only for DOWN on critical devices during business hours.` | Define severity + tag filters and time-window gating logic. |
| After-hours escalation | `/prtg For critical DOWN after hours, send high-priority escalation.` | Separate alert routing by schedule and criticality tags. |
| Maintenance window suppressions | `/prtg Suppress notifications for group 53 during Sunday maintenance window.` | Apply schedule-aware muting/pausing guidance and rollback plan. |
| Reminder for stale incidents | `/prtg Send reminder when an incident is unacknowledged for 30 minutes.` | Build reminder rule based on `status_since` and ack state. |
| Recovery notification | `/prtg Notify when a previously DOWN service returns to UP.` | Track state transition and emit recovery message template. |
| Burst-control notifications | `/prtg If more than 20 sensors fail in 10 minutes, send one aggregate alert.` | Create dedup/aggregation strategy to avoid notification storms. |
| Group owner routing | `/prtg Route alerts by owner tag and include runbook link.` | Use tags/metadata mapping to target recipients and context. |
| SSL expiry reminder cadence | `/prtg Send cert expiry notifications at 30d, 14d, 7d, and 1d.` | Tiered schedule plan from SSL days-to-expiry values. |
| Capacity warning cadence | `/prtg Send daily warnings for disks projected to fill within 14 days.` | Scheduled capacity report with threshold-based recipients. |
| Flapping sensor noise control | `/prtg Notify only if a sensor flaps more than 5 times per hour.` | Gate notifications with flap threshold before dispatch. |
| Environment-aware channels | `/prtg Send prod alerts to PagerDuty and non-prod to email.` | Route by environment tag and severity policy. |
| Change-freeze mode | `/prtg During release freeze, notify on warning-level and above for core systems.` | Temporary stricter policy window and automatic expiry. |

Notification output templates the skill can generate:

1. `Ops Digest`: summary counts, top affected groups, top 10 incidents, since-time.
2. `Immediate Incident`: object path, severity, first seen, latest value, likely owner.
3. `Recovery Notice`: outage duration, impact count, current state, follow-up actions.
4. `Compliance Reminder`: aging incidents, missing acknowledgements, SLA risk list.

## 13) Design Intent for Skill Behavior

When these use cases are invoked, the skill should:

1. Prefer v2 endpoints and correct filter syntax.
2. Set practical limits and paginate for large environments.
3. Normalize statuses for clear reporting.
4. Use channel-name mapping before showing timeseries.
5. Keep outputs concise first, then provide drill-down detail.
6. Disclose write actions and confirm object IDs.
7. Disclose any module-level v1 fallback with reason.
8. Keep dashboard visuals Spectrum-aligned and accessible.
