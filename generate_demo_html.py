#!/usr/bin/env python3
"""Generate HTML demo walkthrough + redesigned dashboard in a target subdirectory."""

import subprocess, json, glob, urllib.parse, os, html as html_mod, collections
import sys
from datetime import datetime

# --- PRTG connection ---
env_files = sorted(p for p in glob.glob('*.env') if p != '.env.example')
env = dict(line.strip().split('=', 1) for line in open(env_files[0]) if '=' in line and not line.startswith('#'))
HOST, KEY = env['PRTG_HOST'].rstrip('/'), env['PRTG_API_KEY']

def prtg_get(path):
    r = subprocess.run(
        ['curl', '-s', '-k', f'{HOST}/api/v2/{path}', '-H', f'Authorization: Bearer {KEY}'],
        capture_output=True, text=True, timeout=60)
    if not r.stdout.strip():
        raise RuntimeError(f'Empty response (path={path})')
    return json.loads(r.stdout)

def prtg_get_v1(path):
    sep = '&' if '?' in path else '?'
    r = subprocess.run(
        ['curl', '-s', '-k', f'{HOST}/api/{path}{sep}apitoken={KEY}'],
        capture_output=True, text=True, timeout=60)
    if not r.stdout.strip():
        raise RuntimeError(f'Empty response (v1 path={path})')
    return json.loads(r.stdout)

def get_ts_named(sensor_id, window='medium'):
    ch_params = urllib.parse.urlencode({'filter': f'parentid = "{sensor_id}"', 'limit': '100'})
    channels = prtg_get(f'experimental/channels?{ch_params}')
    ch_map = {str(ch['id']): ch['name'] for ch in channels}
    ts = prtg_get(f'experimental/timeseries/{sensor_id}/{window}')
    if not ts or not isinstance(ts[0], list):
        return [], ch_map
    header = ts[0]
    rows = []
    for row in ts[1:]:
        if isinstance(row, list) and len(row) == len(header):
            named = {'time': row[0]}
            for i in range(1, len(header)):
                named[ch_map.get(header[i], header[i])] = row[i]
            rows.append(named)
    return rows, ch_map

OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else 'demo'
os.makedirs(OUT_DIR, exist_ok=True)
E = html_mod.escape
NOW = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
PRTG_LOGO_SVG = """
<svg class="brand-mark" viewBox="0 0 56 56" role="img" aria-label="PRTG" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="prtgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F67FF" />
      <stop offset="100%" stop-color="#050F34" />
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="52" height="52" rx="14" fill="url(#prtgGradient)" />
  <circle cx="20" cy="28" r="5.5" fill="#FFFFFF" />
  <circle cx="36" cy="20" r="4.5" fill="#74ABFF" />
  <circle cx="36" cy="36" r="4.5" fill="#A4AD19" />
  <path d="M25 28H31M31 28L34 25M31 28L34 31" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" />
</svg>
"""

# =====================================================================
# FETCH ALL DATA
# =====================================================================
print("Fetching data from PRTG...")
probes = prtg_get('experimental/probes?limit=100')
groups = prtg_get('experimental/groups?limit=3000')
devices = prtg_get('experimental/devices?limit=3000&include=sensor_status_summary')
sensors = prtg_get('experimental/sensors?limit=3000')

params = urllib.parse.urlencode({'filter': 'status = down', 'limit': '3000'})
down_sensors = prtg_get(f'experimental/sensors?{params}')
params2 = urllib.parse.urlencode({'filter': 'status = warning', 'limit': '3000'})
warning_sensors = prtg_get(f'experimental/sensors?{params2}')

# Group problems by device
problem_sensors = down_sensors + warning_sensors
by_device = {}
for s in problem_sensors:
    parent = s.get('parent', {})
    dev_name = parent.get('name', 'Unknown')
    dev_id = parent.get('id', '?')
    key = (dev_name, dev_id)
    by_device.setdefault(key, []).append(s)

# Worst device for Act 3
worst_key = max(by_device, key=lambda k: len(by_device[k]))
worst_dev_name, worst_dev_id = worst_key
params = urllib.parse.urlencode({'filter': f'parentid = "{worst_dev_id}"', 'limit': '3000'})
worst_all_sensors = prtg_get(f'experimental/sensors?{params}')

# Data Exporter (has DOWN sensors)
de_dev_id = "8019"
params = urllib.parse.urlencode({'filter': f'parentid = "{de_dev_id}"', 'limit': '3000'})
de_all_sensors = prtg_get(f'experimental/sensors?{params}')

# Status counts
status_counts = {}
for s in sensors:
    st = s.get('status', 'UNKNOWN')
    status_counts[st] = status_counts.get(st, 0) + 1

dev_status_counts = {}
for d in devices:
    st = d.get('status', 'UNKNOWN')
    dev_status_counts[st] = dev_status_counts.get(st, 0) + 1

# Sensor kind breakdown
kind_counts = collections.Counter(s.get('kind_name', 'Unknown') for s in sensors)

# Device group breakdown
group_device_counts = collections.Counter(d.get('parent', {}).get('name', 'Unknown') for d in devices)

def normalize_status(raw):
    s = str(raw or 'UNKNOWN').upper()
    if s.startswith('SUMMED_INFO_'):
        s = s.replace('SUMMED_INFO_', '', 1)
    if 'DOWN' in s:
        return 'DOWN'
    if 'WARN' in s or 'UNUSUAL' in s:
        return 'WARNING'
    if 'PAUSED' in s:
        return 'PAUSED'
    if 'UP' in s:
        return 'UP'
    return 'OTHER'

# Visualization module data: Group status heatmap
group_status_counts = collections.defaultdict(collections.Counter)
for d in devices:
    gname = d.get('parent', {}).get('name', 'Unknown')
    group_status_counts[gname][normalize_status(d.get('status'))] += 1

top_heat_groups = sorted(
    group_status_counts.items(),
    key=lambda x: -(x[1].get('DOWN', 0) * 3 + x[1].get('WARNING', 0) * 2 + x[1].get('PAUSED', 0)),
)[:12]

# Visualization module data: Alert triage matrix (status x top sensor kinds)
kind_status_counts = collections.defaultdict(collections.Counter)
for s in sensors:
    kname = s.get('kind_name', 'Unknown')
    kind_status_counts[kname][normalize_status(s.get('status'))] += 1

top_matrix_kinds = sorted(
    kind_status_counts.items(),
    key=lambda x: -(x[1].get('DOWN', 0) * 3 + x[1].get('WARNING', 0) * 2 + x[1].get('PAUSED', 0)),
)[:12]

# =====================================================================
# FETCH TIMESERIES
# =====================================================================
print("Fetching timeseries data...")
chart_data = {}

# CPU Load on remote probe + reference server
for label, search in [
    ('Remote Probe (rp-amer) - CPU Load', lambda s: 'CPU' in s.get('kind_name','') and 'rp-amer' in s.get('parent',{}).get('name','')),
    ('Reference Server - CPU Load', lambda s: 'CPU' in s.get('kind_name','') and 'Reference Presales' in s.get('parent',{}).get('name','')),
]:
    found = [s for s in sensors if search(s) and s.get('status') == 'UP']
    if found:
        rows, ch = get_ts_named(found[0]['id'], 'medium')
        if rows:
            chs = [k for k in rows[0] if k != 'time'][:4]
            chart_data[label] = {'rows': [{'time': r['time'], **{c: r.get(c) for c in chs}} for r in rows[-200:]], 'channels': chs}
            print(f"  {label}: {len(chart_data[label]['rows'])} pts")

# Network traffic on Cisco switch
traffic = [s for s in sensors if s.get('kind_name') == 'SNMP Traffic' and s.get('status') == 'UP'
           and any(x in s.get('parent',{}).get('name','').lower() for x in ['cisco', 'forti', 'switch'])]
for s in traffic[:2]:
    label = f"{s.get('parent',{}).get('name','?')} - {s['name']}"
    rows, ch = get_ts_named(s['id'], 'medium')
    if rows:
        chs = [k for k in rows[0] if k != 'time' and 'Total' not in k][:2]  # In/Out
        if not chs:
            chs = [k for k in rows[0] if k != 'time'][:2]
        chart_data[label] = {'rows': [{'time': r['time'], **{c: r.get(c) for c in chs}} for r in rows[-200:]], 'channels': chs}
        print(f"  {label}: {len(chart_data[label]['rows'])} pts")

# Ping response times for key infra
ping_targets = {'Reference Server': '2639', 'Exchange': '6859', 'vCenter': '3178', 'Remote Probe': '9031'}
ping_combined_rows = []
ping_channels = []
for label, sid in ping_targets.items():
    rows, ch = get_ts_named(sid, 'medium')
    if rows:
        ping_ch = [k for k in rows[0] if k != 'time' and 'time' in k.lower()]
        if not ping_ch:
            ping_ch = [k for k in rows[0] if k != 'time'][:1]
        if ping_ch:
            # Rename channel to include device name
            renamed = label
            ping_channels.append(renamed)
            for r in rows[-200:]:
                # Find or create matching time slot
                existing = next((pr for pr in ping_combined_rows if pr['time'] == r['time']), None)
                if existing:
                    existing[renamed] = r.get(ping_ch[0])
                else:
                    ping_combined_rows.append({'time': r['time'], renamed: r.get(ping_ch[0])})
            print(f"  Ping {label}: OK")

if ping_combined_rows:
    ping_combined_rows.sort(key=lambda x: x['time'])
    chart_data['Infrastructure Ping Response Time (ms)'] = {'rows': ping_combined_rows[-200:], 'channels': ping_channels}

# Memory on Reference server
mem = [s for s in sensors if s.get('kind_name') == 'SNMP Memory' and 'Reference' in s.get('parent',{}).get('name','')]
if mem:
    rows, ch = get_ts_named(mem[0]['id'], 'medium')
    if rows:
        chs = [k for k in rows[0] if k != 'time' and 'Percent' in k][:1]
        if chs:
            chart_data['Reference Server - Memory Utilization (%)'] = {
                'rows': [{'time': r['time'], **{c: r.get(c) for c in chs}} for r in rows[-200:]],
                'channels': chs
            }
            print(f"  Memory: {len(rows)} pts")

# Disk on Reference server
disk = [s for s in sensors if 'Disk Free' in s.get('kind_name','') and 'Reference' in s.get('parent',{}).get('name','')]
if disk:
    rows, ch = get_ts_named(disk[0]['id'], 'medium')
    if rows:
        chs = [k for k in rows[0] if k != 'time' and 'Free' in k and 'Byte' not in k][:1]
        if not chs:
            chs = [k for k in rows[0] if k != 'time'][:1]
        if chs:
            chart_data['Reference Server - Disk Free (%)'] = {
                'rows': [{'time': r['time'], **{c: r.get(c) for c in chs}} for r in rows[-200:]],
                'channels': chs
            }
            print(f"  Disk: OK")

# SSL certificate expiry
print("Fetching SSL certificate expiry data...")
ssl_sensors = [s for s in sensors if 'SSL Certificate' in s.get('kind_name', '')]
ssl_expiry = []
for s in ssl_sensors:
    sid = s['id']
    try:
        ts = prtg_get(f'experimental/timeseries/{sid}/live')
        ch_params = urllib.parse.urlencode({'filter': f'parentid = "{sid}"', 'limit': '100'})
        channels = prtg_get(f'experimental/channels?{ch_params}')
        days_ch = next((c for c in channels if 'Days' in c['name'] and 'Expir' in c['name']), None)
        if days_ch and ts and len(ts) > 1:
            header = ts[0]
            last_row = ts[-1]
            ch_idx = next((i for i, h in enumerate(header) if str(days_ch['id']) == str(h)), None)
            if ch_idx is not None and isinstance(last_row, list):
                ssl_expiry.append({
                    'device': s.get('parent', {}).get('name', '?'),
                    'days': last_row[ch_idx],
                    'status': s.get('status', '?')
                })
    except:
        pass
ssl_expiry.sort(key=lambda x: x['days'] if x['days'] is not None else 9999)
print(f"  {len(ssl_expiry)} certs found")

print(f"Total chart series: {len(chart_data)}")

# =====================================================================
# SHARED CSS
# =====================================================================
SPECTRUM_CSS = """
:root {
  --font: Roboto, "Segoe UI", Tahoma, Arial, Helvetica, Verdana, sans-serif;
  --mono: inconsolata, monospace;
  --brand: #050F34; --base: #31343F; --alt: #686B76; --disabled: #A4A6AF;
  --accent: #0F67FF; --danger: #E3063D; --warning-text: #A04B00; --success-text: #697000;
  --bg-body: #F9F9FA; --bg-card: #FFFFFF; --bg-alt: #F9F9FA; --bg-alt2: #F1F1F3; --bg-alt3: #E5E6E9;
  --bg-accent: #0F67FF; --bg-danger-soft: #FFF6F8; --bg-warning-soft: #FFF8F3; --bg-success-soft: #FDFFEB;
  --border: #DBDCDF; --border2: #E5E6E9; --border3: #F1F1F3;
  --fill-danger: #E3063D; --fill-warning: #DE6800; --fill-success: #8F9900;
  --shadow: 0 1px 3px rgba(0,0,0,.08), 0 1px 2px rgba(0,0,0,.06);
  --shadow2: 0 4px 12px rgba(0,0,0,.1), 0 2px 4px rgba(0,0,0,.06);
  --r: 4px; --rl: 8px;
  --c1: #0F67FF; --c2: #A4AD19; --c3: #DE6800; --c4: #0097B2; --c5: #8A3FFC; --c6: #D12771;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--font);font-size:14px;line-height:20px;color:var(--base);background:var(--bg-body)}
h1{font-size:26px;line-height:32px;color:var(--brand);font-weight:700;margin:0 0 4px}
h2{font-size:20px;line-height:28px;color:var(--brand);font-weight:700;margin:24px 0 12px}
h3{font-size:16px;line-height:24px;color:var(--brand);font-weight:500;margin:16px 0 8px}
a{color:var(--accent);text-decoration:none} a:hover{text-decoration:underline}
code{font-family:var(--mono);background:var(--bg-alt2);padding:2px 6px;border-radius:3px;font-size:13px}
.container{max-width:1280px;margin:0 auto;padding:24px}
table{border-collapse:collapse;width:100%;margin:8px 0}
th,td{padding:8px 12px;text-align:left;border-bottom:1px solid var(--border2);font-size:13px}
th{background:var(--bg-alt2);font-weight:500;color:var(--brand);position:sticky;top:0}
tr:hover{background:var(--bg-alt)}
.card{background:var(--bg-card);border-radius:var(--rl);box-shadow:var(--shadow);padding:20px;margin:12px 0}
.badge{display:inline-block;padding:2px 10px;border-radius:12px;font-size:12px;font-weight:500}
.b-up{background:var(--bg-success-soft);color:var(--fill-success)}
.b-down{background:var(--bg-danger-soft);color:var(--fill-danger)}
.b-warn{background:var(--bg-warning-soft);color:var(--fill-warning)}
.b-other{background:var(--bg-alt2);color:var(--disabled)}
.prompt-box{background:#1D202B;color:#E5E6E9;padding:16px 20px;border-radius:var(--rl);font-family:var(--mono);font-size:13px;margin:12px 0;white-space:pre-wrap;line-height:1.5}
.prompt-box .pfx{color:#74ABFF}
.kpi-row{display:flex;gap:16px;flex-wrap:wrap;margin:16px 0}
.kpi{background:var(--bg-card);border-radius:var(--rl);box-shadow:var(--shadow);padding:16px 24px;text-align:center;min-width:100px;flex:1}
.kpi .num{font-size:32px;font-weight:700;color:var(--brand)} .kpi .lbl{font-size:12px;color:var(--alt);margin-top:2px}
.chart-card{background:var(--bg-card);border-radius:var(--rl);box-shadow:var(--shadow);padding:16px;margin:12px 0}
.chart-card h3{margin:0 0 8px;font-size:14px}
.chart-wrap{position:relative;height:220px}
.nav{display:flex;gap:8px;margin:12px 0;flex-wrap:wrap}
.nav a{padding:6px 14px;background:var(--bg-card);border-radius:var(--r);box-shadow:var(--shadow);font-size:13px}
.nav a:hover{background:var(--bg-alt)}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:16px} @media(max-width:900px){.grid-2{grid-template-columns:1fr}}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px} @media(max-width:1000px){.grid-3{grid-template-columns:1fr 1fr}} @media(max-width:600px){.grid-3{grid-template-columns:1fr}}
.act{border-left:4px solid var(--bg-accent);padding-left:20px;margin:32px 0}
.act-hdr{display:flex;align-items:center;gap:12px}
.act-n{background:var(--bg-accent);color:white;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;flex-shrink:0}
.note{background:var(--bg-alt);border-radius:var(--r);padding:10px 14px;margin:8px 0;font-size:13px;color:var(--alt);border-left:3px solid var(--border)}
.sim{background:#FFFCF3;border-left:3px solid var(--fill-warning);padding:10px 14px;border-radius:var(--r);margin:8px 0;font-size:13px}
.timestamp{color:var(--alt);font-size:12px}
.ssl-bar{display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid var(--border3)}
.ssl-bar:last-child{border:none}
.ssl-fill{height:16px;border-radius:3px;min-width:2px}
.ssl-label{font-size:12px;min-width:180px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ssl-days{font-size:12px;font-weight:500;min-width:60px;text-align:right}
.health-ring{position:relative;width:160px;height:160px;margin:0 auto}
.viz-note{font-size:12px;color:var(--alt);margin-bottom:8px}
.heatmap-table td,.heatmap-table th{font-size:12px}
.heat-cell{font-weight:600;text-align:center;border-radius:3px;padding:4px 8px;display:inline-block;min-width:34px}
.matrix-table td,.matrix-table th{font-size:12px}
.brand-header{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:8px}
.brand-lockup{display:flex;align-items:center;gap:12px}
.brand-mark{width:44px;height:44px;display:block}
.brand-copy h1{margin:0}
.brand-copy .timestamp{margin-top:2px;display:block}
.brand-meta{display:flex;align-items:center;gap:10px}
@media(max-width:700px){.brand-mark{width:40px;height:40px}}
"""

def badge(status):
    s = status.upper()
    if 'DOWN' in s: return f'<span class="badge b-down">{E(status)}</span>'
    if 'WARNING' in s or 'UNUSUAL' in s: return f'<span class="badge b-warn">{E(status)}</span>'
    if 'UP' in s: return f'<span class="badge b-up">{E(status)}</span>'
    return f'<span class="badge b-other">{E(status)}</span>'

sorted_devs = sorted(by_device.items(), key=lambda x: -len(x[1]))

# =====================================================================
# WALKTHROUGH (index.html) — keep mostly the same but link to new dashboard
# =====================================================================
print(f"Generating {OUT_DIR}/index.html...")

wt = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>PRTG Skill Demo Walkthrough</title><style>{SPECTRUM_CSS}</style></head><body><div class="container">
<div class="brand-header">
  <div class="brand-lockup">
    {PRTG_LOGO_SVG}
    <div class="brand-copy">
      <h1>PRTG Skill Demo &mdash; Full Walkthrough</h1>
      <span class="timestamp">{E(HOST)} &bull; Snapshot: {NOW}</span>
    </div>
  </div>
  <div class="brand-meta"><a href="dashboard.html">Open Dashboard &rarr;</a></div>
</div>
<p style="margin:8px 0">Output from all 8 acts of the PRTG Skill demo against the live PRTG instance.</p>
<div class="nav">
  <a href="#summary">Summary</a><a href="#act1">1: Orientation</a><a href="#act2">2: Triage</a>
  <a href="#act3">3: Investigation</a><a href="#act4">4: Actions</a><a href="#act5">5: Provisioning</a>
  <a href="#act6">6: Dashboard</a><a href="#act7">7: Charts</a><a href="#act8">8: Cleanup</a>
  <a href="dashboard.html" style="background:var(--bg-accent);color:white">Live Dashboard &rarr;</a>
</div>

<div id="summary" class="card">
<h2 style="margin-top:0">Demo Script Summary</h2>
<p>An 8-act scripted walkthrough of the PRTG skill for Claude Code. Each act is one natural-language prompt.</p>
<h3>Prerequisites</h3>
<ul style="margin:8px 0 8px 24px;font-size:13px">
  <li>PRTG skill installed at <code>~/.claude/skills/prtg</code></li>
  <li><code>prtg.env</code> with PRTG_HOST and PRTG_API_KEY</li>
  <li>PRTG instance with devices in DOWN/WARNING state for interesting triage</li>
</ul>
<table><tr><th>Act</th><th>Title</th><th>Capability Shown</th></tr>
<tr><td>1</td><td>Orientation</td><td>Multi-endpoint aggregation &rarr; infrastructure overview</td></tr>
<tr><td>2</td><td>Triage</td><td>Filtered queries + grouping &rarr; find all problems</td></tr>
<tr><td>3</td><td>Investigation</td><td>Multi-step analysis &rarr; deep dive with timeseries</td></tr>
<tr><td>4</td><td>Take Action</td><td>Write operations &rarr; acknowledge + pause</td></tr>
<tr><td>5</td><td>Provisioning</td><td>POST + create &rarr; add sensors on the fly</td></tr>
<tr><td>6</td><td>Dashboard</td><td>HTML generation with Spectrum design tokens</td></tr>
<tr><td>7</td><td>Charts</td><td>Chart.js + channel name mapping</td></tr>
<tr><td>8</td><td>Cleanup</td><td>Delete + resume &rarr; full lifecycle</td></tr>
</table></div>

<div id="act1" class="act"><div class="act-hdr"><div class="act-n">1</div><h2>Orientation</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Give me a high-level overview of this PRTG installation. Summarize the health.</div>
<div class="note">Queries probes, groups, devices (with sensor_status_summary), and sensors in parallel.</div>
<div class="kpi-row">
  <div class="kpi"><div class="num">{len(probes)}</div><div class="lbl">Probes</div></div>
  <div class="kpi"><div class="num">{len(groups)}</div><div class="lbl">Groups</div></div>
  <div class="kpi"><div class="num">{len(devices)}</div><div class="lbl">Devices</div></div>
  <div class="kpi"><div class="num">{len(sensors)}</div><div class="lbl">Sensors</div></div>
</div>
<div class="grid-2"><div class="card"><h3>Sensor Health</h3><table><tr><th>Status</th><th>Count</th><th>%</th></tr>
"""
for st, ct in sorted(status_counts.items(), key=lambda x: -x[1]):
    wt += f"<tr><td>{badge(st)}</td><td>{ct}</td><td>{ct/len(sensors)*100:.1f}%</td></tr>\n"
wt += f"""</table></div><div class="card"><h3>Device Status</h3><table><tr><th>Status</th><th>Count</th></tr>
"""
for st, ct in sorted(dev_status_counts.items(), key=lambda x: -x[1]):
    wt += f"<tr><td>{badge(st)}</td><td>{ct}</td></tr>\n"
wt += "</table></div></div></div>\n"

# Act 2
wt += f"""<div id="act2" class="act"><div class="act-hdr"><div class="act-n">2</div><h2>Triage</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Show me everything down or warning. Group by device.</div>
<div class="note">Filters by status=down and status=warning, groups by parent device.</div>
<div class="kpi-row">
  <div class="kpi"><div class="num" style="color:var(--fill-danger)">{len(down_sensors)}</div><div class="lbl">DOWN</div></div>
  <div class="kpi"><div class="num" style="color:var(--fill-warning)">{len(warning_sensors)}</div><div class="lbl">WARNING</div></div>
  <div class="kpi"><div class="num">{len(by_device)}</div><div class="lbl">Affected Devices</div></div>
</div>
<table><tr><th>Device</th><th>ID</th><th>#</th><th>Sensors</th></tr>
"""
for (dn, did), slist in sorted_devs[:15]:
    sl = ', '.join(E(s['name']) for s in slist[:3])
    if len(slist) > 3: sl += f' <em>(+{len(slist)-3})</em>'
    wt += f"<tr><td><strong>{E(dn)}</strong></td><td>{E(did)}</td><td>{len(slist)}</td><td>{sl}</td></tr>\n"
rem = len(sorted_devs) - 15
if rem > 0:
    wt += f'<tr><td colspan="4" style="color:var(--alt);font-style:italic">+{rem} more devices</td></tr>\n'
wt += "</table></div>\n"

# Act 3
wt += f"""<div id="act3" class="act"><div class="act-hdr"><div class="act-n">3</div><h2>Investigation</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Deep dive on the worst device. All sensors, status timestamps, timeseries for anything down.</div>
<div class="note">Identifies worst device, queries all sensors via parentid, fetches status_since and timeseries.</div>
<h3>{E(worst_dev_name)} (ID: {E(worst_dev_id)}) &mdash; {len(by_device[worst_key])} problems</h3>
<table><tr><th>Sensor</th><th>Status</th><th>Since</th></tr>
"""
for s in worst_all_sensors:
    since = (s.get('status_since') or 'N/A').replace('T', ' ').replace('Z', ' UTC')
    wt += f"<tr><td>{E(s['name'])}</td><td>{badge(s.get('status','?'))}</td><td class='timestamp'>{E(since)}</td></tr>\n"
wt += f"""</table>
<h3>PRTG Data Exporter (ID: 8019) &mdash; 2 DOWN services</h3>
<table><tr><th>Sensor</th><th>Status</th><th>Since</th></tr>
"""
for s in de_all_sensors:
    since = (s.get('status_since') or 'N/A').replace('T', ' ').replace('Z', ' UTC')
    wt += f"<tr><td>{E(s['name'])}</td><td>{badge(s.get('status','?'))}</td><td class='timestamp'>{E(since)}</td></tr>\n"
wt += "</table></div>\n"

# Act 4
wt += """<div id="act4" class="act"><div class="act-hdr"><div class="act-n">4</div><h2>Take Action</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Acknowledge all down sensors with "Investigating - INC-4521". Pause the device.</div>
<div class="sim"><strong>Simulated</strong> (shared demo server). Claude would call:
<code>POST /sensors/{id}/acknowledge</code> for each DOWN sensor, then <code>POST /devices/8019/pause</code>.</div></div>
"""

# Act 5
wt += f"""<div id="act5" class="act"><div class="act-hdr"><div class="act-n">5</div><h2>Provisioning</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Add a Ping sensor called "Uptime Watchdog" to a healthy device. Trigger a scan.</div>
<div class="sim"><strong>Simulated.</strong> Claude would <code>POST /experimental/devices/{{id}}/sensor?kindid=ping</code> then <code>POST /sensors/{{id}}/scan</code>.</div></div>
"""

# Act 6
wt += f"""<div id="act6" class="act"><div class="act-hdr"><div class="act-n">6</div><h2>Dashboard</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Build a Spectrum-themed dashboard with health overview, SSL expiry, key metrics, and problem list.</div>
<div class="card" style="text-align:center;padding:20px">
  <p>Generated with live data from {len(devices)} devices and {len(sensors)} sensors.</p>
  <a href="dashboard.html" style="display:inline-block;padding:10px 28px;background:var(--bg-accent);color:white;border-radius:var(--rl);font-weight:500;margin-top:8px;text-decoration:none">Open Dashboard &rarr;</a>
</div></div>
"""

# Act 7
wt += """<div id="act7" class="act"><div class="act-hdr"><div class="act-n">7</div><h2>Charts</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Add timeseries charts: CPU, memory, network traffic, ping latency. Spectrum colors.</div>
<div class="card" style="text-align:center;padding:20px">
  <p>Chart.js charts with 30-day trends are embedded in the dashboard.</p>
  <a href="dashboard.html#charts" style="display:inline-block;padding:10px 28px;background:var(--bg-accent);color:white;border-radius:var(--rl);font-weight:500;margin-top:8px;text-decoration:none">View Charts &rarr;</a>
</div></div>
"""

# Act 8
wt += """<div id="act8" class="act"><div class="act-hdr"><div class="act-n">8</div><h2>Cleanup</h2></div>
<div class="prompt-box"><span class="pfx">&gt; </span>/prtg Resume the paused device. Delete the test sensor.</div>
<div class="sim"><strong>Simulated.</strong> <code>POST /devices/{id}/resume</code> + <code>DELETE /experimental/sensors/{id}</code>.</div></div>
"""

# Recap
wt += """<div class="card" style="margin-top:32px"><h2 style="margin-top:0">Recap</h2>
<table><tr><th>Act</th><th>What</th><th>Capability</th></tr>
<tr><td>1</td><td>Infrastructure overview</td><td>Multi-endpoint aggregation</td></tr>
<tr><td>2</td><td>Triage all problems</td><td>Filtered queries + grouping</td></tr>
<tr><td>3</td><td>Deep investigation</td><td>Multi-step analysis + context carryover</td></tr>
<tr><td>4</td><td>Acknowledge + pause</td><td>Write operations</td></tr>
<tr><td>5</td><td>Create sensor</td><td>Provisioning</td></tr>
<tr><td>6</td><td>Status dashboard</td><td>HTML + Spectrum design system</td></tr>
<tr><td>7</td><td>Timeseries charts</td><td>Chart.js + channel mapping</td></tr>
<tr><td>8</td><td>Cleanup</td><td>Full CRUD lifecycle</td></tr>
</table>
<p style="margin-top:8px"><strong>8 prompts &bull; ~10 minutes &bull;</strong> Replaces hours of UI clicks and custom dashboard development.</p>
</div></div></body></html>"""

with open(os.path.join(OUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(wt)
print(f"  -> {OUT_DIR}/index.html")

# =====================================================================
# DASHBOARD (dashboard.html) — redesigned
# =====================================================================
print(f"Generating {OUT_DIR}/dashboard.html...")

# Prepare chart JSON
chart_json = json.dumps(chart_data, default=str)

# Prepare SSL data
ssl_json = json.dumps(ssl_expiry, default=str)

# Health donut data
up_pct = status_counts.get('UP', 0) / len(sensors) * 100
down_pct = status_counts.get('DOWN', 0) / len(sensors) * 100
warn_pct = status_counts.get('WARNING', 0) / len(sensors) * 100
other_pct = 100 - up_pct - down_pct - warn_pct

# Sensor kind top 10
top_kinds = kind_counts.most_common(10)
kind_json = json.dumps([{'kind': k, 'count': c} for k, c in top_kinds])

# Group breakdown top 10
top_groups = group_device_counts.most_common(10)
group_json = json.dumps([{'group': g, 'count': c} for g, c in top_groups])

def rgba(r, g, b, alpha):
    return f"rgba({r},{g},{b},{alpha:.2f})"

# Heatmap table HTML
heatmap_rows_html = ""
for gname, counts in top_heat_groups:
    total = sum(counts.values()) or 1
    down = counts.get('DOWN', 0)
    warn = counts.get('WARNING', 0)
    paused = counts.get('PAUSED', 0)
    up = counts.get('UP', 0)
    other = counts.get('OTHER', 0)
    heatmap_rows_html += (
        "<tr>"
        f"<td><strong>{E(gname)}</strong></td>"
        f"<td><span class='heat-cell' style='background:{rgba(227,6,61,0.12 + 0.62*(down/total))};color:#7A001E'>{down}</span></td>"
        f"<td><span class='heat-cell' style='background:{rgba(222,104,0,0.12 + 0.62*(warn/total))};color:#6A3500'>{warn}</span></td>"
        f"<td><span class='heat-cell' style='background:{rgba(164,166,175,0.12 + 0.62*(paused/total))};color:#4D4F59'>{paused}</span></td>"
        f"<td><span class='heat-cell' style='background:{rgba(143,153,0,0.12 + 0.62*(up/total))};color:#495000'>{up}</span></td>"
        f"<td>{other}</td>"
        f"<td><strong>{total}</strong></td>"
        "</tr>"
    )

# Triage matrix HTML
matrix_cols = ['DOWN', 'WARNING', 'PAUSED', 'UP']
col_max = {col: max((c.get(col, 0) for _, c in top_matrix_kinds), default=0) for col in matrix_cols}
matrix_rows_html = ""
for kname, counts in top_matrix_kinds:
    total = sum(counts.values())
    cells = []
    for col in matrix_cols:
        val = counts.get(col, 0)
        denom = col_max[col] or 1
        strength = val / denom
        if col == 'DOWN':
            bg = rgba(227, 6, 61, 0.08 + 0.67 * strength)
            fg = '#7A001E'
        elif col == 'WARNING':
            bg = rgba(222, 104, 0, 0.08 + 0.67 * strength)
            fg = '#6A3500'
        elif col == 'PAUSED':
            bg = rgba(164, 166, 175, 0.08 + 0.67 * strength)
            fg = '#4D4F59'
        else:
            bg = rgba(143, 153, 0, 0.08 + 0.67 * strength)
            fg = '#495000'
        cells.append(f"<td><span class='heat-cell' style='background:{bg};color:{fg}'>{val}</span></td>")
    matrix_rows_html += f"<tr><td><strong>{E(kname)}</strong></td>{''.join(cells)}<td><strong>{total}</strong></td></tr>"

dash = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>PRTG Infrastructure Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3"></script>
<style>{SPECTRUM_CSS}
.section{{margin:32px 0}}
</style></head><body><div class="container">

<div class="brand-header">
  <div class="brand-lockup">
    {PRTG_LOGO_SVG}
    <div class="brand-copy">
      <h1>PRTG Infrastructure Dashboard</h1>
      <span class="timestamp">Snapshot: {NOW} &bull; {E(HOST)}</span>
    </div>
  </div>
  <div class="brand-meta"><a href="index.html">&larr; Demo Walkthrough</a></div>
</div>

<!-- KPIs -->
<div class="kpi-row">
  <div class="kpi"><div class="num">{len(probes)}</div><div class="lbl">Probes</div></div>
  <div class="kpi"><div class="num">{len(groups)}</div><div class="lbl">Groups</div></div>
  <div class="kpi"><div class="num">{len(devices)}</div><div class="lbl">Devices</div></div>
  <div class="kpi"><div class="num">{len(sensors)}</div><div class="lbl">Sensors</div></div>
  <div class="kpi"><div class="num" style="color:var(--fill-success)">{up_pct:.1f}%</div><div class="lbl">Healthy</div></div>
  <div class="kpi"><div class="num" style="color:var(--fill-danger)">{status_counts.get('DOWN',0)}</div><div class="lbl">DOWN</div></div>
  <div class="kpi"><div class="num" style="color:var(--fill-warning)">{status_counts.get('WARNING',0)}</div><div class="lbl">WARNING</div></div>
</div>

<!-- Row: Health donut + Sensor types + Device groups -->
<div class="grid-3">
  <div class="chart-card"><h3>Sensor Health</h3><div class="chart-wrap" style="height:200px"><canvas id="healthDonut"></canvas></div></div>
  <div class="chart-card"><h3>Top Sensor Types</h3><div class="chart-wrap" style="height:200px"><canvas id="kindChart"></canvas></div></div>
  <div class="chart-card"><h3>Devices by Group</h3><div class="chart-wrap" style="height:200px"><canvas id="groupChart"></canvas></div></div>
</div>

<!-- Visualization Module: Group Status Heatmap -->
<div class="section">
<h2>Group Status Heatmap</h2>
<p class="viz-note">Data source: API v2 (`/experimental/devices?include=sensor_status_summary`). API v1 fallback helper is available but not used for this module.</p>
<div class="card" style="max-height:420px;overflow-y:auto">
<table class="heatmap-table"><tr><th>Group</th><th>DOWN</th><th>WARNING</th><th>PAUSED</th><th>UP</th><th>Other</th><th>Total Devices</th></tr>
{heatmap_rows_html}
</table>
</div>
</div>

<!-- Visualization Module: Alert Triage Matrix -->
<div class="section">
<h2>Alert Triage Matrix (Status x Sensor Type)</h2>
<p class="viz-note">Data source: API v2 (`/experimental/sensors`). Colors are intensity-scaled per status column for quick triage.</p>
<div class="card" style="max-height:420px;overflow-y:auto">
<table class="matrix-table"><tr><th>Sensor Type</th><th>DOWN</th><th>WARNING</th><th>PAUSED</th><th>UP</th><th>Total</th></tr>
{matrix_rows_html}
</table>
</div>
</div>

<!-- SSL Certificate Expiry -->
<div class="section">
<h2>SSL Certificate Expiry Timeline</h2>
<p class="timestamp" style="margin-bottom:8px">Sorted by days until expiration. Red = expired or expiring within 30 days. Orange = within 180 days.</p>
<div class="card" id="sslContainer" style="max-height:400px;overflow-y:auto"></div>
</div>

<!-- Timeseries Charts -->
<div class="section" id="charts">
<h2>Infrastructure Trends (30 Days)</h2>
<p class="timestamp" style="margin-bottom:8px">CPU utilization, network traffic, ping latency, memory, and disk usage across key infrastructure.</p>
<div class="grid-2" id="chartGrid"></div>
</div>

<!-- Problem List -->
<div class="section">
<h2>Active Problems ({len(down_sensors)} DOWN, {len(warning_sensors)} WARNING)</h2>
<div class="card" style="max-height:500px;overflow-y:auto">
<table><tr><th>Device</th><th>Sensor</th><th>Type</th><th>Status</th></tr>
"""

# DOWN first, then WARNING
all_problems = sorted(problem_sensors, key=lambda s: (0 if s.get('status') == 'DOWN' else 1, s.get('parent',{}).get('name','')))
for s in all_problems:
    dash += f"<tr><td>{E(s.get('parent',{}).get('name','?'))}</td><td>{E(s['name'])}</td><td style='color:var(--alt);font-size:12px'>{E(s.get('kind_name',''))}</td><td>{badge(s.get('status','?'))}</td></tr>\n"

dash += f"""</table></div></div>

</div><!-- container -->

<script>
const COLORS = ['#0F67FF','#A4AD19','#DE6800','#0097B2','#8A3FFC','#D12771','#F2174D','#76D8D6','#B4BF17','#DF399D'];

// Health donut
new Chart(document.getElementById('healthDonut'), {{
  type: 'doughnut',
  data: {{
    labels: ['UP','DOWN','WARNING','Other'],
    datasets: [{{ data: [{status_counts.get('UP',0)},{status_counts.get('DOWN',0)},{status_counts.get('WARNING',0)},{len(sensors)-status_counts.get('UP',0)-status_counts.get('DOWN',0)-status_counts.get('WARNING',0)}],
      backgroundColor: ['#8F9900','#E3063D','#DE6800','#DBDCDF'], borderWidth: 0 }}]
  }},
  options: {{responsive:true, maintainAspectRatio:false, cutout:'65%',
    plugins: {{legend:{{position:'bottom',labels:{{font:{{size:11}},usePointStyle:true,pointStyle:'circle'}}}}}}
  }}
}});

// Sensor types bar
const kinds = {kind_json};
new Chart(document.getElementById('kindChart'), {{
  type: 'bar',
  data: {{ labels: kinds.map(k=>k.kind), datasets: [{{ data: kinds.map(k=>k.count), backgroundColor: '#0F67FF40', borderColor: '#0F67FF', borderWidth: 1 }}] }},
  options: {{responsive:true, maintainAspectRatio:false, indexAxis:'y',
    scales: {{x:{{grid:{{color:'#F1F1F3'}}}}, y:{{ticks:{{font:{{size:10}}}}}}}},
    plugins: {{legend:{{display:false}}}}
  }}
}});

// Device groups bar
const groups = {group_json};
new Chart(document.getElementById('groupChart'), {{
  type: 'bar',
  data: {{ labels: groups.map(g=>g.group), datasets: [{{ data: groups.map(g=>g.count), backgroundColor: '#0097B240', borderColor: '#0097B2', borderWidth: 1 }}] }},
  options: {{responsive:true, maintainAspectRatio:false, indexAxis:'y',
    scales: {{x:{{grid:{{color:'#F1F1F3'}}}}, y:{{ticks:{{font:{{size:10}}}}}}}},
    plugins: {{legend:{{display:false}}}}
  }}
}});

// SSL Expiry
const sslData = {ssl_json};
const sslContainer = document.getElementById('sslContainer');
const maxDays = Math.max(...sslData.filter(e=>e.days>0).map(e=>e.days), 365);
sslData.forEach(e => {{
  const d = e.days;
  let color = '#8F9900'; // green
  if (d < 0) color = '#E3063D';
  else if (d < 30) color = '#E3063D';
  else if (d < 180) color = '#DE6800';
  const width = Math.max(Math.min(Math.abs(d) / maxDays * 100, 100), 1);
  const label = d < 0 ? `Expired ${{Math.abs(Math.round(d))}}d ago` : `${{Math.round(d)}} days`;
  sslContainer.innerHTML += `<div class="ssl-bar">
    <div class="ssl-label" title="${{e.device}}">${{e.device}}</div>
    <div style="flex:1;background:#F1F1F3;border-radius:3px;overflow:hidden">
      <div class="ssl-fill" style="width:${{width}}%;background:${{color}}"></div>
    </div>
    <div class="ssl-days" style="color:${{color}}">${{label}}</div>
  </div>`;
}});

// Timeseries charts
const tsData = {chart_json};
const chartGrid = document.getElementById('chartGrid');
Object.entries(tsData).forEach(([title, data], idx) => {{
  const div = document.createElement('div');
  div.className = 'chart-card';
  div.innerHTML = `<h3>${{title}}</h3><div class="chart-wrap"><canvas id="ts${{idx}}"></canvas></div>`;
  chartGrid.appendChild(div);

  const datasets = [];
  data.channels.forEach((ch, ci) => {{
    datasets.push({{
      label: ch,
      data: data.rows.map(r => ({{ x: new Date(r.time), y: r[ch] }})).filter(p => p.y !== undefined && p.y !== null),
      borderColor: COLORS[ci % COLORS.length],
      backgroundColor: COLORS[ci % COLORS.length] + '15',
      borderWidth: 1.5, pointRadius: 0, tension: 0.3, fill: true
    }});
  }});

  requestAnimationFrame(() => {{
    new Chart(document.getElementById('ts' + idx), {{
      type: 'line', data: {{ datasets }},
      options: {{
        responsive:true, maintainAspectRatio:false,
        interaction: {{mode:'index',intersect:false}},
        scales: {{
          x: {{type:'time', grid:{{color:'#F1F1F3'}}, ticks:{{font:{{size:10}}}}}},
          y: {{grid:{{color:'#F1F1F3'}}, ticks:{{font:{{size:10}}}}, beginAtZero:false}}
        }},
        plugins: {{legend:{{position:'bottom',labels:{{font:{{size:11}},usePointStyle:true,pointStyle:'line'}}}}}}
      }}
    }});
  }});
}});
</script></body></html>"""

with open(os.path.join(OUT_DIR, 'dashboard.html'), 'w', encoding='utf-8') as f:
    f.write(dash)
print(f"  -> {OUT_DIR}/dashboard.html")

# Cleanup temp files
for f in [os.path.join(OUT_DIR, '_chart_data.json'), os.path.join(OUT_DIR, '_ssl_data.json')]:
    if os.path.exists(f):
        os.remove(f)

print(f"\nDone! Open {OUT_DIR}/index.html or {OUT_DIR}/dashboard.html in a browser.")
