# Spectrum Visualization Guidelines

Use this file as the implementation rulebook for all generated PRTG visualizations.

## 1) Choose The Right Design System

Use `spectrum-design-system.md` (compact) when:
- The output is mostly static HTML.
- You need quick delivery with token-level styling only.
- The page is KPI/cards/tables/charts without complex interaction.

Use `spectrum-full-system.md` when:
- The output includes reusable components with multiple states.
- You need richer interactions (menus, sheets, toasts, contextual actions, focus states).
- You need stricter parity with full Spectrum component behavior.

If a page mixes both:
- Use full-system rules for interactive components.
- Use compact tokens for static sections.

## 2) Mandatory Branding

Every visualization MUST include a top header with:
- PRTG logo at top-left.
- Visualization title.
- Snapshot timestamp.

Logo implementation options (in order):
1. Local official logo asset if available in the workspace.
2. Inline SVG lockup containing a PRTG wordmark and brand-colored mark.
3. Text fallback only when SVG/image is unavailable.

Accessibility requirements:
- `img` logos need meaningful `alt` text (`"PRTG"` or `"PRTG Network Monitor"`).
- Inline SVG should include `role="img"` and `aria-label="PRTG"`.

## 3) Visual Quality Baseline

All visualizations should feel intentional, not default/boilerplate:
- Use clear information hierarchy:
  - Header and context
  - KPI summary
  - Main visuals
  - Detailed tables/lists
- Use consistent spacing rhythm (4px multiples).
- Prefer semantic status coloring (UP/DOWN/WARNING/PAUSED) via Spectrum tokens.
- Keep chart gridlines and labels subtle; make data series the visual focus.
- Use card surfaces, border radius, and elevation consistently.

## 4) Visualization Types (Recommended)

Good default output types:
- Status dashboard
- Timeseries trend report
- Sensor-type distribution view
- Device-group health comparison
- SSL/SLA timeline view
- Topology-style service dependency overview (if graph links are available)

## 5) Output Checklist

Before finalizing generated HTML:
- PRTG logo is present in the top header.
- Snapshot time and source context are shown.
- Spectrum tokens are used (avoid ad-hoc color values except chart palette accents).
- Status semantics are consistent.
- Page is readable on desktop and mobile breakpoints.
