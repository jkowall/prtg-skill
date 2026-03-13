# Design System Knowledge Base

> This file is the single source of truth for our design system patterns.
> It is maintained by Claude Code during analysis and used as reference during restructuring.
> DO NOT edit manually unless correcting an error.

## Global Tokens

### Colors

> The design system uses **light** (default) and **dark** themes. CSS variables resolve to different values per theme.

#### Text Colors

| Token Name | Light | Dark | Usage |
|---|---|---|---|
| `--text/base` | `#31343f` | `#e5e6e9` | Primary text, active/current items, menu item labels, contextual menu item text, empty state title & subtitle, banner message text. **Variable ID confirmed: `VariableID:23337:93155`** |
| `--text/alt` | `#686b76` | `#babcc2` | Secondary/muted text, default items, menu group headings, contextual menu icon default color. **Variable ID confirmed: `VariableID:23879:2979`** |
| `--text/accent` | `#0f67ff` | *TBD* | Interactive/link text, hover state, contextual menu selected item text/icon/border, banner inline link text. **Variable ID confirmed: `VariableID:23879:2981`** |
| `--text/overlay` | `#ffffff` | `#ffffff` | Text/icons on colored backgrounds (FAB icon, primary button text). **Theme-invariant. Variable ID confirmed: `VariableID:23879:2987`** |
| `--text/brand` | `#050f34` | *TBD* | Brand-specific text |

#### Background Colors

| Token Name | Light | Dark | Usage |
|---|---|---|---|
| `--background/base` | `#ffffff` | `#252937` | Base surface background, menu/popover background, contextual menu container, CTA bar container, sheet container. **Variable ID confirmed: `VariableID:23879:3177`** |
| `--background/body` | `#f9f9fa` | `#1d202b` | Page/body background, showcase containers, footer background, **Alert Secondary fill**. **Variable ID confirmed: `VariableID:23879:3178`** |
| `--background/alt7` | `#3f414b` | *TBD* | Dark background for tags/badges |
| `--background/accentsoft` | `#f5f9ff` | *TBD* | Soft accent background, Toast Primary fill, **Banner Information fill**, **Alert Primary fill**. **Variable ID confirmed: `VariableID:23879:3187`** |
| `--background/accent` | `#0f67ff` | `#0f67ff`* | Primary accent, FAB default state, checkbox selected fill, primary button fill (enabled). *Likely theme-invariant. **Variable ID confirmed: `VariableID:23879:3183`** |
| `--background/accentalt` | `#065aec` | *TBD* | Darker accent, FAB hover & focus states, checkbox hover-selected & hover-indeterminate fill. **Variable ID confirmed: `VariableID:23879:3184`** |
| `--background/accentalt2` | `#024ed3` | `#024ed3`* | Darkest accent, FAB pressed state. *Confirmed same in dark. **Variable ID confirmed: `VariableID:23879:3185`** |
| `--background/hover` | `#f1f1f3` | *TBD* | Hover/focus background for interactive elements (checkbox hover & focus, contextual menu hover & focus, secondary button fill, empty state illustration circle). **Variable ID confirmed: `VariableID:23879:3179`**. Note: Disabled checkbox uses a **different variable** (`23879:3182`) with same hex — will likely diverge in dark theme |
| `--background/pressed` | `#e5e6e9` | *TBD* | Pressed/active background for interactive elements (contextual menu pressed state). **Variable ID confirmed: `VariableID:23879:3180`** — separate variable from `--border/alt2` (`23880:1100`) despite same hex in light theme |
| `--background/success` *(tentative)* | `#fdffeb` | *TBD* | Toast Success fill, **Alert Success fill**. **Variable ID: `VariableID:23879:3198`** |
| `--background/error` *(tentative)* | `#fff6f8` | *TBD* | Toast Error fill, **Banner Error fill**, **Alert Error fill**. **Variable ID: `VariableID:23879:3193`** |
| `--background/warning` *(tentative)* | `#fff8f3` | *TBD* | Toast Warning fill, **Banner Warning fill**, **Alert Warning fill**. **Variable ID: `VariableID:23879:3196`** |

#### Border Colors

| Token Name | Light | Dark | Usage |
|---|---|---|---|
| `--border/alt` | `#dbdcdf` | `#686b76` | Default border color, container outlines, **Alert Secondary outer border**. **Variable ID confirmed: `VariableID:23880:1099`** |
| `--border/alt2` | `#e5e6e9` | `#54565f` | Lighter border variant, dividers, menu separators, disabled checkbox fill & border, contextual menu divider stroke, footer separator line. **Variable ID confirmed: `VariableID:23880:1100`** |
| `--border/base` | `#a4a6af` | *TBD* | Standard border, checkbox default border, footer text color (muted/tertiary). **Variable ID confirmed: `VariableID:23880:1098`**. Note: Disabled label text uses a **different variable** (`23879:2980`) with same hex #a4a6af — likely diverge in dark theme |
| `--border/accentsoft` | `#74abff` | *TBD* | Soft blue focus ring (FAB focus state 4px border, checkbox focus ring 4px border, contextual menu focus ring 4px border), **Banner Information border**, **Alert Primary outer border**. **Variable ID: `VariableID:23880:1103`**. Note: Disabled primary button fill uses a **different variable** (`23879:3186`) with same hex — will likely diverge in dark theme |
| `--border/errorsoft` *(tentative)* | `#ff779a` | *TBD* | Banner Error border, **Alert Error outer border** (softer than `--border/error`). **Variable ID: `VariableID:23880:1105`** |
| `--border/warningsoft` *(tentative)* | `#ffb067` | *TBD* | Banner Warning border, **Alert Warning outer border** (softer than `--border/warning`). **Variable ID: `VariableID:23880:1107`** |
| `--border/successsoft` *(tentative)* | `#dce55c` | *TBD* | **Alert Success outer border** (softer than `--border/success`). **Variable ID: `VariableID:23880:1109`** |
| `--border/success` *(tentative)* | `#8f9900` | *TBD* | Toast Success border/accent bar. **Variable ID: `VariableID:23880:1338`** |
| `--border/error` *(tentative)* | `#e3063d` | *TBD* | Toast Error border/accent bar. **Variable ID: `VariableID:23880:1336`** |
| `--border/warning` *(tentative)* | `#de6800` | *TBD* | Toast Warning border/accent bar. **Variable ID: `VariableID:23880:1337`** |
| `--border/accent` | `#0f67ff` | *TBD* | Toast Primary border/accent bar, contextual menu Selected 4px left accent border. **Variable IDs: `VariableID:23880:1335`** (Toast), **`VariableID:23880:1102`** (Contextual Menu) — two different VarIDs mapping to same token; same hex as `--text/accent` / `--background/accent` |

> **Note:** Tokens marked *TBD* were not directly confirmed from analyzed components' dark variants. They should be verified as more components are analyzed.
> **Note:** Status tokens (`--background/success`, `--background/error`, `--background/warning`, `--border/success`, `--border/error`, `--border/warning`) are tentative names based on variable IDs discovered in the Toast component. Exact token names should be verified against the design system's variable collection.

### Typography

Font family: `Roboto` (all weights), `Roboto Mono` (for code/tags)

| Token Name | Family | Weight | Size | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|---|---|
| `Text Regular/Size 1 (small)` | Roboto | 400 (Regular) | 12px | 16px | 0 | Small breadcrumb items (default state) |
| `Text Regular/Size 2 (base)` | Roboto | 400 (Regular) | 14px | 20px | 0 | Base breadcrumb items (default state) |
| `Text Regular/Size 3 (large)` | Roboto | 400 (Regular) | 16px | 20px | 0 | Body text in documentation |
| `Text Medium/Size 1 Medium (small)` | Roboto | 500 (Medium) | 12px | 16px | 0 | Small breadcrumb items (active state) |
| `Text Medium/Size 2 Medium (base) (H4 mobile)` | Roboto | 500 (Medium) | 14px | 20px | 0 | Base breadcrumb items (active state) |
| `Text Medium/Size 4 Medium` | Roboto | 500 (Medium) | 20px | *auto* | 0 | Empty state primary message title |
| `Text Medium/Size 6 Medium (H2)` | Roboto | 500 (Medium) | 22px | 32px | 0 | Section headings in docs |
| `Text Bold/Size 2 (base)` | Roboto | 700 (Bold) | 14px | *auto* | 0.28px | Button labels (primary, secondary, ghost), CTA bar info text |

### Spacing

| Token Name | Value | Notes |
|---|---|---|
| `--spacing/2` | `2px` | Minimal vertical padding (Breadcrumb wrapper) |
| `--spacing/4` | `4px` | Small gap between elements (separator ↔ text, menu icon ↔ label gap) |
| `--spacing/8` | `8px` | Medium spacing, active item horizontal padding, contextual menu item vertical padding |
| `--spacing/12 (Avoid)` | `12px` | Vertical padding for breadcrumb items, toast paddingRight (asymmetric). **Note:** Token is marked "(Avoid)" — may be deprecated, yet still used in toast component |
| `--spacing/10` | `10px` | Button internal gap, CTA bar tertiary↔button-group gap, toast root horizontal itemSpacing |
| `--spacing/16` | `16px` | Menu item horizontal padding, contextual menu item horizontal padding, CTA bar mobile padding |
| `--spacing/20` | `20px` | Button horizontal padding (Small buttons) |
| `--spacing/24` | `24px` | Larger spacing, CTA bar vertical padding |
| `--spacing/32` | `32px` | CTA bar desktop horizontal padding (default) |

### Shadows & Elevation

| Token Name | Definition | Usage |
|---|---|---|
| `BoxShadow/Elevation/2` | `0px 4px 14px rgba(37,41,55,0.10)`, `0px 1px 4px rgba(37,41,55,0.23)` | Contextual menus, popovers |
| `BoxShadow/Elevation/3` | `0px 14px 16px rgba(37,41,55,0.16)`, `2px 0px 10px rgba(37,41,55,0.16)`, `0px 0px 4px rgba(37,41,55,0.08)` | FAB button, CTA bar (elevated/fixed variant) |
| `BoxShadow/Elevation/4` *(tentative)* | `0px 40px 32px rgba(37,41,55,0.16)`, `0px 4px 16px rgba(37,41,55,0.16)`, `0px 0px 4px rgba(37,41,55,0.10)` | Toast notifications (highest elevation, floating overlay). **Name unconfirmed** — significantly larger offsets than Elevation/3 |

> Shadow color base: `#252937` (rgba variations). Shadows appear to be **theme-invariant** (same values in light and dark).

### Border Radius

| Token / Value | Usage |
|---|---|
| `28px` | FAB button (fully circular at 44×44px) |
| `12px` | Component container cards, doc cards |
| `5px` | Tags/badges |
| `4px` | Contextual menu / popover, small buttons (Primary, Secondary, Ghost), checkbox box, toast container |
| `12px 12px 0 0` | Sheet (mobile) top-rounded container (asymmetric) |

### Icon Sizes

> Icons use a consistent sizing system based on component context. All icons are contained in square frames with a transparent `Container` rectangle and a `Vector` child for the actual glyph.

| Icon Size | Usage | Components |
|---|---|---|
| `24×24px` | **Standard** — Dropdown arrows, action icons, close buttons, navigation icons, status icons | Breadcrumb (Down arrow), Sheet (Close, ChevronLeft, ChevronRight, action icons), Toast (status icons, Close, MoreVert), Footer (Refresh, Pause), Contextual Menu (action icons in composed menus), **Banner (InfoFill, ErrorFill, WarningFill, Close)**, **Alert (SuccessFill, ErrorFill, WarningFill, InfoFill, Close)** |
| `20×20px` | **Medium** — Home icon (Base size), submenu chevrons | Breadcrumb (Home @ Base size), Menu/Control (ChevronRight submenu indicator), Checkbox (box frame size) |
| `16×16px` | **Small** — Menu item icons, Home icon (Small size), FAB icon, check/minus glyphs, status icons | Menu/Control (item icon e.g. Notifications), Breadcrumb (Home @ Small size), FAB (Grid icon), Checkbox (Check/Minus glyph inside 20px box), Toast (status icon glyph) |

**Icon sizing rules:**
- **Base components** use 20px icons (Breadcrumb Base Home, Checkbox box, submenu chevron)
- **Small components** use 16px icons (Breadcrumb Small Home, menu item icons, FAB icon)
- **Dropdown arrows and close/action buttons** always use 24px containers regardless of component size
- Icon containers always have a transparent `Container` RECTANGLE + a `Vector` child with the actual glyph fill
- Glyph fills use color tokens (`--text/alt` for default, `--text/accent` for hover, `--text/base` for active/dark)

### Breakpoints
<!-- Populated after analysis -->

### Motion / Transitions
<!-- Populated after analysis -->

---

## Component Patterns & Conventions

### Naming Conventions

- **Component names**: PascalCase, descriptive (`Breadcrumb`, `BreadcrumbItem`)
- **Variant props**: PascalCase values for enums (`"Base"`, `"Small"`, `"Default"`, `"Hover"`, `"Active"`)
- **CSS variable naming**: Slash-delimited categories: `--category/variant` (e.g. `--text/base`, `--background/alt7`, `--spacing/4`)
- **Sub-components**: Named as `ParentName / SubName` in Figma (e.g. `Breadcrumb / Item`)
- **Figma page naming**: Prefixed with bullet `•` followed by component name (e.g. `• Breadcrumb`)

### File Structure Conventions

Each component page in Figma follows a consistent layout:
1. **Documentation frame** — "Doc Content" instance containing: description, when to use, don't use, considerations, content guidelines, accessibility guidelines, structure guidelines
2. **Component showcase (Light theme)** — Main component variants displayed in a grid with labeled axes (props as tags). Uses `--background/body: #f9f9fa` (light) with `--border/alt: #dbdcdf`.
3. **Component showcase (Dark theme)** — Same component shown in dark context. Uses `--background/body: #1d202b` (dark) with `--border/alt: #686b76`. **This is where dark token values can be extracted.**
4. **Elements/Controls frame** — Sub-component variants with state labels (default, hover, active) and size labels

### Props API Conventions

- **`size`** prop: Common across components. Values: `"Base"` | `"Small"`. Controls typography scale, icon size, and spacing.
- **`status`** prop: Used for interactive states. Values vary by component: `"Default"` | `"Hover"` | `"Active"` (Breadcrumb) or `"Default"` | `"Hover"` | `"Pressed"` | `"Focus"` (FAB) or `"Default"` | `"Hover"` | `"Selected"` | `"Disabled"` | `"Focus"` + combinations (Checkbox) or `"Default"` | `"Hover"` | `"Pressed"` | `"Selected"` | `"Focus"` | `"Disabled"` (Contextual Menu). In code, these map to CSS pseudo-classes (`:hover`, `:active`, `:focus-visible`, `:checked`, `:disabled`, `:indeterminate`).
- **`Device`** prop: Used for responsive variants. Values: `"Desktop"` | `"Mobile"`. Controls touch target sizing (e.g., Checkbox Mobile adds 12px vertical padding for 44px minimum). Found on: Checkbox.
- **`Elevation`** prop: Controls shadow/elevation. Values: `"3"` | `"None"`. Use "3" when component is fixed on top of scrollable content, "None" for inline. Found on: CTA Bar.
- **Boolean props**: Used for optional features (e.g. `icon`, `showArrow`, `Label`, `Tertiary`, `Secondary`)
- **Content props**: String props with sensible defaults (e.g. `content = "Name"`, `Info text = "Message"`)
- **INSTANCE_SWAP props**: Allow swapping sub-component instances (e.g. `Primary` button in CTA Bar can swap between Primary/Danger variants). Found on: CTA Bar.
- **Defaults**: All optional props have explicit defaults

### State Management Patterns

- **Default state**: Uses `--text/alt` (muted color) for non-active items
- **Hover state**: Uses `--text/accent` (blue) for text, hides dropdown arrow, no other visual change
- **Active state**: Uses `--text/base` (dark) with `font-weight: 500 (Medium)`, gains `px-[8px]` horizontal padding. Represents the current page/location.
- **State transitions in code**: Hover and Active are modeled as Figma variants (`status` prop) but should be implemented as CSS `:hover` and `.active`/`aria-current` states

### Theming Patterns

- **Approach:** CSS custom properties (variables) with two modes — **Light** (default) and **Dark**
- **How it works:** Same token names resolve to different values per theme. Components reference tokens, never raw colors.
- **Spacing & typography are theme-invariant** — they don't change between light and dark
- **Colors invert semantically (theme-aware):**
  - `--text/base`: dark text in light → light text in dark
  - `--text/alt`: medium gray in light → lighter gray in dark
  - `--background/base`: white in light → dark navy (#252937) in dark
  - `--background/body`: near-white in light → darker navy (#1d202b) in dark
  - `--border/alt`: light gray in light → medium gray in dark
  - `--border/alt2`: near-white (#e5e6e9) in light → dark gray (#54565f) in dark
- **Colors that are theme-invariant (same in both themes):**
  - `--text/overlay`: always `#ffffff` (white on colored surfaces)
  - `--background/accent`, `--background/accentalt`, `--background/accentalt2`: accent blues stay the same
  - `BoxShadow/Elevation/*`: shadow values don't change per theme
- **Figma representation:** Light and Dark variants are shown as separate "Component showcase container" frames on each component page. The dark frame has `--background/body` set to `#1d202b`.

### Accessibility Patterns

- **Keyboard navigation**: Full tab-through support with Enter to activate links/buttons
- **Focus rings**: Visible focus state using `--border/accentsoft` (#74abff) as a 4px border (confirmed on FAB and Checkbox)
- **Current page indication**: Active/current item should use `aria-current="page"` (Breadcrumb)
- **Semantic structure**: Breadcrumb uses `<nav aria-label="Breadcrumb">` with `<ol>` list; FAB uses `<button>` with `aria-label`
- **Separator handling**: Separators (slash `/`) should be decorative and hidden from screen readers (`aria-hidden="true"`)
- **Menu accessibility**: Contextual menus triggered by FAB should use `role="menu"` and `role="menuitem"` with keyboard arrow navigation
- **Touch targets**: Mobile variants enforce minimum 44px touch target area via padding (confirmed on Checkbox)
- **Form controls**: Checkboxes use Tab, Space, and Arrow keys; labels associated via proper markup for screen readers
- **Sheet dismiss behavior**: Action type determines dismiss behavior — single selection auto-dismisses, configuration stays open, destructive auto-dismisses with confirmation (Sheet documentation)

### Platform Conventions

- **Desktop/Mobile component pairing**: Some components have separate desktop and mobile versions rather than responsive variants:
  - **Contextual Menu** (desktop) ↔ **Sheet (Mobile)** — Same purpose (contextual actions), different interaction patterns
  - **CTA Bar** — Has Desktop and Mobile variants within the same component set (different prop values)
  - **Checkbox** — Has Desktop and Mobile variants via `Device` prop (touch target sizing)
  - **Footer** — Desktop-only, no mobile counterpart
- **Mobile-only patterns**:
  - Bottom-anchored containers with top-rounded corners (`border-radius: 12px 12px 0 0`)
  - Touch-friendly sizing (375px width, larger tap targets)
  - Swipe/dismiss gestures (auto-dismiss vs stay-open rules)

### Component Construction Patterns

> These patterns describe how components are structurally built in Figma, useful for implementing or improving existing components.

**Atom → Composed pattern:**
- **Atom components** (e.g. `Breadcrumb / Item`, `Menu/Control`, `Checkbox`) are the smallest units with full variant/state coverage
- **Composed components** (e.g. `Breadcrumb`, `Action Menu / Device`, `Sheet/Mobile/Sensor`) assemble atom instances into functional layouts
- When improving a composed component, focus changes on the atom first — all instances will update

**Common internal structure:**
- Root: auto-layout frame (HORIZONTAL or VERTICAL) with explicit padding and itemSpacing
- Icon child: FRAME with transparent RECTANGLE "Container" + VECTOR glyph — never raw vectors at root level
- Text child: TEXT node with explicit font family/weight/size, fill using color tokens
- Optional children: toggled via boolean props (`visible: false` when prop is `false`)

**Layout patterns by component type:**
- **Inline items** (Breadcrumb Item, Menu/Control, Checkbox): HORIZONTAL layout, HUG content, icon + text + optional trailing element
- **Containers** (Contextual Menu, Sheet, Toast): Composed with VERTICAL menu frame holding grouped atom instances, separated by dividers
- **Fixed bars** (CTA Bar, Footer): HORIZONTAL layout with FILL width, space-between via large itemSpacing in Figma (implement as `justify-content: space-between`)
- **Floating elements** (FAB, Toast): Elevated with shadow tokens, fixed position relative to viewport

**State implementation mapping (Figma → CSS):**
| Figma Variant Prop | CSS Implementation |
|---|---|
| `Status=Default` | No pseudo-class (base styles) |
| `Status=Hover` | `:hover` pseudo-class |
| `Status=Pressed` | `:active` pseudo-class |
| `Status=Focus` | `:focus-visible` pseudo-class |
| `Status=Selected` | `:checked` or `[aria-selected="true"]` or `.active` |
| `Status=Disabled` | `:disabled` or `[aria-disabled="true"]` |
| `Status=Active` | `[aria-current="page"]` or `.active` class |
| `Status=Indeterminate` | `:indeterminate` pseudo-class |
| `Device=Desktop/Mobile` | Media queries or container queries |
| Boolean props (`Icon`, `Label`, `Button`, etc.) | Conditional rendering / `display: none` |

### Confirmed Figma Variable Bindings

| Variable ID | Token Name | Value (Light) |
|---|---|---|
| `VariableID:23879:3177` | `--background/base` | `#ffffff` |
| `VariableID:23879:3178` | `--background/body` | `#f9f9fa` |
| `VariableID:23879:3187` | `--background/accentsoft` | `#f5f9ff` |
| `VariableID:23879:3193` | `--background/error` *(tentative)* | `#fff6f8` |
| `VariableID:23879:3196` | `--background/warning` *(tentative)* | `#fff8f3` |
| `VariableID:23879:3198` | `--background/success` *(tentative)* | `#fdffeb` |
| `VariableID:23880:1335` | `--border/accent` *(tentative)* | `#0f67ff` |
| `VariableID:23880:1336` | `--border/error` *(tentative)* | `#e3063d` |
| `VariableID:23880:1337` | `--border/warning` *(tentative)* | `#de6800` |
| `VariableID:23880:1338` | `--border/success` *(tentative)* | `#8f9900` |
| `VariableID:23880:1103` | `--border/accentsoft` | `#74abff` |
| `VariableID:23880:1105` | `--border/errorsoft` *(tentative)* | `#ff779a` |
| `VariableID:23880:1107` | `--border/warningsoft` *(tentative)* | `#ffb067` |
| `VariableID:23337:93155` | `--text/base` | `#31343f` |
| `VariableID:23879:2981` | `--text/accent` | `#0f67ff` |
| `VariableID:23880:1099` | `--border/alt` | `#dbdcdf` |
| `VariableID:23880:1104` | Alert Error accent border | `#e3063d` |
| `VariableID:23880:1108` | Alert Success accent border | `#8f9900` |
| `VariableID:23880:1109` | `--border/successsoft` *(tentative)* | `#dce55c` |
| `VariableID:23998:11347` | Alert Warning accent border | `#c45c00` |
| `VariableID:23879:3183` | `--background/accent` | `#0f67ff` |
| `VariableID:23879:3184` | `--background/accentalt` | `#065aec` |
| `VariableID:23879:3185` | `--background/accentalt2` | `#024ed3` |
| `VariableID:23879:2987` | `--text/overlay` | `#ffffff` |
| `VariableID:23879:3179` | `--background/hover` | `#f1f1f3` |
| `VariableID:23879:3182` | Disabled fill *(separate from hover)* | `#f1f1f3` |
| `VariableID:23880:1098` | `--border/base` | `#a4a6af` |
| `VariableID:23880:1100` | `--border/alt2` | `#e5e6e9` |
| `VariableID:23879:2980` | Disabled text *(separate from border/base)* | `#a4a6af` |
| `VariableID:23879:2979` | `--text/alt` | `#686b76` |
| `VariableID:23879:3180` | `--background/pressed` | `#e5e6e9` |
| `VariableID:23880:1102` | `--border/accent` *(contextual menu)* | `#0f67ff` |
| `VariableID:23879:3186` | Disabled primary fill *(separate from --border/accentsoft)* | `#74abff` |

---

## Component Catalog

### Alert (Inline)

- **Purpose:** Provides contextual feedback messages inline within the page flow. Communicates status about a specific section, action, or condition. Unlike Banner (page/section level, persistent) and Toast (transient overlay), Alert is embedded in content and supports both brief messages and headline + caption layouts.
- **Figma Page:** `• Alerts & Notifications` (node `16130:22099`)
- **Figma Component Name:** `Alert/Inline` (COMPONENT_SET `17515:59497`)

- **Props/API:**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `Type` | `"ShortText" \| "LongText"` | `"ShortText"` | Content layout — single-line message (ShortText) or headline + caption (LongText) |
  | `Status` | `"Success" \| "Error" \| "Warning" \| "Primary" \| "Secondary"` | `"Success"` | Visual status variant — controls fill, border colors, and status icon |
  | `Dismiss` | `boolean` | `false` | Show/hide the close (X) button |

- **Figma Prop Name Mapping (from COMPONENT_SET `17515:59497`):**
  - `Dismiss#30235:0` → `Dismiss` (boolean, default: false) — toggles close button visibility
  - `Type` → `Type` (variant: "ShortText" | "LongText")
  - `Status` → `Status` (variant: "Success" | "Error" | "Warning" | "Primary" | "Secondary")

- **Variants (ShortText — canonical dual-border pattern, all 5 statuses):**

  | Status | Node ID | Root Fill | Root Fill VarID | Root Stroke (outer, soft) | Root Stroke VarID | Wrapper Stroke (inner, accent) | Wrapper Stroke VarID |
  |---|---|---|---|---|---|---|---|
  | Success | `30256:4603` | `#fdffeb` | `23879:3198` | `#dce55c` | `23880:1109` | `#8f9900` | `23880:1108` |
  | Error | `30256:4582` | `#fff6f8` | `23879:3193` | `#ff779a` | `23880:1105` | `#e3063d` | `23880:1104` |
  | Warning | `30256:4542` | `#fff8f3` | `23879:3196` | `#ffb067` | `23880:1107` | `#c45c00` | `23998:11347` |
  | Primary | `30256:4529` | `#f5f9ff` | `23879:3187` | `#74abff` | `23880:1103` | `#0f67ff` | `23879:2981` |
  | Secondary | `30235:4777` | `#f9f9fa` | `23879:3178` | `#dbdcdf` | `23880:1099` | `#0f67ff` | `23879:2981` |

  > **Token mapping:**
  > - Success fill `#fdffeb` = `--background/success`, outer `#dce55c` = `--border/successsoft` **(NEW)**, accent `#8f9900` (`23880:1108` — same hex as `--border/success` but different variable from Toast's `23880:1338`)
  > - Error fill `#fff6f8` = `--background/error`, outer `#ff779a` = `--border/errorsoft`, accent `#e3063d` (`23880:1104` — same hex as `--border/error` but different variable from Toast's `23880:1336`)
  > - Warning fill `#fff8f3` = `--background/warning`, outer `#ffb067` = `--border/warningsoft`, accent `#c45c00` (`23998:11347` — **different hex** from Toast's `--border/warning` #de6800)
  > - Primary fill `#f5f9ff` = `--background/accentsoft`, outer `#74abff` = `--border/accentsoft`, accent `#0f67ff` = `--text/accent`
  > - Secondary fill `#f9f9fa` = `--background/body`, outer `#dbdcdf` = `--border/alt` (`23880:1099`), accent `#0f67ff` = `--text/accent`
  > - **Pattern:** Alert uses _soft_ outer borders (shared with Banner) + _accent_ inner borders (left bar). Fill tokens shared across Alert/Banner/Toast. Accent border variables are separate from Toast's border variables despite matching hex in some cases.

- **Variants (LongText — structural inconsistencies noted):**

  | Status | Node ID | Has Wrapper? | Root Stroke | Root Stroke VarID | Root Fill VarID | Notes |
  |---|---|---|---|---|---|---|
  | Success | `30235:4822` | NO | `#8f9900` (accent) | `23880:1108` | `23879:3198` | Single border, accent on root |
  | Error | `30235:4838` | NO | `#e3063d` (accent) | `23880:1104` | `23879:3193` | Single border, accent on root |
  | Warning | `30235:4853` | NO | `#ffb067` (soft) | `23880:1107` | `23879:3193` | **Bug:** Uses Error fill VarID instead of Warning's `23879:3196` |
  | Primary | `30235:4868` | YES | `#74abff` (soft) | `23880:1103` | `23879:3187` | Dual border, matches ShortText |
  | Secondary | `30235:4884` | YES | `#dbdcdf` (soft) | `23880:1099` | `23879:3178` | Dual border, matches ShortText |

  > **Structural inconsistency:** LongText variants have mixed implementations:
  > - **Primary & Secondary**: Correct dual-border pattern (Root + Wrapper), matching ShortText
  > - **Success & Error**: Missing Wrapper, accent border applied directly to Root, soft outer border lost
  > - **Warning**: Missing Wrapper, uses soft border on Root (not accent), AND has wrong fill VarID (Error's `23879:3193` instead of Warning's `23879:3196`)
  > - **Recommendation:** Implement ALL variants with the canonical dual-border pattern (as in ShortText and LongText Primary/Secondary). The inconsistencies in Success/Error/Warning LongText appear to be Figma file bugs.

- **Visual Design:**

  | Element | Token / Value | Notes |
  |---|---|---|
  | Container background | Status-specific fill (see variant table) | Soft tinted background per status |
  | Outer border | Status-specific soft stroke, `strokeWeight: 1px`, `strokeAlign: INSIDE` | Subtle outer border (Root level) |
  | Inner accent border | Status-specific accent stroke, `strokeWeight: 1px`, `strokeAlign: INSIDE` | Strong left accent bar (Wrapper level, likely left-only via individual stroke weights) |
  | Corner radius | `4px` | Both Root and Wrapper have `cornerRadius: 4` |
  | Shadow | None | No elevation — same as Banner, unlike Toast (Elevation/4) |
  | Status icon | 24×24px, status-specific | SuccessFill, ErrorFill (`96:1190`), WarningFill (`5208:10192`), InfoFill (`5208:10202`) |
  | Message text | `--text/base` (#31343f) | ShortText: single line; LongText: headline + caption |
  | Close button | `Small/Ghost` Icon variant (`19905:79546`) | ~36×28px, contains Close icon 24×24px, hidden by default |

- **Tokens Used:**
  - **Colors (status-specific, theme-aware):**
    - Success: fill `--background/success` (`#fdffeb`, `23879:3198`), outer `--border/successsoft` (`#dce55c`, `23880:1109`), accent `23880:1108` (`#8f9900`)
    - Error: fill `--background/error` (`#fff6f8`, `23879:3193`), outer `--border/errorsoft` (`#ff779a`, `23880:1105`), accent `23880:1104` (`#e3063d`)
    - Warning: fill `--background/warning` (`#fff8f3`, `23879:3196`), outer `--border/warningsoft` (`#ffb067`, `23880:1107`), accent `23998:11347` (`#c45c00`)
    - Primary: fill `--background/accentsoft` (`#f5f9ff`, `23879:3187`), outer `--border/accentsoft` (`#74abff`, `23880:1103`), accent `--text/accent` (`#0f67ff`, `23879:2981`)
    - Secondary: fill `--background/body` (`#f9f9fa`, `23879:3178`), outer `--border/alt` (`#dbdcdf`, `23880:1099`), accent `--text/accent` (`#0f67ff`, `23879:2981`)
  - **Colors (shared):**
    - `--text/base` (`#31343f`, `VariableID:23337:93155`) — All message/headline/caption text
  - **Spacing (theme-invariant):**
    - Wrapper padding: `16px` left/right, `8px` top/bottom
    - Message Container itemSpacing: `8px` (gap between icon and text)
    - ShortText text frame: `paddingTop: 3px` (vertical centering within 24px icon)
    - LongText text frame: `itemSpacing: 4px` (gap between headline and caption), `VERTICAL` layout
  - **Typography (theme-invariant):**
    - ShortText message: `Text Regular/Size 2 (base)` — Roboto 400, 14px, lineHeight: 20px
    - LongText headline/caption: Exact tokens TBD (API truncated text node children)

- **Internal Structure (ShortText — canonical, confirmed via dev mode):**

  **DUAL-BORDER PATTERN:** Alert uses TWO nested elements to create a left accent bar effect:
  - **Root** COMPONENT: status-specific fill + soft outer border (subtle, all sides)
  - **Wrapper** FRAME: accent inner border (strong color, likely left-only via individual stroke weights)

  ```
  Root (COMPONENT, ~548×36px, HORIZONTAL, cornerRadius: 4)
  ├── Fill: status background (boundVariables)
  ├── Stroke: soft outer border (boundVariables), 1px INSIDE
  └── Wrapper (FRAME, layoutGrow:1, layoutAlign:STRETCH, HORIZONTAL, SPACE_BETWEEN)
      ├── Stroke: accent border (boundVariables), 1px INSIDE, cornerRadius: 4
      ├── Padding: 16px L/R, 8px T/B
      ├── Message Container (FRAME, layoutGrow:1, HORIZONTAL, itemSpacing:8)
      │   ├── Icon (INSTANCE, 24×24px) — status-specific
      │   └── Text frame (FRAME, paddingTop:3px, HORIZONTAL)
      │       └── Text (TEXT) — message, --text/base, Roboto 400, 14px
      └── Small/Ghost (INSTANCE 19905:79546, ~36×28px) — close button
          ├── Contains Close icon (841:6), 24×24px
          └── visible: false (default, controlled by Dismiss#30235:0)
  ```

- **Internal Structure (LongText — canonical, from Primary/Secondary):**

  ```
  Root (COMPONENT, ~548×60px, HORIZONTAL, cornerRadius: 4)
  ├── Fill: status background + Stroke: soft outer border (same as ShortText)
  └── Wrapper (FRAME, same as ShortText)
      ├── Message Container (FRAME, layoutGrow:1, HORIZONTAL, itemSpacing:8)
      │   ├── Icon (INSTANCE, 24×24px) — status-specific
      │   └── Text frame (FRAME, VERTICAL, itemSpacing:4, counterAxisSizingMode:FIXED)
      │       ├── Headline (TEXT) — title
      │       └── Caption (TEXT) — description
      └── Small/Ghost (INSTANCE) — close button, visible: false
  ```

- **CSS Implementation Reference:**
  ```
  /* Alert (Inline) — Dual-border container */
  .alert-inline {
    display: flex;
    flex-direction: row;
    border-radius: 4px;
    border: 1px solid var(--border-status-soft);  /* Root: soft outer border */
    background: var(--bg-status);
  }
  .alert-inline__wrapper {
    flex: 1;                        /* layoutGrow: 1 */
    display: flex;
    flex-direction: row;
    justify-content: space-between; /* SPACE_BETWEEN */
    align-items: flex-start;
    padding: 8px 16px;
    border-radius: 4px;
    border-left: 2px solid var(--border-status-accent); /* Accent left bar */
    /* Note: Figma shows strokeWeight:1 uniform but likely uses individual
       stroke weights for left-only. Verify with Desktop Bridge. */
  }
  .alert-inline__message {
    flex: 1;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }
  /* ShortText: single line, vertically centered with icon */
  .alert-inline__text--short {
    padding-top: 3px;             /* vertical centering with 24px icon */
  }
  /* LongText: headline + caption stacked */
  .alert-inline__text--long {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .alert-inline__close {
    /* Small/Ghost Icon variant */
  }
  ```

- **Icon Sizes:**
  - Status icon (SuccessFill, ErrorFill, WarningFill, InfoFill): **24×24px**
  - Close button icon (Close): **24×24px** inside ghost button

- **Accessibility:**
  - Use `role="alert"` for important status messages requiring screen reader announcement
  - Close button should have `aria-label="Dismiss alert"` or similar
  - Keyboard-accessible close button (Tab + Enter/Space)
  - Color alone does not convey status — icon and text provide redundant cues

- **Dependencies:**
  - Buttons: `Small/Ghost` Icon variant (COMPONENT `19905:79546`) — close button
  - Icons: `ErrorFill` (`96:1190`), `WarningFill` (`5208:10192`), `InfoFill` (`5208:10202`), `Close` (`841:6`), SuccessFill (ID TBD)

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** For inline contextual feedback about a specific section or action result; when message is important but non-blocking; supports 5 severity levels: Success (green), Error (red), Warning (orange), Primary/Informational (blue), Secondary/Neutral (gray)
  - **Don't use:** For page-level persistent messages — use Banner; for transient notifications — use Toast; for blocking/critical errors — use Modal
  - **ShortText vs LongText:** Use ShortText for brief single-line messages; use LongText when a headline + descriptive caption is needed for clarity
  - **Dismiss behavior:** Close button is hidden by default (`Dismiss: false`). Enable when the alert can be safely dismissed without losing important context
  - **Dual-border pattern:** The component uses a nested Root + Wrapper structure to create a left accent bar: Root provides soft outer border, Wrapper provides strong accent border (left-only). This is the canonical pattern — implement with CSS `border` on outer container and `border-left` on inner content wrapper
  - **Content:** Keep messages concise and actionable. ShortText for simple status updates, LongText when headline context helps users understand the alert's significance

- **Alert vs Banner vs Toast Comparison:**

  | Aspect | Alert (Inline) | Banner | Toast |
  |---|---|---|---|
  | **Position** | Inline within content | Inline, under header/section | Floating overlay |
  | **Width** | Container-width (~548px in Figma) | Full-width | Fixed 320px |
  | **Persistence** | Until dismissed or condition resolves | Until dismissed or condition resolves | Transient, auto-dismiss |
  | **Shadow** | None | None | Elevation/4 |
  | **Border pattern** | Dual: soft outer + accent inner (left bar) | Single: soft border | Single: strong border + left accent bar |
  | **Status types** | Success, Error, Warning, Primary, Secondary | Information, Error, Warning | Success, Error, Warning, Primary |
  | **Content types** | ShortText / LongText | Single line | Message + optional caption/button |
  | **Close button** | Optional (Dismiss, default hidden) | Optional (Close, default shown) | Optional (Clearable) |
  | **Fill tokens** | Same pool | Same pool | Same pool |
  | **Border tokens** | Soft outer + accent inner (separate vars) | Soft only | Strong only |

- **Open Questions:**
  - Left accent bar implementation: Like Toast, the Wrapper stroke likely uses individual stroke weights (`strokeLeftWeight` etc.) to create a left-only accent bar. Needs Figma Desktop Bridge plugin access to confirm (REST API only returns uniform `strokeWeight: 1`).
  - LongText inconsistencies: 3 of 5 LongText variants (Success, Error, Warning) have incorrect structure — missing Wrapper frame and/or wrong fill variable. These appear to be Figma file bugs. Implementation should follow the canonical dual-border pattern.
  - Dark theme: No dark variant values confirmed for Alert-specific tokens.
  - Alert accent border variables vs Toast: Some Alert accent borders share hex values with Toast border tokens but use DIFFERENT variable IDs (e.g., Alert `23880:1108` vs Toast `23880:1338`, both `#8f9900`). These may diverge in dark theme. Warning already differs: Alert `#c45c00` vs Toast `#de6800`.
  - Icon component IDs: SuccessFill icon component ID needs confirmation (API data showed `96:1190` for the icon instance in Error variants but named "Success Icon" — likely a naming bug in Figma).
  - LongText typography tokens: Exact text styles for headline and caption in LongText variants need confirmation (API truncated deeply nested text children).

### Banner

- **Purpose:** Communicates a state that affects a system, feature, or page. Helps users stay informed about important conditions without interrupting their workflow. Non-blocking, persistent, and placed inline beneath the header or relevant section.
- **Figma Page:** `• Alerts & Notifications` (node `16130:22099`)
- **Figma Component Name:** `Banner` (COMPONENT_SET `24524:2267`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/banner/banner.html)

- **Props/API:**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `Type` | `"Information" \| "Error" \| "Warning"` | `"Information"` | Visual status variant — controls background fill, border color, and status icon |
  | `Content` | `"Single Line"` | `"Single Line"` | Content layout — currently only single line available |
  | `Close` | `boolean` | `true` | Show/hide the close (X) button |

- **Figma Prop Name Mapping (from COMPONENT_SET `24524:2267`):**
  - `Type` → `Type` (variant: "Information" | "Error" | "Warning")
  - `Content` → `Content` (variant: "Single Line")
  - `Close#29548:0` → `Close` (boolean, default: true) — toggles close button visibility

- **Variants (by Type):**

  | Type | Node ID | Fill (hex) | Fill Variable ID | Stroke (hex) | Stroke Variable ID | Icon |
  |---|---|---|---|---|---|---|
  | Information | `29428:4011` | `#f5f9ff` | `VariableID:23879:3187` | `#74abff` | `VariableID:23880:1103` | `InfoFill` (`5208:10202`) |
  | Error | `29432:4057` | `#fff6f8` | `VariableID:23879:3193` | `#ff779a` | `VariableID:23880:1105` | `ErrorFill` (`96:1190`) |
  | Warning | `29432:4087` | `#fff8f3` | `VariableID:23879:3196` | `#ffb067` | `VariableID:23880:1107` | `WarningFill` (`5208:10192`) |

  > **Token mapping:**
  > - Information fill `#f5f9ff` = `--background/accentsoft`, stroke `#74abff` = `--border/accentsoft`
  > - Error fill `#fff6f8` = `--background/error` (shared with Toast), stroke `#ff779a` = `--border/errorsoft` (NEW — softer than Toast's `--border/error` #e3063d)
  > - Warning fill `#fff8f3` = `--background/warning` (shared with Toast), stroke `#ffb067` = `--border/warningsoft` (NEW — softer than Toast's `--border/warning` #de6800)
  > - **Pattern:** Banner uses _soft_ border tokens while Toast uses _strong_ border tokens. Fill tokens are shared.

- **Visual Design:**

  | Element | Token / Value | Notes |
  |---|---|---|
  | Container background | Status-specific fill (see table above) | Soft tinted background per status |
  | Container border | Status-specific stroke, `strokeWeight: 1px`, `strokeAlign: INSIDE` | 1px border all around |
  | Corner radius | None (`0px`) | No rounded corners — full-width inline element |
  | Shadow | None | No elevation — unlike Toast which uses Elevation/4 |
  | Status icon | 24×24px status-specific icon | InfoFill (blue), ErrorFill (red), WarningFill (orange) |
  | Message text | `--text/base` (#31343f) | `Text Regular/Size 2 (base)` — Roboto 400, 14px, lineHeight: 20px |
  | Inline link text | `--text/accent` (#0f67ff) | Same font, color override via character style override |
  | Close button | `Small/Ghost` Icon variant (`19905:79546`) | 36×36px, contains Close icon 24×24px |

- **Tokens Used:**
  - **Colors (status-specific, theme-aware):**
    - Information fill: `--background/accentsoft` (`#f5f9ff`, `VariableID:23879:3187`)
    - Information border: `--border/accentsoft` (`#74abff`, `VariableID:23880:1103`)
    - Error fill: `--background/error` (`#fff6f8`, `VariableID:23879:3193`)
    - Error border: `--border/errorsoft` (`#ff779a`, `VariableID:23880:1105`)
    - Warning fill: `--background/warning` (`#fff8f3`, `VariableID:23879:3196`)
    - Warning border: `--border/warningsoft` (`#ffb067`, `VariableID:23880:1107`)
  - **Colors (shared):**
    - `--text/base` (`#31343f`, `VariableID:23337:93155`) — Message text
    - `--text/accent` (`#0f67ff`, `VariableID:23879:2981`) — Inline link text (character style override)
  - **Spacing (theme-invariant):**
    - `12px` — Root horizontal padding (paddingLeft, paddingRight)
    - `32px` — Root itemSpacing (gap between spacer, content frame, close button)
    - `4px` — Content frame vertical padding (paddingTop, paddingBottom)
    - `8px` — Content frame itemSpacing (gap between icon and text)
  - **Typography (theme-invariant):**
    - `Text Regular/Size 2 (base)` — Roboto 400, 14px, lineHeight 20px — Message text and inline link

- **Internal Structure (confirmed via dev mode — identical across all 3 type variants):**
  - Root: COMPONENT, 698×40px (`primaryAxisSizingMode: FIXED` width, height from content), `layoutMode: HORIZONTAL`
    - `primaryAxisAlignItems: CENTER` → CSS: `justify-content: center`
    - `counterAxisAlignItems: CENTER` → CSS: `align-items: center`
    - Padding: `left: 12px`, `right: 12px` (no vertical padding)
    - `itemSpacing: 32px` → CSS: `gap: 32px`
    - Fill: status-specific background (with `boundVariables` color binding)
    - Stroke: status-specific border (with `boundVariables` color binding), `strokeWeight: 1px`, `strokeAlign: INSIDE`
    - No effects (no shadow)
  - Children (3 slots):
    1. **Small/Ghost [spacer]** (INSTANCE `19905:79546`, Icon variant): 40×40px, **`opacity: 0`** — **INVISIBLE SPACER**
       - Contains Close icon (24×24px) but fully transparent
       - Purpose: balances layout so content frame appears visually centered even with a close button on only one side
       - This is a key layout pattern — mirror the close button size on the opposite side with an invisible element
    2. **Frame 5747** (content frame): `layoutGrow: 1` (→ CSS: `flex: 1`), `layoutAlign: STRETCH`
       - `layoutMode: HORIZONTAL`, `primaryAxisAlignItems: CENTER`, `counterAxisAlignItems: CENTER`
       - `paddingTop: 4px`, `paddingBottom: 4px`, `itemSpacing: 8px`
       - `primaryAxisSizingMode: FIXED`, `counterAxisSizingMode: FIXED`
       - Children:
         a. **Icon** (INSTANCE): 24×24px — status-specific icon (InfoFill / ErrorFill / WarningFill)
         b. **Text** (TEXT): Message with optional inline link
            - Fill: `--text/base` (#31343f, `VariableID:23337:93155`), Roboto Regular 400, 14px, lineHeight: 20px
            - "Optional Link" portion uses `characterStyleOverrides` with `--text/accent` (#0f67ff, `VariableID:23879:2981`)
            - This is an **inline link pattern** — not a separate component, but a text run with color override
    3. **Small/Ghost [close button]** (INSTANCE `19905:79546`, Icon variant): 36×36px — **ACTUAL CLOSE BUTTON**
       - `primaryAxisSizingMode: FIXED`, `counterAxisSizingMode: FIXED`
       - Contains Close icon (`841:6`), 24×24px
       - Toggled by `Close#29548:0` boolean prop
       - Component: `Small/Ghost` with `Type: "Icon"`, `Status: "Default"`

- **CSS Implementation Reference:**
  ```
  /* Banner container */
  .banner {
    display: flex;
    flex-direction: row;
    align-items: center;           /* counterAxisAlignItems: CENTER */
    justify-content: center;       /* primaryAxisAlignItems: CENTER */
    width: 100%;                    /* full-width inline */
    padding: 0 12px;                /* no vertical padding, 12px horizontal */
    gap: 32px;                      /* itemSpacing: 32 */
    border: 1px solid var(--border-status);  /* strokeWeight: 1, strokeAlign: INSIDE */
    background: var(--bg-status);
  }
  /* Invisible spacer (mirrors close button for centering) */
  .banner__spacer {
    width: 40px;
    height: 40px;
    opacity: 0;
    pointer-events: none;
  }
  /* Content frame */
  .banner__content {
    flex: 1;                        /* layoutGrow: 1 */
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4px 0;
    gap: 8px;
  }
  /* Close button */
  .banner__close {
    width: 36px;
    height: 36px;
    /* Small/Ghost Icon variant */
  }
  ```

- **Icon Sizes:**
  - Status icon (InfoFill, ErrorFill, WarningFill): **24×24px**
  - Close button icon (Close): **24×24px** inside 36×36px ghost button
  - Invisible spacer icon (Close): **24×24px** inside 40×40px ghost button (opacity: 0)

- **Accessibility:**
  - Provide a keyboard-accessible close button (if present)
  - Use `role="alert"` or `role="status"` for screen reader announcements
  - Close button should have `aria-label="Close banner"` or similar

- **Responsive Behavior:**
  - Full-width, inline element — no fixed pixel width
  - Height adapts to content (40px for single line)
  - Placed underneath the header or section it relates to

- **Dependencies:**
  - Buttons: `Small/Ghost` Icon variant (COMPONENT `19905:79546`) — used for close button and invisible spacer
  - Icons: `InfoFill` (`5208:10202`), `ErrorFill` (`96:1190`), `WarningFill` (`5208:10192`), `Close` (`841:6`)

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** To inform users about system, feature, or page-level states; when the message is important but non-blocking; can include a link for more information or next steps; use variants to indicate message type: Information (Blue), Warning (Orange), Critical/Error (Red)
  - **Don't use:** For critical issues that block user interaction or require immediate action — use a Modal or Inline Alert instead; for transient or low-priority messages — use a Toast
  - **Considerations:** Place underneath the header or section it relates to; include a close button only if the message is not critical; use clear visual hierarchy to distinguish between variants; ensure the banner is persistent enough to be noticed, especially for critical states
  - **Content:** Be concise and direct; keep it static; clearly state the issue or status; offer a link for additional information or actions; match tone to the severity of the message; icons can be customized with any icon from the library
  - **Accessibility:** Provide a keyboard-accessible close button (if present); use `role="alert"` or `role="status"` for screen reader announcements
  - **Structure:** Message area with status icon + primary text communicating the state; optional inline link for more details or actions (styled as character override with `--text/accent`); variant styling: color-coded to reflect status (fill + border + icon); optional close button (`Small/Ghost` Icon variant)

- **Banner vs Toast Comparison:**

  | Aspect | Banner | Toast |
  |---|---|---|
  | **Position** | Inline, underneath header/section | Floating, bottom-left (desktop) / bottom-center (mobile) |
  | **Width** | Full-width (flexible) | Fixed 320px |
  | **Persistence** | Persistent until dismissed or condition resolves | Transient, auto-dismiss |
  | **Shadow** | None | Elevation/4 |
  | **Border tokens** | Soft variants (`--border/accentsoft`, `--border/errorsoft`, `--border/warningsoft`) | Strong variants (`--border/accent`, `--border/error`, `--border/warning`) |
  | **Fill tokens** | Same (`--background/accentsoft`, `--background/error`, `--background/warning`) | Same |
  | **Status types** | Information, Error, Warning | Success, Error, Warning, Primary |
  | **Close button** | Optional (boolean prop), no more-options | Optional (Clearable prop), includes more-options |

- **Examples:**
  - Information: `[ℹ️ The new interface is still in development and not yet feature complete. ✕]` — blue tint
  - Error: `[❗ Instance offline: https://frontier.paesslergmbh.de/1516/ View server ✕]` — pink tint with link
  - Warning: `[⚠️ Sensor count reached its limit and some sensors are paused. Optional Link ✕]` — orange tint with link

- **Open Questions:**
  - Multi-line content: The `Content` variant prop has only "Single Line" option. A multi-line variant may be planned but is not yet implemented.
  - Dark theme: The `• Alerts & Notifications` page has a `Notification/Dark` frame (`24527:2291`) with a dark Banner component set, but exact dark token values need separate analysis.
  - Invisible spacer sizing: The left spacer is 40×40px while the right close button is 36×36px (with FIXED sizing). This creates a 4px asymmetry — may be intentional or a minor inconsistency.

### Breadcrumb

- **Purpose:** Provides hierarchical navigation that shows users their current location within the system and enables quick navigation back to any parent level. Serves as shortcuts for complex system hierarchies.
- **Figma Page:** `• Breadcrumb` (node `9540:31`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/breadcrumb/breadcrumb.html)

- **Props/API (Breadcrumb — parent component):**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `levels` | `"1" \| "2" \| "3" \| "4" \| "5"` | `"1"` | Number of hierarchy levels to display |
  | `size` | `"Base" \| "Small"` | `"Base"` | Controls overall sizing of all child items |

- **Props/API (BreadcrumbItem — sub-component):**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `status` | `"Default" \| "Hover" \| "Active"` | `"Default"` | Interactive state of the item |
  | `icon` | `boolean` | `false` | When `true`, shows Home icon instead of text (used for root level) |
  | `showArrow` | `boolean` | `true` | Shows dropdown arrow for alternative navigation paths |
  | `content` | `string` | `"Name"` | Text label for the breadcrumb level |
  | `size` | `"Base" \| "Small"` | `"Base"` | Size variant |

- **Variants:**
  - **By levels:** 1 through 5 levels of depth
  - **By size:** Base (14px text, 20px icons) and Small (12px text, 16px icons)
  - Left column = Base, Right column = Small in Figma layout

- **States (per BreadcrumbItem):**

  **Light Theme:**

  | State | Text Color | Font Weight | Icon Color | Dropdown Arrow | Extra Padding |
  |---|---|---|---|---|---|
  | Default | `--text/alt` (#686b76) | 400 (Regular) | Gray (#686b76) | Visible (if `showArrow`) | None |
  | Hover | `--text/accent` (#0f67ff) | 400 (Regular) | Blue (#0f67ff) | Hidden | None |
  | Active | `--text/base` (#31343f) | 500 (Medium) | Dark (#31343f) | Visible (if `showArrow`) | `px-[8px]` |

  **Dark Theme** (same tokens, different resolved values):

  | State | Text Color | Font Weight | Icon Color | Dropdown Arrow | Extra Padding |
  |---|---|---|---|---|---|
  | Default | `--text/alt` (#babcc2) | 400 (Regular) | Light gray (#babcc2) | Visible (if `showArrow`) | None |
  | Hover | `--text/accent` (*TBD dark value*) | 400 (Regular) | Accent (*TBD*) | Hidden | None |
  | Active | `--text/base` (#e5e6e9) | 500 (Medium) | Near-white (#e5e6e9) | Visible (if `showArrow`) | `px-[8px]` |

  > **Theming note:** The component uses CSS variables, so theme switching is automatic. No component-level changes needed — only the variable definitions change between themes.

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--text/base` — Light: `#31343f` / Dark: `#e5e6e9` — Active items
    - `--text/alt` — Light: `#686b76` / Dark: `#babcc2` — Default items
    - `--text/accent` — Light: `#0f67ff` / Dark: *TBD* — Hover items
    - `--background/body` — Light: `#f9f9fa` / Dark: `#1d202b` — Showcase container
    - `--border/alt` — Light: `#dbdcdf` / Dark: `#686b76` — Container border
  - **Spacing (theme-invariant):** `--spacing/2` (wrapper py), `--spacing/4` (item gap), `--spacing/8` (active px), `--spacing/12-(avoid)` (item py)
  - **Typography (theme-invariant):** `Text Regular/Size 1 (small)`, `Text Regular/Size 2 (base)`, `Text Medium/Size 1 Medium (small)`, `Text Medium/Size 2 Medium (base) (H4 mobile)`

- **Internal Structure:**
  - `Breadcrumb` (wrapper) → contains `Breadcrumb Wrapper` (flex row)
    - First child: `BreadcrumbItem` with `icon=true` (Home icon + dropdown) — always present as root
    - Subsequent children: `BreadcrumbItem` with `icon=false` (separator + text label + optional dropdown)
    - Last item: `status="Active"` (bold, dark text, represents current page)
  - **Separator:** Forward slash `/` icon (`Slashforward`, 14×14px) — placed inside each non-root `BreadcrumbItem`
  - **Home icon:** 20×20px (Base) or 16×16px (Small)
  - **Dropdown arrow:** `Down` icon, 24×24px — present on Default and Active states, hidden on Hover

- **Accessibility:**
  - Full tab-through support with Enter to activate links
  - Current/active page should be indicated for screen readers
  - Structure: root always has icon, levels separated by visual slash

- **Responsive Behavior:**
  - Two size variants (Base/Small) for different density contexts
  - No explicit breakpoint-based behavior documented — size selection is manual

- **Dependencies:**
  - Icons: `Home` (house icon), `Slashforward` (separator), `Down` (dropdown chevron)
  - Shared: `Divider/Horizontal` component (in docs only)

- **Figma Prop Name Mapping:**
  - `Show Arrow#30730:0` → `showArrow` (boolean, default: true)
  - `Content#30734:7` → `content` (text, default: "Name")
  - `Status` → `status` (variant)
  - `Icon` → `icon` (variant: "False" | "True")
  - `Size` → `size` (variant)

- **Icon Sizes:**
  - Home icon: **20×20px** (Base), **16×16px** (Small)
  - Down arrow: **24×24px** (both sizes) — container 24×24, inner vector 10×5px
  - Separator (Slashforward): **14×14px**

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** When users navigate through multiple levels of sections; to help users understand their position within nested views and pages; only show dropdown arrows when multiple navigation paths are available
  - **Don't use:** For single-level or simple two-level hierarchies; as the main navigation method — it's supplementary
  - **Considerations:** Always highlight current page to provide context
  - **Content:** Use concise, descriptive labels that immediately convey the level's purpose; users should quickly identify their location
  - **Accessibility:** Full tab-through support with Enter to activate links; use `<nav aria-label="Breadcrumb">` with `<ol>` list; current page uses `aria-current="page"`; separators should be `aria-hidden="true"`
  - **Structure:** Always display root with an icon (Home); introduce each level with a separator (`/`); dropdown icon displays alternative navigation paths; last item is always the active/current page (bold)

- **Examples:**
  - 1-level: `[Home icon ▼] / Name ▼`
  - 3-level: `[Home icon ▼] / Name ▼ / Name ▼ / **Name** ▼` (last is active/bold)
  - 5-level: `[Home icon ▼] / Name ▼ / Name ▼ / Name ▼ / Name ▼ / Name ▼`

### Floating Action Button (FAB)

- **Purpose:** Serves as a consistent, easily discoverable access point for contextual actions within the interface. Always positioned in the same place, it provides quick access to screen-specific actions without requiring navigation away from the current context.
- **Figma Page:** `• Buttons: Floating Action Button` (node `12473:0`)
- **Figma Component Name:** `Floating Button`
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/floating-action-button/floating-action-button.html)

- **Props/API:**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `status` | `"Default" \| "Hover" \| "Pressed" \| "Focus"` | `"Default"` | Interactive state |
  | `contextualMenu` | `boolean` | `false` | When `true` + Pressed, shows a contextual menu |

- **Variants:** Single variant — no size or style variations. Fixed 44×44px circular button.

- **States:**

  **Light & Dark Theme** (accent colors appear theme-invariant):

  | State | Node ID | Background | Background VarID | Border | Shadow | Icon Color | Behavior |
  |---|---|---|---|---|---|---|---|
  | Default | `18603:47849` | `--background/accent` (#0f67ff) | `23879:3183` | None | `Elevation/3` | `--text/overlay` (#fff, `23879:2987`) | Resting state |
  | Hover | `18603:47848` | `--background/accentalt` (#065aec) | `23879:3184` | None | `Elevation/3` | `--text/overlay` (#fff, `23879:2987`) | Darker blue on `:hover` |
  | Pressed | `18603:47847` | `--background/accentalt2` (#024ed3) | `23879:3185` | None | `Elevation/3` | `--text/overlay` (#fff, `23879:2987`) | Darkest blue on `:active`; opens contextual menu |
  | Focus | `18603:47846` | `--background/accentalt` (#065aec) | `23879:3184` | 4px `--border/accentsoft` (#74abff, `23880:1103`), `strokeAlign: OUTSIDE` | `Elevation/3` | `--text/overlay` (#fff, `23879:2987`) | Focus ring for `:focus-visible` |

  > **Theme note:** The FAB button itself uses accent colors that appear to be theme-invariant (same blue in light and dark). The `--text/overlay` (#ffffff) is also invariant. The contextual menu it triggers adapts to theme via `--background/base` and `--text/base`.
  > **Focus = Hover fill:** Both Focus and Hover use `--background/accentalt` (`23879:3184`). Focus additionally gets a 4px OUTSIDE stroke ring.

- **Tokens Used:**
  - **Colors (theme-invariant for button):** `--background/accent`, `--background/accentalt`, `--background/accentalt2`, `--text/overlay`, `--border/accentsoft`
  - **Colors (theme-aware for menu):** `--background/base` (Light: #ffffff / Dark: #252937), `--text/base`, `--text/alt`, `--border/alt2` (Light: #e5e6e9 / Dark: #54565f)
  - **Shadows:** `BoxShadow/Elevation/3` (button), `BoxShadow/Elevation/2` (contextual menu)
  - **Spacing:** `--spacing/4` (menu icon-text gap), `--spacing/8` (menu item py, menu wrapper py), `--spacing/16` (menu item px)
  - **Typography:** `Text Regular/Size 2 (base)` (menu items, 14px), `Text Regular/Size 1 (small)` (menu heading, 12px)

- **Internal Structure (confirmed via dev mode):**

  **Button (all 4 states — identical structure, only fill/stroke changes):**

  ```
  Root (COMPONENT, 44×44px, NO auto-layout — constraints-based)
  ├── Fill: status-specific accent color (boundVariables)
  ├── Stroke: none (Default/Hover/Pressed) or 4px OUTSIDE --border/accentsoft (Focus)
  ├── cornerRadius: 28px (fully circular)
  ├── Effects: 3× DROP_SHADOW (Elevation/3)
  │   ├── Shadow 1: offset(0,14) blur:16 rgba(37,41,55,0.16) showShadowBehindNode:true
  │   ├── Shadow 2: offset(2,0) blur:10 rgba(37,41,55,0.16) showShadowBehindNode:true
  │   └── Shadow 3: offset(0,0) blur:4 rgba(37,41,55,0.08) showShadowBehindNode:false
  └── Grid (INSTANCE, componentId: 29782:5923, 16×16px)
      ├── constraints: { vertical: CENTER, horizontal: CENTER }
      ├── clipsContent: true
      ├── Vector (16×16px, no fill — transparent bounding box)
      └── Vector (10.67×10.67px, fill: --text/overlay #fff, VarID: 23879:2987 — actual glyph)
  ```

  > **Layout note:** FAB does NOT use auto-layout (`layoutMode` absent). Icon centering is via Figma constraints (`CENTER, CENTER`). In CSS, use `display: flex; align-items: center; justify-content: center;` or `display: grid; place-items: center;`.

  **Contextual Menu (child of Pressed variant, `visible: false` by default):**

  ```
  Menu/Example (INSTANCE, componentId: 18756:48876, 231×296px)
  ├── visible: false (toggled by Contextual Menu#29771:0 boolean prop)
  ├── Fill: --background/base (#fff, VarID: 23879:3177)
  ├── cornerRadius: 4px
  ├── layoutMode: VERTICAL
  ├── paddingTop: 8px, paddingBottom: 8px
  ├── counterAxisSizingMode: FIXED (231px width)
  ├── componentProperties: { Type: "Headline", Icon: "True" }
  ├── Effects: 2× DROP_SHADOW (Elevation/2)
  │   ├── Shadow 1: offset(0,4) blur:14 rgba(37,41,55,0.10) showShadowBehindNode:true
  │   └── Shadow 2: offset(0,1) blur:4 rgba(37,41,55,0.23) showShadowBehindNode:true
  ├── Headline (INSTANCE, componentId: 18756:48627, 28px height, layoutAlign: STRETCH)
  ├── Menu/Control ×5 (INSTANCE, componentId: 18756:48260, 36px each, layoutAlign: STRETCH)
  │   ├── layoutMode: HORIZONTAL, counterAxisAlignItems: CENTER
  │   ├── padding: 8px 16px, itemSpacing: 4px
  │   ├── fill: --background/base (23879:3177)
  │   └── componentProperties: { Submenu Icon#29896:0: false, Status: Default, Icon: True }
  ├── Divider (INSTANCE, componentId: 830:495, 8px height, layoutAlign: STRETCH)
  ├── Headline (hidden, visible: false)
  └── Menu/Control ×2 (same as above)
  ```

  > Menu positioned below-left of FAB (absolute offset: ~-175px left, ~60px below button).

- **Accessibility:**
  - Full tab-through support with Enter to activate
  - Visible focus ring: 4px `--border/accentsoft` border
  - Should use `<button>` element with `aria-label` describing the action
  - Contextual menu should use `role="menu"` / `role="menuitem"` pattern
  - Menu should be keyboard navigable (arrow keys)

- **Responsive Behavior:**
  - Fixed size (44×44px), no responsive variants
  - Position is fixed/consistent across all UI screens

- **CSS Implementation Reference:**
  ```
  /* FAB button */
  .fab {
    position: fixed;                /* consistent position across screens */
    width: 44px;
    height: 44px;
    border-radius: 28px;            /* fully circular */
    display: flex;
    align-items: center;
    justify-content: center;        /* constraints CENTER,CENTER → flex centering */
    background: var(--background-accent);
    border: none;
    box-shadow: /* Elevation/3 */
      0px 14px 16px rgba(37,41,55,0.16),
      2px 0px 10px rgba(37,41,55,0.16),
      0px 0px 4px rgba(37,41,55,0.08);
    cursor: pointer;
  }
  .fab:hover {
    background: var(--background-accentalt);
  }
  .fab:active {
    background: var(--background-accentalt2);
  }
  .fab:focus-visible {
    background: var(--background-accentalt);  /* same as hover */
    outline: 4px solid var(--border-accentsoft); /* strokeAlign: OUTSIDE */
    outline-offset: 0;
  }
  .fab__icon {
    width: 16px;
    height: 16px;
    color: var(--text-overlay);     /* #ffffff, theme-invariant */
  }
  /* Contextual menu (positioned below-left of FAB) */
  .fab__menu {
    position: absolute;
    top: 60px;
    left: -175px;                   /* offset from FAB position */
    width: 231px;
    background: var(--background-base);
    border-radius: 4px;
    padding: 8px 0;
    box-shadow: /* Elevation/2 */
      0px 4px 14px rgba(37,41,55,0.10),
      0px 1px 4px rgba(37,41,55,0.23);
  }
  ```

- **Dependencies:**
  - Icons: `Grid` (3×3 dots icon, componentId: `29782:5923`, 16×16px, glyph ~10.67px)
  - Associated: `Menu/Example` (componentId: `18756:48876`) with `Menu/Control` items (`18756:48260`), `Headline` (`18756:48627`), `Divider` (`830:495`)
  - Icons in menu example: `Pause`, `Refresh`, `Edit`, `Notifications`, `externalLink`, `Link`

- **Figma Prop Name Mapping:**
  - `Contextual Menu#29771:0` → `contextualMenu` (boolean, default: false)
  - `Status` → `status` (variant)

- **Icon Sizes:**
  - Grid icon (FAB action icon): **16×16px** inside 44×44px circular container

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** When users need quick access to actions specific to their current page; for actions that users perform regularly throughout their tasks/workflows; to provide a predictable action entry point across all interfaces
  - **Don't use:** For delete, archive, or critical system changes that require careful consideration; when only one action is available; FAB should trigger actions, not navigate between views
  - **Considerations:** Always place it in the same place across all UI
  - **Content:** Use concise action-oriented labels; prioritize quick comprehension
  - **Accessibility:** Full tab-through support with Enter to activate links; use `<button>` with `aria-label`; contextual menu uses `role="menu"` / `role="menuitem"` with keyboard arrow navigation
  - **Structure:** Use icon to make it clear; display options using list; FAB triggers a contextual menu on press, positioned below-left of the button

- **Examples:**
  - Default: Blue circle with grid icon, elevated shadow
  - Pressed with menu: Shows "Group Actions" contextual menu with items: Pause, Scan Now, Settings, Notification Triggers | Open in New Tab, Copy Link (divided into two groups)

### Checkbox

- **Purpose:** Enable users to select one or more options from a set of choices or toggle individual settings on or off.
- **Figma Page:** `• Checkbox` (node `12423:49777`)
- **Figma Component Name:** `Checkbox` (component set `16679:31552`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/checkbox/checkbox.html)

- **Props/API:**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `Status` | `"Default" \| "Hover" \| "Selected" \| "SelectedIndeterminate" \| "Disabled" \| "SelectedDisabled" \| "SelectedIntermediateDisabled" \| "HoverSelected" \| "HoverIndeterminate" \| "Focus"` | `"Default"` | Interactive state of the checkbox |
  | `Device` | `"Desktop" \| "Mobile"` | `"Desktop"` | Device variant — controls touch target sizing |
  | `Label` | `boolean` | `true` | Show or hide the label text |

- **Variants:**
  - **By status:** 10 states covering default, hover, focus, selected, indeterminate, disabled, and combinations
  - **By device:** Desktop (20px height) and Mobile (44px height with 12px vertical padding for touch target)
  - Total: 20 component variants (10 states × 2 devices)

- **States:**

  **Light Theme (Desktop):**

  | State | Box Fill | Box Border | Border Width | Icon | Label Color | CSS Mapping |
  |---|---|---|---|---|---|---|
  | Default | `--background/base` (#ffffff) | `--border/base` (#a4a6af) | 2px | None | `--text/base` (#31343f) | Default state |
  | Hover | `--background/hover` (#f1f1f3) | `--border/base` (#a4a6af) | 2px | None | `--text/base` (#31343f) | `:hover` |
  | Focus | `--background/hover` (#f1f1f3) | `--border/base` (#a4a6af) 2px + `--border/accentsoft` (#74abff) 4px outer | 2px + 4px | None | `--text/base` (#31343f) | `:focus-visible` |
  | Selected | `--background/accent` (#0f67ff) | None | — | Check (white) | `--text/base` (#31343f) | `:checked` |
  | HoverSelected | `--background/accentalt` (#065aec) | None | — | Check (white) | `--text/base` (#31343f) | `:checked:hover` |
  | SelectedIndeterminate | `--background/accent` (#0f67ff) | None | — | Remove/minus (white) | `--text/base` (#31343f) | `:indeterminate` |
  | HoverIndeterminate | `--background/accentalt` (#065aec) | None | — | Remove/minus (white) | `--text/base` (#31343f) | `:indeterminate:hover` |
  | Disabled | `--background/hover` (#f1f1f3) | `--border/alt2` (#e5e6e9) | 2px | None | `--border/base` (#a4a6af) | `:disabled` |
  | SelectedDisabled | `--border/alt2` (#e5e6e9) | None | — | Check (muted) | `--border/base` (#a4a6af) | `:checked:disabled` |
  | SelectedIntermediateDisabled | `--border/alt2` (#e5e6e9) | None | — | Remove/minus (muted) | `--border/base` (#a4a6af) | `:indeterminate:disabled` |

  > **Note:** Disabled states use a dedicated disabled text variable (`VariableID:23879:2980`, #a4a6af — same hex as `--border/base` but **different variable**) for label text, and `--border/alt2` (`VariableID:23880:1100`, #e5e6e9) for fill/border — creating a muted, low-contrast appearance. Icon color in disabled selected states appears muted (same gray family).
  > **Note:** Hover fill (`VariableID:23879:3179`) and Disabled unchecked fill (`VariableID:23879:3182`) share the same hex `#f1f1f3` but are **different Figma variables** — they likely diverge in dark theme.

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--text/base` — Light: `#31343f` — Active label text
    - `--background/base` — Light: `#ffffff` — Default checkbox fill
    - `--background/accent` — Light: `#0f67ff` — Selected/indeterminate fill
    - `--background/accentalt` — Light: `#065aec` — Hover-selected/hover-indeterminate fill
    - `--background/hover` — Light: `#f1f1f3` — Hover/focus/disabled checkbox background
    - `--border/base` — Light: `#a4a6af` — Default checkbox border, disabled label text
    - `--border/alt2` — Light: `#e5e6e9` — Disabled checkbox fill/border
    - `--border/accentsoft` — Light: `#74abff` — Focus ring (4px outer border)
  - **Spacing (theme-invariant):** 8px gap between checkbox and label, 12px vertical padding (Mobile only)
  - **Typography (theme-invariant):** `Text Regular/Size 2 (base)` — Roboto 400, 14px

- **Variant Node IDs (all 20 confirmed via dev mode):**

  | Status | Desktop Node | Mobile Node |
  |---|---|---|
  | Default | `20010:83128` | `30882:40405` |
  | Hover | `20010:83127` | `30882:40408` |
  | Focus | `22713:88046` | `30882:40438` |
  | Selected | `20010:83125` | `30882:40414` |
  | SelectedIndeterminate | `20010:83122` | `30882:40426` |
  | HoverSelected | `20010:83124` | `30882:40418` |
  | HoverIndeterminate | `20010:83121` | `30882:40430` |
  | Disabled | `20010:83126` | `30882:40411` |
  | SelectedDisabled | `20010:83123` | `30882:40422` |
  | SelectedIntermediateDisabled | `20010:83120` | `30882:40434` |

- **Confirmed Variable Bindings (from dev mode):**

  | Element | Token | Hex | Variable ID | States Used |
  |---|---|---|---|---|
  | Box fill | `--background/base` | `#ffffff` | `23879:3177` | Default |
  | Box fill | `--background/hover` | `#f1f1f3` | `23879:3179` | Hover, Focus |
  | Box fill | Disabled fill *(separate var)* | `#f1f1f3` | `23879:3182` | Disabled (same hex as hover!) |
  | Box fill | `--background/accent` | `#0f67ff` | `23879:3183` | Selected, SelectedIndeterminate |
  | Box fill | `--background/accentalt` | `#065aec` | `23879:3184` | HoverSelected, HoverIndeterminate |
  | Box fill | `--border/alt2` *(as fill)* | `#e5e6e9` | `23880:1100` | SelectedDisabled, SelectedIntermediateDisabled |
  | Box stroke | `--border/base` | `#a4a6af` | `23880:1098` | Default, Hover, Focus (inner) |
  | Box stroke | `--border/alt2` | `#e5e6e9` | `23880:1100` | Disabled |
  | Focus ring | `--border/accentsoft` | `#74abff` | `23880:1103` | Focus (outer, 4px OUTSIDE) |
  | Label text | `--text/base` | `#31343f` | `23337:93155` | All non-disabled states |
  | Label text | Disabled text *(separate var)* | `#a4a6af` | `23879:2980` | All disabled states |

  > **Variable pairing insight:** Two pairs share hex values but are separate variables (will likely diverge in dark theme):
  > - Hover fill `23879:3179` ≠ Disabled fill `23879:3182` (both `#f1f1f3`)
  > - Border/base stroke `23880:1098` ≠ Disabled text `23879:2980` (both `#a4a6af`)

- **Internal Structure (confirmed via dev mode — all 20 variants):**

  **Root (consistent across all variants):**
  - `layoutMode: HORIZONTAL`, `itemSpacing: 8`
  - Desktop: no padding → height from content (20px)
  - Mobile: `paddingTop: 12`, `paddingBottom: 12` → 44px total (touch target)
  - No fills or strokes on root component

  **Pattern A — Unchecked (Default, Hover, Disabled):**
  ```
  Root (COMPONENT, HORIZONTAL, itemSpacing:8)
  ├── Checkbox (FRAME, 20×20px, cornerRadius:4)
  │   ├── Fill: state-specific (boundVariables)
  │   ├── Stroke: state-specific, strokeWeight:2, strokeAlign:INSIDE
  │   └── (no children — empty box)
  └── Label (TEXT, "Label", Roboto 400, 14px/20px, --text/base or disabled)
  ```

  **Pattern B — Checked / Indeterminate (Selected, SelectedIndeterminate, HoverSelected, HoverIndeterminate):**
  ```
  Root (COMPONENT, HORIZONTAL, itemSpacing:8)
  ├── Checkbox (FRAME, 20×20px, cornerRadius:4, clipsContent:true)
  │   ├── Fill: accent color (boundVariables), no stroke
  │   └── Check (INSTANCE 303:1431, 16×16px) or Remove (INSTANCE 5901:457, 16×16px)
  │       └── constraints: CENTER or SCALE (both center the 16px icon in 20px box)
  └── Label (TEXT)
  ```

  **Pattern C — Focus (dual-layer for focus ring):**
  ```
  Root (COMPONENT, HORIZONTAL, itemSpacing:8)
  ├── Checkbox (FRAME, 20×20px, cornerRadius:4, clipsContent:true)
  │   ├── No fill
  │   ├── Stroke: --border/accentsoft (#74abff), strokeWeight:4, strokeAlign:OUTSIDE
  │   └── Checkbox (RECTANGLE, 20×20px, cornerRadius:4)
  │       ├── Fill: --background/hover (#f1f1f3, VarID:23879:3179)
  │       └── Stroke: --border/base (#a4a6af, VarID:23880:1098), strokeWeight:2, INSIDE
  └── Label (TEXT)
  ```

  **Pattern D — Disabled Selected (SelectedDisabled, SelectedIntermediateDisabled):**
  ```
  Root (COMPONENT, HORIZONTAL, itemSpacing:8)
  ├── 01-Base/Background (FRAME, 20×20px, cornerRadius:4, clipsContent:true)
  │   ├── Fill: --border/alt2 (#e5e6e9, VarID:23880:1100) — border token reused as fill
  │   ├── No stroke
  │   └── Check (303:1431) or Remove (5901:457), 16×16px, constraints:CENTER
  └── Label (TEXT, disabled color VarID:23879:2980)
  ```

  > **Focus ring approach:** Checkbox uses a dual-layer structure (outer FRAME for focus ring + inner RECTANGLE for checkbox). Unlike FAB (single element with OUTSIDE stroke on same element), Checkbox nests a RECTANGLE inside the focus FRAME. This allows the focus ring (4px OUTSIDE) to wrap around the checkbox border (2px INSIDE) without overlap.
  > **Naming inconsistency:** Box child is named "Checkbox" for most states but "01-Base/Background" for disabled selected states. Functionally identical 20×20 FRAME.
  > **Desktop vs Mobile:** ONLY difference is `paddingTop/Bottom: 12px` on root. All internal structure, tokens, and box dimensions are identical.

- **CSS Implementation Reference:**
  ```
  /* Checkbox root */
  .checkbox {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    gap: 8px;                          /* itemSpacing: 8 */
  }
  .checkbox--mobile {
    padding: 12px 0;                   /* 44px touch target */
  }
  /* Checkbox box */
  .checkbox__box {
    width: 20px;
    height: 20px;
    border-radius: 4px;
    flex-shrink: 0;
    background: var(--background-base);
    border: 2px solid var(--border-base);  /* strokeWeight:2, INSIDE */
  }
  .checkbox__box:hover {
    background: var(--background-hover);   /* 23879:3179 */
  }
  /* Focus — dual-layer in Figma, outline in CSS */
  .checkbox__box:focus-visible {
    background: var(--background-hover);
    border: 2px solid var(--border-base);
    outline: 4px solid var(--border-accentsoft); /* strokeAlign:OUTSIDE, 4px */
    outline-offset: 0;
  }
  /* Selected */
  .checkbox__box:checked {
    background: var(--background-accent);  /* 23879:3183 */
    border: none;
  }
  .checkbox__box:checked:hover {
    background: var(--background-accentalt); /* 23879:3184 */
  }
  /* Disabled */
  .checkbox__box:disabled {
    background: var(--background-disabled);  /* 23879:3182, same hex as hover */
    border: 2px solid var(--border-alt2);    /* 23880:1100 */
  }
  .checkbox__box:checked:disabled,
  .checkbox__box:indeterminate:disabled {
    background: var(--border-alt2);          /* #e5e6e9 reused as fill */
    border: none;
  }
  /* Icon (Check or Remove) */
  .checkbox__icon {
    width: 16px;
    height: 16px;
    /* Centered in 20×20 box via constraints → natural centering with margin:auto or position */
  }
  /* Label */
  .checkbox__label {
    font: 400 14px/20px Roboto;
    color: var(--text-base);               /* 23337:93155 */
  }
  .checkbox:disabled .checkbox__label {
    color: var(--text-disabled);            /* 23879:2980, #a4a6af */
  }
  ```

- **Accessibility:**
  - Minimum 44px touch target on mobile devices (enforced via padding)
  - Keyboard navigation: Tab, Space, and Arrow keys
  - Associate labels with checkboxes using proper markup (`<label>` or `aria-labelledby`)
  - Use `<input type="checkbox">` with `aria-checked` for indeterminate state
  - Screen reader: labels provide actionable context

- **Responsive Behavior:**
  - Desktop: compact 20px height, optimized for pointer interaction
  - Mobile: 44px height with 12px vertical padding for touch accessibility
  - Stack vertically on smaller screens to ensure adequate spacing

- **Dependencies:**
  - Icons: `Check` (checkmark, componentId: `303:1431`, 16×16px), `Remove` (minus/dash, componentId: `5901:457`, 16×16px)

- **Figma Prop Name Mapping (from COMPONENT_SET `16679:31552`):**
  - `Label#30833:0` → `Label` (boolean, default: true) — toggles label text visibility
  - `Status` → `Status` (variant: "Default" | "Hover" | "Selected" | "SelectedIndeterminate" | "Disabled" | "SelectedDisabled" | "SelectedIntermediateDisabled" | "HoverSelected" | "HoverIndeterminate" | "Focus")
  - `Device` → `Device` (variant: "Desktop" | "Mobile")

- **Icon Sizes:**
  - Checkbox box frame: **20×20px**, border-radius: 4px
  - Check glyph: **16×16px** inside 20px box (white fill on accent background)
  - Minus/Remove glyph: **16×16px** inside 20px box (indeterminate state)

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** Use checkboxes when multiple options can be selected from a list; to give users a range of options to choose from; to let users confirm they agree to a policy, service, terms and conditions, or settings; use the indeterminate state for parent items when some child items are selected
  - **Don't use:** For single-choice selections where a radio button would work; for on/off, active/inactive, or yes/no states — use a toggle
  - **Considerations:** Labels should be visible and actionable; selected items are more prominent than unselected items; stack vertically on smaller screens to ensure adequate spacing; mobile requires a bigger padding to provide a minimum 44px hit area for Accessibility; use hints only when you need to provide additional information to the user; use tooltips to provide secondary information not required to complete the checkbox
  - **Content:** Keep it crisp and clear — use concise, scannable labels that clearly describe what will happen when selected; every checkbox should represent a meaningful choice that helps users achieve their goals; use active language and specific terminology
  - **Structure:** Checkbox input (interactive square displaying selection state) + Label (optional descriptive text)

- **Examples (from documentation):**
  - Default unchecked with label: `☐ Enable sensor alerts`
  - Selected with label: `☑ Enable sensor alerts`
  - Variants showcase: shows all 10 states in two columns (Desktop left, Mobile right)

### Contextual Menu

- **Purpose:** Provides quick access to relevant actions and tools for specific elements within the interface. Appears on right-click (desktop) and offers context-specific options that help users perform tasks efficiently without navigating away from their current view.
- **Figma Page:** `• Contextual Menu` (node `6993:539`)
- **Figma Component Names:** `Menu/Control` (atom, component set `18756:48139`), `Action Menu / Device` (`29791:7642`), `Action Menu / Probe` (`29916:10130`), `Action Menu / Group` (`29916:10481`), `Action Menu / Channel` (`29935:4773`), `Action Menu / Submenu` (`29984:5838`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/contextual-menu/contextual-menu.html)

- **Props/API (Menu/Control — atom sub-component):**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `Status` | `"Default" \| "Hover" \| "Pressed" \| "Selected" \| "Focus" \| "Disabled"` | `"Default"` | Interactive state of the menu item |
  | `Icon` | `"False" \| "True"` | `"False"` | Whether to show a leading icon |
  | `Submenu Icon` | `boolean` | `false` | When `true`, shows a ChevronRight arrow indicating a submenu is available |

- **Variants:**
  - **By status:** 6 states — Default, Hover, Pressed, Selected, Focus, Disabled
  - **By icon:** With or without a leading icon
  - Total: 12 atom variants (6 states × 2 icon options)
  - **Composed menus:** 5 pre-built Action Menu components for different entity types (Device, Probe, Group, Channel, Submenu)

- **States (Menu/Control item):**

  **Light Theme:**

  | State | Background | Text Color | Icon Color | Chevron Color | Border | CSS Mapping |
  |---|---|---|---|---|---|---|
  | Default | `--background/base` (#ffffff) | `--text/base` (#31343f) | `--text/alt` (#686b76) | `--border/base` (#a4a6af) | None | Default state |
  | Hover | `--background/hover` (#f1f1f3) | `--text/base` (#31343f) | `--text/alt` (#686b76) | `--text/base` (#31343f) | None | `:hover` |
  | Pressed | `--background/pressed` (#e5e6e9) | `--text/base` (#31343f) | `--text/alt` (#686b76) | `--text/base` (#31343f) | None | `:active` |
  | Selected | `--background/base` (#ffffff) | `--text/accent` (#0f67ff) | `--text/accent` (#0f67ff) | `--text/base` (#31343f) | 4px INSIDE `--border/accent` (#0f67ff) | `aria-checked="true"` |
  | Focus | `--background/hover` (#f1f1f3) | `--text/base` (#31343f) | `--text/alt` (#686b76) | `--text/base` (#31343f) | 4px OUTSIDE `--border/accentsoft` (#74abff) | `:focus-visible` |
  | Disabled | `--background/base` (#ffffff) | Disabled text (#a4a6af) | Disabled text (#a4a6af) | Disabled text (#a4a6af) | None | `aria-disabled="true"` |

  > **Theming note:** The menu item uses CSS variables, so theme switching is automatic. Only the variable definitions change between themes.

  > **Dev-mode confirmed details (2026-03-03):**
  > - **All atom variants** share identical layout: `HORIZONTAL`, `primaryAxisSizingMode: FIXED`, `counterAxisAlignItems: CENTER`, padding 16/16/8/8, gap 4, height 36px
  > - **Selected border** uses `strokeAlign: INSIDE` (VarID `23880:1102` → `--border/accent`). Dev mode shows 4px on all sides; in CSS, implement as `border-left: 4px solid var(--border/accent)` for the left accent bar effect
  > - **Focus border** uses `strokeAlign: OUTSIDE` (VarID `23880:1103` → `--border/accentsoft`). Dev mode shows 4px on all sides outside the box → CSS `outline: 4px solid var(--border/accentsoft)` or `box-shadow`
  > - **Disabled** uses a dedicated text-namespace variable (VarID `23879:2980`, #a4a6af) — NOT `--border/base` despite identical hex. Same-hex/different-variable pattern found in Checkbox; these will likely diverge in dark theme
  > - **Icon default** (non-selected/non-disabled): VarID `23879:2979` → `--text/alt` (#686b76). In Selected state, icon uses `--text/accent` (VarID `23879:2981`). In Disabled, icon uses disabled text variable (`23879:2980`)
  > - **ChevronRight** always `visible: false` in atoms. Toggled via `Submenu Icon#29896:0`. Vector fill: `--text/base` in most states, disabled text in Disabled state
  > - **Composed menus override atom padding**: Atom default is py:8px (36px height), but composed Action Menus override to py:4px (28px height). Implementation should use 4px (the composed value)

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--text/base` — Light: `#31343f` — Menu item text (default/hover/pressed/focus), chevron (hover/pressed/focus/selected)
    - `--text/alt` — Light: `#686b76` — Menu item icon default color, headline group label text
    - `--text/accent` — Light: `#0f67ff` — Selected item text & icon. **VarID: `23879:2981`**
    - `--background/base` — Light: `#ffffff` — Menu container background, default/selected/disabled item background. **VarID: `23879:3177`**
    - `--background/hover` — Light: `#f1f1f3` — Hover and focus item background. **VarID: `23879:3179`**
    - `--background/pressed` — Light: `#e5e6e9` — Pressed item background. **VarID confirmed: `23879:3180`** (separate variable from `--border/alt2` despite same hex in light)
    - `--border/accent` — Light: `#0f67ff` — Selected item left border (4px INSIDE). **VarID: `23880:1102`**
    - `--border/accentsoft` — Light: `#74abff` — Focus ring (4px OUTSIDE). **VarID: `23880:1103`**
    - `--border/alt2` — Light: `#e5e6e9` — Menu divider stroke. **VarID: `23880:1100`**
    - Disabled text — Light: `#a4a6af` — Disabled item text/icon/chevron color. **VarID: `23879:2980`** (text namespace, NOT `--border/base` despite same hex)
  - **Shadows:** `BoxShadow/Elevation/2` (menu container)
  - **Spacing (theme-invariant):** `--spacing/4` (menu container py, icon↔text gap, **composed menu item py override**), `--spacing/8` (menu item py atom default — overridden to 4px in composed menus), `--spacing/16` (menu item px)
  - **Typography (theme-invariant):** `Text Regular/Size 2 (base)` (menu items, 14px/400), `Text Regular/Size 1 (small)` (headline text, 12px/400)

- **Internal Structure (dev-mode confirmed):**

  **Menu Container (Action Menu) — confirmed across all 5 composed variants:**
  ```
  Action Menu / [Variant] (FRAME, VERTICAL auto-layout)
  ├── layoutMode: VERTICAL
  ├── counterAxisSizingMode: FIXED (width: 231px main, 133px submenu)
  ├── paddingTop: 4, paddingBottom: 4 (NO horizontal padding)
  ├── fill: --background/base (VarID:23879:3177) #ffffff
  ├── cornerRadius: 4
  ├── effects: 2× DROP_SHADOW (Elevation/2)
  │
  ├── Title (INSTANCE → 03-Controls/Headline, componentId:18756:48627)
  │   ├── 28px height, wraps Headline sub-frame (componentId:18756:48597)
  │   └── Text: group label (e.g. "Device Actions"), 12px, --text/alt
  │
  ├── Menu/Control (INSTANCE, componentId:18756:48139) ×N
  │   ├── Atom default: py:8px, height 36px
  │   ├── **Composed override: py:4px, height 28px** ← actual implementation value
  │   └── (structure detail below)
  │
  ├── Divider (INSTANCE, componentId:830:495)
  │   ├── stroke VECTOR child with strokeAlign: CENTER
  │   └── stroke: --border/alt2 (VarID:23880:1100) #e5e6e9
  │
  └── [hidden Menu/Control instances and Headline instances]
  ```

  **Menu Item (Menu/Control atom) — 4 structural patterns:**

  **Pattern 1: Default / Hover / Pressed (no border)**
  ```
  Menu/Control (FRAME, HORIZONTAL auto-layout)
  ├── paddingLeft: 16, paddingRight: 16, paddingTop: 8, paddingBottom: 8
  ├── itemSpacing: 4, counterAxisAlignItems: CENTER
  ├── fill: varies by state (see States table)
  ├── strokes: [] (none)
  │
  ├── [Icon] (INSTANCE, 16×16px, visible when Icon=True)
  │   ├── componentId: varies (e.g. Notifications 0:574)
  │   └── Vector fill: --text/alt (VarID:23879:2979) #686b76
  │
  ├── Text (TEXT, layoutGrow: 1)
  │   ├── fontSize: 14, fontWeight: 400, lineHeight: 20px
  │   └── fill: --text/base (VarID:23337:93155) #31343f
  │
  └── ChevronRight (INSTANCE, 20×20px, visible: false)
      ├── componentId: 0:1050
      └── Vector fill: --text/base (VarID:23337:93155)
  ```

  **Pattern 2: Selected (INSIDE border)**
  ```
  Menu/Control (FRAME) — same layout as Pattern 1, plus:
  ├── fill: --background/base (VarID:23879:3177) #ffffff
  ├── stroke: --border/accent (VarID:23880:1102) #0f67ff
  ├── strokeWeight: 4, strokeAlign: INSIDE
  │
  ├── [Icon] Vector fill: --text/accent (VarID:23879:2981) #0f67ff
  ├── Text fill: --text/accent (VarID:23879:2981) #0f67ff
  └── ChevronRight Vector fill: --text/base (VarID:23337:93155)
  ```

  **Pattern 3: Focus (OUTSIDE border)**
  ```
  Menu/Control (FRAME) — same layout as Pattern 1, plus:
  ├── fill: --background/hover (VarID:23879:3179) #f1f1f3
  ├── stroke: --border/accentsoft (VarID:23880:1103) #74abff
  ├── strokeWeight: 4, strokeAlign: OUTSIDE
  │
  ├── [Icon] Vector fill: --text/alt (VarID:23879:2979) #686b76
  ├── Text fill: --text/base (VarID:23337:93155) #31343f
  └── ChevronRight Vector fill: --text/base (VarID:23337:93155)
  ```

  **Pattern 4: Disabled (muted colors, dedicated variable)**
  ```
  Menu/Control (FRAME) — same layout as Pattern 1, plus:
  ├── fill: --background/base (VarID:23879:3177) #ffffff
  ├── strokes: [] (none)
  │
  ├── [Icon] Vector fill: Disabled text (VarID:23879:2980) #a4a6af
  ├── Text fill: Disabled text (VarID:23879:2980) #a4a6af
  └── ChevronRight Vector fill: Disabled text (VarID:23879:2980) #a4a6af
  ```

  **Submenu (Action Menu / Submenu):** Same container structure as main menu but narrower (133px width), positioned adjacent to parent menu. Contains 4 Menu/Control items (Top, Up, Down, Bottom) with directional icons.

- **Composed Action Menu Variants:**

  | Variant | Width | Items | Groups |
  |---|---|---|---|
  | Device | 231px | Pause, Resume, Scan Now, Add Sensor, Settings, Notification Triggers, Delete, Move \| Open in New Tab, Copy Link | 2 (separated by divider) |
  | Probe | 231px | Pause, Scan Now, Add Device, Add Group, Settings, Notification Triggers, Delete, Move \| Open in New Tab, Copy Link | 2 |
  | Group | 231px | Pause, Scan Now, Add Device, Add Group, Settings, Notification Triggers, Delete, Move \| Open in New Tab, Copy Link | 2 |
  | Channel | 231px | Details, Settings, Graphs | 1 (with headline) |
  | Submenu | 133px | Top, Up, Down, Bottom | 1 (used for Move sub-navigation) |

- **Accessibility:**
  - Keyboard navigation: Tab, Arrow keys (up/down), Enter to activate, Escape to close
  - Screen reader: proper ARIA roles (`role="menu"`, `role="menuitem"`) and labels for all items
  - Focus management: clear visual focus indicator (4px `--border/accentsoft` ring) and logical tab order
  - Alternative access: provide keyboard shortcuts or alternative access methods for all contextual actions
  - Disabled options should always make it clear why they're unavailable

- **Responsive Behavior:**
  - Desktop: right-click triggered, positioned near cursor
  - Mobile: implementation should use Sheets component instead (referenced in documentation)
  - Menu automatically repositions to stay within viewport boundaries
  - No explicit size variants — single fixed width (231px for main, 133px for submenu)

- **Dependencies (dev-mode confirmed):**
  - Icons (16×16px): `Notifications` (componentId: `0:574`), `Pause`, `Play Arrow`, `Refresh`, `Add`, `Edit`, `Delete`, `ImportExport`, `externalLink`, `Link`, `EyeOutline`, `ChartAreaspline`, `SortDescending`, `SortAscending`, `ArrowUp`, `ArrowDown`
  - ChevronRight icon (20×20px): componentId `0:1050`, submenu indicator (Container RECTANGLE + Vector glyph ~6.2×10px)
  - `Divider` component: componentId `830:495` (horizontal separator, stroke VECTOR child with `strokeAlign: CENTER`)
  - `03-Controls/Headline`: componentId `18756:48627`, wraps inner Headline `18756:48597` (group label, 12px --text/alt)

- **Figma Prop Name Mapping:**
  - `Submenu Icon#29896:0` → `Submenu Icon` (boolean, default: false)
  - `Status` → `Status` (variant)
  - `Icon` → `Icon` (variant: "False" | "True")

- **Icon Sizes:**
  - Menu item icon (leading): **16×16px** — transparent container FRAME with vector glyph child
  - ChevronRight (submenu indicator): **20×20px** — container FRAME with vector glyph child (~6.2×10px glyph, strokeWeight 0.833)
  - Headline group label: text only, no icon

- **Variant Node IDs (dev-mode confirmed):**

  **Menu/Control Atom Variants (component set `18756:48139`):**

  | Node ID | Status | Icon | Fill VarID | Stroke VarID | StrokeAlign |
  |---|---|---|---|---|---|
  | `18756:48136` | Default | False | `23879:3177` (--background/base) | — | — |
  | `18756:48260` | Default | True | `23879:3177` (--background/base) | — | — |
  | `18756:48133` | Hover | False | `23879:3179` (--background/hover) | — | — |
  | `18756:48259` | Hover | True | `23879:3179` (--background/hover) | — | — |
  | `18756:48132` | Pressed | False | `23879:3180` (--background/pressed) | — | — |
  | `18756:48257` | Pressed | True | `23879:3180` (--background/pressed) | — | — |
  | `18756:48135` | Selected | False | `23879:3177` (--background/base) | `23880:1102` (--border/accent) | INSIDE |
  | `18756:48256` | Selected | True | `23879:3177` (--background/base) | `23880:1102` (--border/accent) | INSIDE |
  | `18756:48134` | Focus | False | `23879:3179` (--background/hover) | `23880:1103` (--border/accentsoft) | OUTSIDE |
  | `18756:48258` | Focus | True | `23879:3179` (--background/hover) | `23880:1103` (--border/accentsoft) | OUTSIDE |
  | `29916:10609` | Disabled | False | `23879:3177` (--background/base) | — | — |
  | `29916:10612` | Disabled | True | `23879:3177` (--background/base) | — | — |

  **Composed Action Menu Variants:**

  | Node ID | Variant | Width | Container Fill VarID |
  |---|---|---|---|
  | `29791:7642` | Device | 231px | `23879:3177` (--background/base) |
  | `29916:10130` | Probe | 231px | `23879:3177` (--background/base) |
  | `29916:10481` | Group | 231px | `23879:3177` (--background/base) |
  | `29935:4773` | Channel | 231px | `23879:3177` (--background/base) |
  | `29984:5838` | Submenu | 133px | `23879:3177` (--background/base) |

- **Confirmed Variable Bindings (from dev mode):**

  | Variable ID | Token | Hex (Light) | Used On |
  |---|---|---|---|
  | `23879:3177` | `--background/base` | `#ffffff` | Container fill, Default/Selected/Disabled item fill |
  | `23879:3179` | `--background/hover` | `#f1f1f3` | Hover & Focus item fill |
  | `23879:3180` | `--background/pressed` | `#e5e6e9` | Pressed item fill |
  | `23337:93155` | `--text/base` | `#31343f` | Default/Hover/Pressed/Focus text, ChevronRight vector (non-disabled) |
  | `23879:2979` | `--text/alt` | `#686b76` | Icon default color (non-selected/non-disabled states) |
  | `23879:2981` | `--text/accent` | `#0f67ff` | Selected text & icon |
  | `23879:2980` | Disabled text | `#a4a6af` | Disabled text, icon, chevron (same hex as `--border/base`, different variable) |
  | `23880:1102` | `--border/accent` | `#0f67ff` | Selected 4px INSIDE stroke |
  | `23880:1103` | `--border/accentsoft` | `#74abff` | Focus 4px OUTSIDE stroke |
  | `23880:1100` | `--border/alt2` | `#e5e6e9` | Divider stroke |

- **CSS Implementation Reference:**
  ```css
  /* Menu Container */
  .contextual-menu {
    display: flex;
    flex-direction: column;
    width: 231px; /* 133px for submenu */
    padding: 4px 0;
    background: var(--background-base);
    border-radius: 4px;
    box-shadow: var(--elevation-2);
  }

  /* Menu Item — actual implementation uses composed 4px padding, not atom 8px */
  .menu-item {
    display: flex;
    align-items: center;
    padding: 4px 16px; /* Composed override: 4px vertical, 16px horizontal */
    gap: 4px;
    height: 28px;
    background: var(--background-base);
    color: var(--text-base);
    cursor: pointer;
  }
  .menu-item:hover { background: var(--background-hover); }
  .menu-item:active { background: var(--background-pressed); }

  /* Selected state — 4px left border accent bar */
  .menu-item[aria-checked="true"] {
    background: var(--background-base);
    border-left: 4px solid var(--border-accent);
    color: var(--text-accent);
    padding-left: 12px; /* Compensate for 4px border */
  }
  .menu-item[aria-checked="true"] .menu-item-icon { color: var(--text-accent); }

  /* Focus state — 4px outside ring */
  .menu-item:focus-visible {
    background: var(--background-hover);
    outline: 4px solid var(--border-accentsoft);
    outline-offset: 0;
  }

  /* Disabled state — dedicated variable, NOT --border/base */
  .menu-item[aria-disabled="true"] {
    background: var(--background-base);
    color: var(--text-disabled); /* VarID:23879:2980, hex same as --border/base in light */
    cursor: default;
    pointer-events: none;
  }

  /* Menu item icon */
  .menu-item-icon {
    width: 16px;
    height: 16px;
    flex-shrink: 0;
    color: var(--text-alt);
  }

  /* Submenu chevron */
  .menu-item-chevron {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
    color: var(--text-base);
  }
  .menu-item[aria-disabled="true"] .menu-item-chevron { color: var(--text-disabled); }

  /* Divider */
  .menu-divider {
    height: 1px;
    margin: 4px 0;
    background: var(--border-alt2);
  }

  /* Headline group label */
  .menu-headline {
    padding: 4px 16px;
    font-size: 12px;
    line-height: 20px;
    color: var(--text-alt);
  }
  ```

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** Quick access to actions related to specific elements; provide secondary/contextual actions; for operations on selected items (lists, tables, visual elements); data manipulation options (copy, export); contextual tools for monitoring elements
  - **Don't use:** For primary actions that should be immediately visible and accessible; when fewer than 3 relevant actions available; for global navigation or application-wide functions; when users expect a dedicated button or control
  - **Considerations:** Desktop triggered by right-click, positioned near cursor; menu automatically repositions to stay within viewport boundaries; on mobile, use Sheet component instead of contextual menu
  - **Content:** Crisp and clear action-oriented labels; use conventional language (e.g. "Copy to Clipboard" rather than "Execute Copy Operation"); use active verbs (Edit, Copy, Delete, Configure); maintain consistency in context terminology
  - **Accessibility:** Keyboard navigation: `Tab` to open, `Arrow Up`/`Arrow Down` to navigate items, `Enter` to activate, `Escape` to close; screen reader: use `role="menu"` on container and `role="menuitem"` on items with proper `aria-label`; focus management: clear 4px `--border/accentsoft` focus ring, logical tab order through items; disabled options should use `aria-disabled="true"` and always make it clear why they are unavailable; alternative access: provide keyboard shortcuts or alternative access methods for all contextual actions
  - **Structure:** Wrapper with shadow (`Elevation/2`) provides elevation; icon container (16×16px) to quickly scan actions; label text for the action name; submenu arrow (ChevronRight 20×20px) when sub-items are available; divider to separate grouped menu items; headline row for group labels; disabled items styled with dedicated disabled text variable (#a4a6af)

- **Examples:**
  - Device context menu: "Device Actions" headline, 10 items in 2 groups (actions | links)
  - Channel context menu: "Channel Actions" headline, 3 items (Details, Settings, Graphs)
  - Submenu for Move: 4 items (Top, Up, Down, Bottom) with directional icons

### CTA Bar

- **Purpose:** Provides a consistent action area at the bottom of interfaces, enabling users to confirm, cancel, or navigate through workflows. Used for multi-step processes, dialogs, and edit workflows.
- **Figma Page:** `• CTA bar` (node `28577:19952`)
- **Figma Component Names:** `CTA bar Desktop` (component set `28692:63771`), `CTA bar Mobile` (component set `28595:115`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/cta-bar/cta-bar.html)

- **Props/API (CTA bar Desktop):**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `State` | `"Enabled" \| "Disabled"` | `"Enabled"` | Controls whether actions are interactive |
  | `Elevation` | `"3" \| "None"` | `"3"` | Shadow elevation — use "3" when fixed on top of scrollable content, "None" for inline |
  | `Padding` | `"32px" \| "16px"` | `"32px"` | Horizontal padding — 32px default, 16px to align with header actions |
  | `Tertiary element` | `"Ghost button" \| "Info text"` | `"Ghost button"` | Left-side element type — ghost button (e.g. Cancel) or informational text (e.g. "7 unsaved changes") |
  | `Info text` | `string (TEXT)` | `"Message"` | Text content for the info message (when Tertiary element = Info text) |
  | `Tertiary` | `boolean` | `true` | Show/hide the tertiary element (ghost button or info text) |
  | `Secondary` | `boolean` | `true` | Show/hide the secondary button |
  | `Primary` | `INSTANCE_SWAP` | `Small/Primary` | Swappable primary button — can use Primary or Danger button variants |

- **Props/API (CTA bar Mobile):**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `State` | `"Enabled" \| "Disabled"` | `"Enabled"` | Controls whether actions are interactive |
  | `Elevation` | `"3" \| "None"` | `"3"` | Shadow elevation |
  | `Tertiary element` | `"Ghost button" \| "Info text"` | `"Ghost button"` | Top element type |
  | `Info text` | `string (TEXT)` | `"Message"` | Text content for the info message |
  | `Secondary` | `boolean` | `true` | Show/hide the secondary button |
  | `Tertiary` | `boolean` | `true` | Show/hide the tertiary element |
  | `Primary` | `INSTANCE_SWAP` | `Small/Primary` | Swappable primary button |

  > **Note:** Mobile has no `Padding` prop — always uses 16px.

- **Variants:**
  - **Desktop:** 16 variants (2 states × 2 elevations × 2 paddings × 2 tertiary element types)
  - **Mobile:** 8 variants (2 states × 2 elevations × 2 tertiary element types)
  - Total: 24 component variants

- **States:**

  **Enabled:**

  | Element | Background | Text Color | Notes |
  |---|---|---|---|
  | Container | `--background/base` (#ffffff) | — | White background |
  | Primary button | `--background/accent` (#0f67ff) | `--text/overlay` (#ffffff) | Blue filled button |
  | Secondary button | `--background/hover` (#f1f1f3) | `--text/base` (#31343f) | Gray filled button |
  | Ghost button | transparent | `--text/base` (#31343f) | Text-only button |
  | Info text | — | `--text/base` (#31343f) | Bold info message |

  **Disabled:**

  | Element | Background | Text Color | Notes |
  |---|---|---|---|
  | Container | `--background/base` (#ffffff) | — | Same white background |
  | Primary button | Disabled primary fill (#74abff) | `--text/overlay` (#ffffff) at 60% opacity | Muted blue, faded text |
  | Secondary button | `--background/hover` (#f1f1f3) | Disabled text (#a4a6af) | Same gray bg, muted text |
  | Ghost button | transparent | Disabled text (#a4a6af) | Muted text |
  | Info text | — | Disabled text (#a4a6af) | **Muted in disabled state** (not same as enabled) |

  > **Theming note:** Button colors use the same tokens as elsewhere. The disabled primary fill uses VarID `23879:3186` (#74abff) — a **separate background-namespace variable** from `--border/accentsoft` (`23880:1103`) despite identical hex. These will likely diverge in dark theme. Disabled text uses VarID `23879:2980` (#a4a6af) — the same dedicated disabled text variable used across other components.

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--text/base` — Light: `#31343f` — Ghost/secondary button text (enabled), info text
    - `--text/overlay` — `#ffffff` — Primary button text (theme-invariant)
    - `--background/base` — Light: `#ffffff` — CTA bar container background
    - `--background/accent` — `#0f67ff` — Primary button fill (enabled)
    - `--background/hover` — Light: `#f1f1f3` — Secondary button fill
    - Disabled text — Light: `#a4a6af` — Disabled ghost/secondary/info text color. **VarID: `23879:2980`** (text namespace, NOT `--border/base` despite same hex)
    - Disabled primary fill — Light: `#74abff` — Disabled primary button fill. **VarID: `23879:3186`** (background namespace, NOT `--border/accentsoft` `23880:1103` despite same hex)
  - **Shadows:** `BoxShadow/Elevation/3` (when Elevation="3") — 3-layer DROP_SHADOW: `0 14px 16px rgba(37,41,55,0.16)`, `2px 0 10px rgba(37,41,55,0.16)`, `0 0 4px rgba(37,41,55,0.08)`
  - **Spacing (theme-invariant):**
    - `--spacing/8` (8px) — gap between stacked buttons (mobile), gap between secondary and primary buttons (desktop)
    - `--spacing/10` (10px) — gap between tertiary element and button group (desktop), button internal padding gap
    - `--spacing/16` (16px) — CTA bar mobile padding (all sides), CTA bar desktop horizontal padding (compact)
    - `--spacing/20` (20px) — button horizontal padding (all Small buttons)
    - `--spacing/24` (24px) — CTA bar vertical padding (top/bottom, both desktop and mobile desktop)
    - `--spacing/32` (32px) — CTA bar desktop horizontal padding (default)
  - **Typography (theme-invariant):** `Text Bold/Size 2 (base)` — Roboto 700, 14px, letter-spacing 0.28px — all button labels and info text
  - **Border Radius:** `4px` — all buttons (Primary, Secondary, Ghost)

- **Internal Structure (dev-mode confirmed):**

  **Desktop variant:**
  ```
  CTA bar Desktop (FRAME, HORIZONTAL auto-layout)
  ├── layoutMode: HORIZONTAL
  ├── primaryAxisSizingMode: FIXED, counterAxisSizingMode: FIXED
  ├── width: 800px, height: 84px
  ├── counterAxisAlignItems: CENTER (vertical centering)
  ├── primaryAxisAlignItems: MAX (right-align button group)
  ├── paddingLeft: 32|16 (by Padding prop), paddingRight: 32|16
  ├── paddingTop: 24, paddingBottom: 24
  ├── itemSpacing: 10
  ├── fill: --background/base (VarID:23879:3177) #ffffff
  ├── effects: [Elevation/3 × 3 shadows] or [] (by Elevation prop)
  │
  ├── [Tertiary: Ghost button] Small/Ghost (INSTANCE)
  │   ├── componentId: 19905:79550 (Enabled) | 19905:79540 (Disabled)
  │   ├── fills: [] (transparent)
  │   ├── layoutAlign: INHERIT
  │   └── componentProperties: Type="OnlyText", Status="Default"|"Disabled"
  │
  ├── [Tertiary: Info text] Changes (TEXT)
  │   ├── Enabled fill: --text/base (VarID:23337:93155) #31343f
  │   ├── Disabled fill: Disabled text (VarID:23879:2980) #a4a6af
  │   ├── fontWeight: 700, fontSize: 14, letterSpacing: 0.28
  │   ├── textAutoResize: WIDTH_AND_HEIGHT
  │   └── layoutAlign: INHERIT
  │
  └── Button group (FRAME)
      ├── layoutGrow: 1 (flex: 1 — absorbs remaining width)
      ├── layoutMode: HORIZONTAL, primaryAxisAlignItems: MAX
      ├── counterAxisAlignItems: CENTER, itemSpacing: 8
      ├── clipsContent: true
      ├── [Small/Secondary] (optional, via Secondary boolean)
      └── [Small/Primary] (swappable via INSTANCE_SWAP)
  ```

  **Mobile variant:**
  ```
  CTA bar Mobile (FRAME, VERTICAL auto-layout)
  ├── layoutMode: VERTICAL
  ├── counterAxisSizingMode: FIXED (width: 375px)
  ├── primaryAxisAlignItems: CENTER
  ├── counterAxisAlignItems: MAX (overridden by children's STRETCH)
  ├── padding: 16px all sides
  ├── itemSpacing: 8
  ├── fill: --background/base (VarID:23879:3177) #ffffff
  ├── effects: [Elevation/3 × 3 shadows] or [] (by Elevation prop)
  ├── constraints: vertical: BOTTOM, horizontal: CENTER
  │
  ├── [Tertiary: Ghost button] Small/Ghost (INSTANCE, layoutAlign: STRETCH)
  │   └── componentId: 19905:79550 (Enabled) | 19905:79540 (Disabled)
  │
  ├── [Tertiary: Info text] Message (TEXT, layoutAlign: STRETCH)
  │   ├── Enabled fill: --text/base (VarID:23337:93155)
  │   ├── Disabled fill: Disabled text (VarID:23879:2980)
  │   ├── textAlignHorizontal: CENTER
  │   └── textAutoResize: HEIGHT (STRETCH handles width)
  │
  ├── Small/Secondary (INSTANCE, layoutAlign: STRETCH)
  │   ├── componentId: 19905:79020 (Enabled) | 19905:78978 (Disabled)
  │   └── fill: --background/hover (VarID:23879:3179) #f1f1f3
  │
  └── Small/Primary (INSTANCE, layoutAlign: STRETCH)
      ├── componentId: 19902:80389 (Enabled) | 19902:80324 (Disabled)
      ├── Enabled fill: --background/accent (VarID:23879:3183) #0f67ff
      └── Disabled fill: Disabled primary fill (VarID:23879:3186) #74abff
  ```

  **Button sizing (Small — confirmed across all button instances):**
  - Height: 36px
  - Padding: `px: 20px`, `py: 10px`
  - Corner radius: 4px
  - Font: Roboto Bold 700, 14px, letter-spacing 0.28px, center-aligned
  - layout: HORIZONTAL, primaryAxisAlignItems: CENTER, counterAxisAlignItems: CENTER

- **Accessibility:**
  - Full tab-through support with Enter to confirm and Escape to cancel
  - Touch targets for mobile: minimum 44×44px (buttons are 36px tall but full-width provides adequate tap area)
  - Always provide at least one enabled action — never trap users without an exit
  - Use danger styling for destructive/irreversible actions paired with cancel option

- **Responsive Behavior:**
  - **Desktop:** Horizontal layout, elements in a single row. Tertiary left-aligned, buttons right-aligned.
  - **Mobile:** Vertical stack, full-width buttons, 16px padding. Primary button at bottom for easy thumb reach. 8px gap between stacked buttons.
  - No `Padding` prop on Mobile — always 16px.

- **Dependencies (dev-mode confirmed):**
  - `Small/Primary`: componentId `19902:80389` (Enabled), `19902:80324` (Disabled) — fill `--background/accent` (Enabled) / Disabled primary fill VarID `23879:3186` (Disabled)
  - `Small/Secondary`: componentId `19905:79020` (Enabled), `19905:78978` (Disabled) — fill `--background/hover` (both states)
  - `Small/Ghost`: componentId `19905:79550` (Enabled), `19905:79540` (Disabled) — transparent (no fills)
  - `Small/Danger`: available via INSTANCE_SWAP (from `• Buttons` page)
  - The `Primary` prop uses `INSTANCE_SWAP` — default `19902:80389`, preferredValues include Primary and Danger component sets

- **Figma Prop Name Mapping (dev-mode confirmed):**
  - **Desktop (`28692:63771`):**
    - `Info text#31271:0` → `Info text` (TEXT, default "Message")
    - `Tertiary#31271:6` → `Tertiary` (BOOLEAN, default true)
    - `Secondary#31271:12` → `Secondary` (BOOLEAN, default true)
    - `Primary#31271:18` → `Primary` (INSTANCE_SWAP, default `19902:80389`)
    - `State` → variant: "Enabled" | "Disabled"
    - `Elevation` → variant: "3" | "None"
    - `Padding` → variant: "32px" | "16px"
    - `Tertiary element` → variant: "Ghost button" | "Info text"
  - **Mobile (`28595:115`):**
    - `Info text#31278:0` → `Info text` (TEXT, default "Message")
    - `Secondary#31278:4` → `Secondary` (BOOLEAN, default true)
    - `Tertiary#31278:9` → `Tertiary` (BOOLEAN, default true)
    - `Primary#31278:14` → `Primary` (INSTANCE_SWAP, default `19902:80389`)
    - `State` → variant: "Enabled" | "Disabled"
    - `Elevation` → variant: "3" | "None"
    - `Tertiary element` → variant: "Ghost button" | "Info text"
    - *(No `Padding` prop — always 16px)*

- **Variant Node IDs (dev-mode confirmed):**

  **Desktop (component set `28692:63771`) — 16 variants:**

  | Node ID | State | Elevation | Padding | Tertiary Element |
  |---|---|---|---|---|
  | `28692:63772` | Enabled | 3 | 32px | Ghost button |
  | `31271:8531` | Enabled | 3 | 16px | Ghost button |
  | `28692:63777` | Enabled | None | 32px | Ghost button |
  | `31271:8536` | Enabled | None | 16px | Ghost button |
  | `28692:63791` | Disabled | 3 | 32px | Ghost button |
  | `31271:8541` | Disabled | 3 | 16px | Ghost button |
  | `28692:63798` | Disabled | None | 32px | Ghost button |
  | `31271:8546` | Disabled | None | 16px | Ghost button |
  | `28692:63805` | Enabled | 3 | 32px | Info text |
  | `31271:8551` | Enabled | 3 | 16px | Info text |
  | `31271:8438` | Enabled | None | 32px | Info text |
  | `31271:8566` | Enabled | None | 16px | Info text |
  | `31271:8445` | Disabled | 3 | 32px | Info text |
  | `31271:8556` | Disabled | 3 | 16px | Info text |
  | `31271:8464` | Disabled | None | 32px | Info text |
  | `31271:8561` | Disabled | None | 16px | Info text |

  **Mobile (component set `28595:115`) — 8 variants:**

  | Node ID | State | Elevation | Tertiary Element |
  |---|---|---|---|
  | `28595:130` | Enabled | 3 | Ghost button |
  | `28595:116` | Enabled | None | Ghost button |
  | `31278:3170` | Disabled | 3 | Ghost button |
  | `31278:3166` | Disabled | None | Ghost button |
  | `31271:8712` | Enabled | 3 | Info text |
  | `31278:3136` | Enabled | None | Info text |
  | `31278:3192` | Disabled | 3 | Info text |
  | `31278:3174` | Disabled | None | Info text |

- **Confirmed Variable Bindings (from dev mode):**

  | Variable ID | Token | Hex (Light) | Used On |
  |---|---|---|---|
  | `23879:3177` | `--background/base` | `#ffffff` | CTA bar container fill (all variants) |
  | `23337:93155` | `--text/base` | `#31343f` | Info text (Enabled state) |
  | `23879:2980` | Disabled text | `#a4a6af` | Info text (Disabled state), ghost/secondary button text (Disabled) |
  | `23879:3183` | `--background/accent` | `#0f67ff` | Primary button fill (Enabled) |
  | `23879:3186` | Disabled primary fill | `#74abff` | Primary button fill (Disabled) — **NOT** `--border/accentsoft` despite same hex |
  | `23879:3179` | `--background/hover` | `#f1f1f3` | Secondary button fill (both Enabled & Disabled) |

- **CSS Implementation Reference:**
  ```css
  /* CTA Bar — Desktop */
  .cta-bar-desktop {
    display: flex;
    align-items: center;
    justify-content: flex-end; /* primaryAxisAlignItems: MAX */
    width: 100%;
    height: 84px;
    padding: 24px 32px; /* or 24px 16px for compact */
    gap: 10px;
    background: var(--background-base);
  }
  .cta-bar-desktop.elevated {
    box-shadow:
      0 14px 16px rgba(37, 41, 55, 0.16),
      2px 0 10px rgba(37, 41, 55, 0.16),
      0 0 4px rgba(37, 41, 55, 0.08);
  }

  /* Button group — right-aligned via flex:1 */
  .cta-bar-desktop .button-group {
    flex: 1;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 8px;
  }

  /* CTA Bar — Mobile */
  .cta-bar-mobile {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    width: 100%;
    padding: 16px;
    gap: 8px;
    background: var(--background-base);
  }
  .cta-bar-mobile.elevated {
    box-shadow:
      0 14px 16px rgba(37, 41, 55, 0.16),
      2px 0 10px rgba(37, 41, 55, 0.16),
      0 0 4px rgba(37, 41, 55, 0.08);
  }

  /* All Small buttons */
  .btn-small {
    height: 36px;
    padding: 10px 20px;
    border-radius: 4px;
    font: 700 14px/16px 'Roboto', sans-serif;
    letter-spacing: 0.28px;
    text-align: center;
  }
  .btn-primary { background: var(--background-accent); color: var(--text-overlay); }
  .btn-primary:disabled { background: var(--background-accent-disabled); } /* VarID:23879:3186 */
  .btn-secondary { background: var(--background-hover); color: var(--text-base); }
  .btn-ghost { background: transparent; color: var(--text-base); }
  .btn-small:disabled { color: var(--text-disabled); } /* VarID:23879:2980 */

  /* Info text */
  .cta-info-text {
    font: 700 14px/16px 'Roboto', sans-serif;
    letter-spacing: 0.28px;
    color: var(--text-base);
  }
  .cta-bar-desktop .cta-info-text { white-space: nowrap; } /* WIDTH_AND_HEIGHT */
  .cta-bar-mobile .cta-info-text { text-align: center; width: 100%; } /* STRETCH + CENTER */
  .cta-bar[aria-disabled="true"] .cta-info-text { color: var(--text-disabled); }
  ```

  > **Dev-mode note (2026-03-03):** 2 of 16 Desktop variants (Enabled + Elevation=None + Ghost button) use `SPACE_BETWEEN` with `itemSpacing: 579` instead of `MAX` with `itemSpacing: 10`. Both achieve identical visual results (tertiary left, buttons right). Implementation should use `justify-content: space-between` or `flex: 1` on button group — either works.

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** Multi-step processes requiring navigation/confirmation (onboarding, setup wizard); dialogs requiring confirmation or cancellation; edit workflows where users save or discard changes
  - **Don't use:** For inline actions within content (use standard buttons); when only a single action is needed without confirmation; for read-only views without user interaction
  - **Considerations:** Always position at bottom of container; use 32px padding by default, 16px to align with header actions; add elevation (`Elevation/3`) when fixed on top of scrollable content, "None" for inline; primary button should always carry highest emphasis; use danger styling for destructive/irreversible actions (e.g. delete account, discard unsaved work) paired with cancel option; always provide at least one enabled action — never trap users without an exit; use info message (Tertiary element = "Info text") to provide context (e.g. "7 unsaved changes")
  - **Content:** Concise action-oriented labels under 3 words with active verbs (Save, Confirm, Next, Back, Discard); keep info messages clear and brief; maintain consistent terminology
  - **Accessibility:** Full tab-through support with `Enter` to confirm and `Escape` to cancel; touch targets for mobile: minimum 44×44px (buttons are 36px tall but full-width provides adequate tap area); danger actions must be paired with a cancel option
  - **Structure (Desktop):** Horizontal arrangement, single row. Order left→right: Tertiary element (optional), Secondary button (optional), Primary button. Tertiary left-aligned, buttons right-aligned (via `flex: 1` spacer on button group `FRAME`). Padding: 32px default, 16px to align with header.
  - **Structure (Mobile):** Vertical stack, full-width elements (`layoutAlign: STRETCH`), 16px container padding. Order top→bottom: Tertiary element (optional), Secondary button, Primary button. Primary at bottom for thumb reach. 8px gap between stacked buttons. No `Padding` prop — always 16px. Mobile constraints: `vertical: BOTTOM, horizontal: CENTER`.

- **Examples:**
  - Navigation flow: `Cancel | [spacer] | Back | Next` (Next = Primary blue)
  - Save flow with info: `Message | [spacer] | Cancel | Save` (Save = Primary blue)
  - Destructive flow: `Cancel | [spacer] | Back | Delete` (Delete = Danger red)
  - Mobile stack: Cancel (ghost, top) → Back (secondary) → Next (primary, bottom)

### Empty State

- **Purpose:** Provides a meaningful user experience when there is no content to display within a container, view, or data set. Informs users the empty state is intentional, guides them toward appropriate next actions, and maintains confidence in the system's functionality.
- **Figma Page:** `• Empty State` (node `30058:1185`)
- **Figma Component Name:** `Empty State` (component set `30058:1967`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/empty-state/empty-state.html)

- **Props/API:**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `Type` | `"Content" \| "Search"` | `"Content"` | Context of the empty state — content area has no items, or search/filter returned no results |
  | `Subtitle` | `boolean` | `true` | Show/hide the secondary message text |
  | `Button` | `boolean` | `true` | Show/hide the action button |

- **Variants:**
  - **Type=Content:** General empty state — container/view/collection has no items. Uses sad face illustration, title like "This group has no devices.", action like "+ Add device"
  - **Type=Search:** Search/filter empty state — no results match criteria. Uses search/magnifying glass illustration, title like "No matching results.", action like "Reset all"
  - Total: 2 component variants

- **Visual Design:**

  | Element | Color Token | Font | Notes |
  |---|---|---|---|
  | Illustration circle | `--background/hover` (#f1f1f3) | — | 200×200px circle background |
  | Primary message (title) | `--text/base` (#31343f) | `Text Medium/Size 4 Medium` (Roboto 500, 20px) | Center-aligned |
  | Secondary message (subtitle) | `--text/base` (#31343f) | `Text Regular/Size 2 (base)` (Roboto 400, 14px) | Center-aligned |
  | Action button (Secondary) | `--background/hover` (#f1f1f3) fill, `--text/base` (#31343f) text | `Text Bold/Size 2 (base)` (Roboto 700, 14px, ls: 0.28px) | With leading icon |

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--text/base` — Light: `#31343f` — Primary message, secondary message, button text
    - `--background/hover` — Light: `#f1f1f3` — Illustration circle background, secondary button fill
  - **Spacing (theme-invariant):**
    - `--spacing/16` (16px) — Component padding (all sides), gap between illustration/message/button
    - `--spacing/8` (8px) — Gap between primary and secondary message within Message Container
    - `--spacing/4` (4px) — Button icon↔text gap
  - **Typography (theme-invariant):**
    - `Text Medium/Size 4 Medium` — Roboto 500, 20px — primary message title
    - `Text Regular/Size 2 (base)` — Roboto 400, 14px — secondary message subtitle
    - `Text Bold/Size 2 (base)` — Roboto 700, 14px, letter-spacing 0.28px — button label
  - **Border Radius:** `4px` — action button

- **Internal Structure:**
  - Root: `VERTICAL` auto-layout, `FIXED` width (408px) × `HUG` height (356px with all elements)
  - Padding: `16px` all sides
  - Gap: `16px` between children
  - Alignment: center-aligned horizontally (text center, illustration and button centered)
  - Children:
    1. **Illustration frame:** 200×200px FIXED
       - Circle background vector (`Ellipse 2.1`): 200×200px, `--background/hover` (#f1f1f3)
       - Content variant: `404_face02` group (sad face page illustration)
       - Search variant: `Search Icon` frame (150×150px magnifying glass, padded 25px inside container)
    2. **Message Container:** FILL width × HUG height, `VERTICAL`, gap `8px`
       - "Primary Message" text: FILL width, 20px Medium, center
       - "Secondary Message" text: FILL width, 14px Regular, center (optional via `Subtitle` prop)
    3. **Small/Secondary button:** HUG × HUG (optional via `Button` prop)
       - Icon-prefixed variant: `paddingLeft: 12px`, `paddingRight: 20px`, `paddingTop: 6px`, `paddingBottom: 6px`
       - Icon: 24×24px (Add icon for Content, ResetFilter icon for Search)
       - Gap: 4px between icon and label
       - Height: 36px

- **Button Variant Note (icon-prefixed):**
  The button used here is `Small/Secondary` with a leading icon. Its padding differs from the text-only buttons in CTA Bar:
  - **Text-only:** `px: 20px`, `py: 10px`, gap: `10px`
  - **With icon:** `pl: 12px`, `pr: 20px`, `py: 6px`, icon: 24×24px, gap: `4px`
  - Both maintain consistent 36px total height.

- **Accessibility:**
  - Full tab-through support with Enter to activate action button/links
  - Illustration is decorative — should be `aria-hidden="true"` or have empty alt text
  - Title should be semantically meaningful heading for screen readers

- **Responsive Behavior:**
  - Fixed width (408px), height adapts to content (HUG)
  - Illustrations scale appropriately across screen sizes
  - No explicit breakpoint variants — component is designed to center within available space

- **Dependencies:**
  - Illustrations: `404_face02` (sad face page), `Search Icon` (magnifying glass) — both rendered within 200×200px circle
  - Icons: `Add` (24×24px, for Content variant), `ResetFilter` (24×24px, for Search variant)
  - Buttons: `Small/Secondary` (with icon variant)

- **Figma Prop Name Mapping:**
  - `Type` → `Type` (variant: "Content" | "Search")
  - `Subtitle` → `Subtitle` (boolean, default: true)
  - `Button` → `Button` (boolean, default: true)

- **Icon Sizes:**
  - Action button icon (Add / ResetFilter): **24×24px** — leading icon inside `Small/Secondary` button
  - Illustration circle: **200×200px** — decorative, `aria-hidden="true"`

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** User views sensors/devices/probes/data collections with no items; search returns no results; filter combination yields no matches; initial onboarding with no content created yet; deletion left a collection empty; users cleared/deleted all items
  - **Don't use:** For loading states (use loading indicators); when content temporarily unavailable due to connectivity; as replacement for error messages; when empty state would interfere with critical system information
  - **Considerations:** Illustrations should scale appropriately across screen sizes; each screen should remain readable on multiple resolutions; button should be relevant and actionable; for disabled button status, always explain what users need to do to enable the action (e.g. "You do not have permission to add devices"); component centers within available space (fixed 408px width)
  - **Content:** Use simple, understandable language that gets to the point quickly. Write for scanning first, reading second. Maintain informal, conversational tone. Match user's mental model. Begin with context in primary message (e.g. "This group has no devices."), put guidance in subtitle and action in button. Keep concise (1-2 lines). Clearly state what is empty (e.g. "No sensors found", "No matching results."). Use placeholder-style copy that adapts to context.
  - **Accessibility:** Illustration is decorative — use `aria-hidden="true"` or empty alt text; title should be semantically meaningful heading for screen readers; full tab-through support with `Enter` to activate action button
  - **Structure:** Illustration (optional, decorative visual reinforcing empty state — 200×200px circle with icon); Title (required, concise headline explaining why content is empty — `Text Medium/Size 4 Medium` 20px); Subtitle (optional, additional context or guidance — `Text Regular/Size 2` 14px); Secondary Action Button (optional, main action to resolve the empty state — `Small/Secondary` with 24×24px leading icon)

- **Examples:**
  - Content: Sad face illustration → "This group has no devices." → "You do not have permission to add devices." → `[+ Add device]`
  - Search: Magnifying glass illustration → "No matching results." → "Refine your search and try again." → `[⊘ Reset all]`

### Footer

- **Purpose:** Displays persistent system information, status, and branding at the bottom of desktop interfaces. Provides real-time refresh controls, version info, user identity, and copyright.
- **Figma Page:** `• Footer` (node `11651:35322`)
- **Figma Component Name:** `Footer` (single component `29660:1701`, not a component set)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/footer/footer.html)

- **Props/API:**
  - No variant props — single fixed component
  - Content is configured by populating the child text elements and swapping icons

- **Variants:** None — single component, desktop-only.

- **Visual Design:**

  | Element | Color Token | Font | Notes |
  |---|---|---|---|
  | Background | `--background/body` (#f9f9fa) | — | Variable binding confirmed: `VariableID:23879:3178` |
  | Separator line | `--border/alt2` (#e5e6e9) | — | 1px horizontal line at top |
  | All text (version, timer, user, copyright) | `--border/base` (#a4a6af) | `Text Regular/Size 2 (base)` (Roboto 400, 14px) | Intentionally muted to avoid competing with main content |
  | Logo | — | — | `Brand/Paessler/Small` instance, 95×12px |

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--background/body` — Light: `#f9f9fa` — Footer background (**first confirmed variable binding**: `VariableID:23879:3178`)
    - `--border/alt2` — Light: `#e5e6e9` — Top separator line (1px stroke)
    - `--border/base` — Light: `#a4a6af` — All footer text (muted/tertiary appearance)
  - **Spacing (theme-invariant):**
    - `--spacing/4` (4px) — Gap between separator and content, gap between refresh control icons/text
    - `--spacing/8` (8px) — Content row vertical padding
    - `--spacing/16` (16px) — Content row horizontal padding
  - **Typography (theme-invariant):** `Text Regular/Size 2 (base)` — Roboto 400, 14px — all footer text

- **Internal Structure:**
  - Root: `VERTICAL` auto-layout, `FIXED` width (1354px) × `HUG` height (40px)
  - Background: `--background/body` (#f9f9fa)
  - Gap: `4px` between separator and content row
  - Children:
    1. **Separator** (LINE): FILL width, 1px stroke `--border/alt2`
    2. **Frame 3** (content row): FILL width × HUG height (36px), `HORIZONTAL`
       - Padding: `px: 16px`, `py: 8px`
       - Gap: `188px` (large fixed spacing — implements space-between via Figma auto-layout)
       - Children (left to right):
         a. **Brand/Paessler/Small** (logo): FILL width (95px) × 12px — logo component instance
         b. **Version text**: HUG, "25.4.113.1073+ [Canary]"
         c. **Frame 1** (refresh controls): HUG × HUG (170×20px), HORIZONTAL, gap 4px — contains Refresh icon + Pause icon + timer text ("Refresh in 06 seconds")
         d. **User text**: HUG, "admin"
         e. **Copyright text**: FIXED width, "© 2025 Paessler GmbH"

- **Accessibility:**
  - Keyboard navigation support with visible focus indicators
  - Refresh and pause buttons have descriptive ARIA attributes
  - Cursor changes to pointer for all interactive elements
  - Logo link displays tooltip with destination information on hover

- **Responsive Behavior:**
  - **Desktop only** — not for mobile viewports
  - Always positioned at the absolute bottom of the viewport
  - Full-width, content spread horizontally

- **Dependencies:**
  - Brands: `Brand/Paessler/Small` (logo component, 95×12px)
  - Icons: `Refresh` (refresh/rotate icon), `Pause` (pause icon)

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** Standard component for all desktop interfaces; when persistent system status and branding need visibility; when real-time information and refresh controls must remain accessible
  - **Don't use:** On mobile viewports (desktop-only component); when system information isn't relevant to the user's context
  - **Considerations:** Always position at the absolute bottom of the viewport; maintain visual hierarchy with subtle styling (`--border/base` muted text) to avoid competing with main content; refresh and pause actions should provide immediate visual feedback; cursor changes to pointer for all interactive elements; logo link displays tooltip with destination information on hover
  - **Content:** Keep text concise and scannable; display timer in consistent format (e.g. "Refresh in 12 seconds"); version format includes build number and channel tag
  - **Accessibility:** Keyboard navigation support with visible focus indicators; refresh and pause buttons have descriptive ARIA attributes (`aria-label`); logo link is keyboard-accessible
  - **Structure:** Horizontal arrangement with all five elements in a single row: Logo (95×12px) | Version text | Refresh controls (↻ ⏸ + timer) | User identity | Copyright. Separated from content by 1px `--border/alt2` line. Content row uses `HORIZONTAL` layout with `px: 16px`, `py: 8px`. Large `itemSpacing` (188px) implements `justify-content: space-between`.

- **Examples:**
  - `[PAESSLER logo] | 25.4.113.1073+ [Canary] | ↻ ⏸ Refresh in 06 seconds | admin | © 2025 Paessler GmbH`

### Sheet (Mobile)

- **Purpose:** Serves as the mobile replacement for traditional contextual menus. Provides device-specific options and displays relevant information in a touch-friendly format that preserves the monitoring context while offering quick access to actions and details. Exclusively for mobile experiences.
- **Figma Page:** `• Sheets (mobile)` (node `12470:0`)
- **Figma Component Names:** 4 individual COMPONENT nodes (not a component set):
  - `Sheets/Mobile/Base` (`12471:120`) — Base container shape
  - `Sheets/Mobile/Objects Selected` (`29946:3407`) — Bulk action list
  - `Sheets/Mobile/Sensor` (`29984:5904`) — Grouped entity actions
  - `Sheets/Mobile/Submenu` (`29984:6753`) — Submenu with back navigation
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/sheets-mobile/sheets-mobile.html)
- **Desktop counterpart:** Contextual Menu (use traditional contextual menus on desktop)

- **Props/API:**
  - No variant props — each use case is a separate component
  - Content is configured by composing `Menu/Control` instances and group headers inside the Menu frame

- **Variants:**

  | Variant | Node ID | Dimensions | Description |
  |---|---|---|---|
  | Base | `12471:120` | 375×368px | White container shape with top-rounded corners; used as instance inside other variants |
  | Objects Selected | `29946:3407` | 375×304px | Header with count + close button; flat list of bulk actions |
  | Sensor | `29984:5904` | 375×700px | Status icon + name header + close; grouped actions with headlines & dividers + links |
  | Submenu | `29984:6753` | 375×286px | Back chevron + status icon + name header + close; single group of sub-actions |

- **Visual Design:**

  | Element | Token / Value | Notes |
  |---|---|---|
  | Container background | `--background/base` (#ffffff) | Variable binding confirmed: `VariableID:23879:3177` |
  | Container corner radius | `12px 12px 0 0` | Top-left and top-right only; bottom corners are flat (anchored to screen bottom) |
  | Menu frame corner radius | `12px` | All corners, but visually clipped by Base container |
  | Menu frame itemSpacing | `8px` (`--spacing/8`) | Vertical gap between menu sections/items |
  | Menu item text | `--text/base` (#31343f) | Via `Menu/Control` atom (same as Contextual Menu) |
  | Group heading text | `--text/alt` (#686b76) | "Sensor Actions", "Channel Actions", "Move" labels |
  | Dividers | `--border/alt2` (#e5e6e9) | Horizontal separators between groups |
  | Close button icon | `--text/base` (#31343f) | X icon in header row |
  | Header title | `--text/base` (#31343f) | "Name" / "X Objects selected" |
  | Status icon | Varies | Entity status indicator (e.g. green circle for OK) |

- **Tokens Used:**
  - **Colors (theme-aware):**
    - `--background/base` — Light: `#ffffff` / Dark: `#252937` — Sheet container background (**Variable ID: `VariableID:23879:3177`**)
    - `--text/base` — Light: `#31343f` / Dark: `#e5e6e9` — Menu item labels, header title, close icon
    - `--text/alt` — Light: `#686b76` / Dark: `#babcc2` — Group heading labels
    - `--border/alt2` — Light: `#e5e6e9` / Dark: `#54565f` — Group dividers
  - **Spacing (theme-invariant):**
    - `--spacing/8` (8px) — Menu frame vertical gap between sections/items
  - **Typography (theme-invariant):**
    - `Text Regular/Size 2 (base)` — Roboto 400, 14px — Menu item labels (via `Menu/Control`)
    - `Text Regular/Size 1 (small)` — Roboto 400, 12px — Group heading labels (via `Menu/Control`)
  - **Border Radius:**
    - `12px` — Container top corners (asymmetric: `12px 12px 0 0`), Menu frame (all corners)

- **Internal Structure (dev-mode confirmed):**

  **Base** (`12471:120`):
  ```
  Sheets/Mobile/Base (COMPONENT, 375×368px)
  ├── fill: --background/base (VarID:23879:3177) #ffffff
  ├── rectangleCornerRadii: [12, 12, 0, 0] (top-left, top-right, bottom-right, bottom-left)
  ├── constraints: vertical: TOP_BOTTOM, horizontal: LEFT_RIGHT (stretches both axes)
  │
  └── Base (VECTOR, 375×368px)
      ├── fill: --background/base (VarID:23879:3177) #ffffff
      ├── rectangleCornerRadii: [0, 0, 0, 0] (no rounding — parent clips)
      └── constraints: vertical: SCALE, horizontal: SCALE
  ```
  > Note: The rounding is achieved by the COMPONENT frame's corner radii clipping the VECTOR child. The VECTOR itself has no corner radii.

  **Composed variants** (Objects Selected, Sensor, Submenu) — all share this confirmed pattern:
  ```
  Sheets/Mobile/[Variant] (COMPONENT, fills: [], no fill on root)
  │
  └── Container Menu (GROUP)
      ├── constraints: vertical: SCALE, horizontal: SCALE
      │
      ├── Sheets/Mobile/Base (INSTANCE, componentId: 12471:120)
      │   ├── fills: [] (cleared at instance level — background from component's VECTOR child)
      │   ├── rectangleCornerRadii: [12, 12, 0, 0]
      │   └── constraints: varies per variant (see table below)
      │
      └── Menu (FRAME, VERTICAL auto-layout)
          ├── layoutMode: VERTICAL
          ├── primaryAxisSizingMode: FIXED, counterAxisSizingMode: FIXED
          ├── width: 375px (matches parent)
          ├── itemSpacing: 8 (--spacing/8)
          ├── cornerRadius: 12 (all corners, but visually clipped by Base)
          ├── fills: [] (transparent — relies on Base instance for background)
          │
          ├── Header row (varies per variant)
          ├── Menu/Control instances (action items)
          ├── Headline rows (group labels)
          └── Divider instances (group separators)
  ```

  **Constraint patterns per variant (dev-mode confirmed):**

  | Variant | Base Instance Constraints | Menu FRAME Constraints | Menu Height |
  |---|---|---|---|
  | Objects Selected | `V: TOP_BOTTOM, H: SCALE` | `V: SCALE, H: SCALE` | 304px (= parent) |
  | Sensor | `V: TOP_BOTTOM, H: SCALE` | `V: TOP, H: SCALE` | 611.9px (< 700px parent) |
  | Submenu | `V: SCALE, H: SCALE` | `V: SCALE, H: SCALE` | 250px (< 286px parent) |

  > Note: Sensor and Submenu have Menu FRAMEs shorter than the component height, leaving empty space at the bottom within the rounded Base container. In CSS, this naturally happens with `flex-direction: column` content that doesn't fill the container.

  **Header row patterns:**
  - **Objects Selected**: `"X Objects selected"` text + close (X) button (right-aligned)
  - **Sensor**: Status icon + `"Name"` text + close (X) button (right-aligned)
  - **Submenu**: Back chevron (`<`) + Status icon + `"Name"` text + close (X) button (right-aligned)

- **Action Behavior Rules (from documentation):**

  | Action Type | Behavior | Reason |
  |---|---|---|
  | Single selection | Auto-dismiss | Task completed |
  | Configuration | Stay open | Multiple adjustments |
  | Destructive | Auto-dismiss + confirmation | Prevent errors |
  | Navigation | Auto-dismiss | Context change |
  | Quick feedback | Stay open | Repetitive actions |

- **Accessibility:**
  - Full tab-through support with Enter to activate links
  - Provide feedback when an action is triggered
  - Close button should be keyboard-accessible
  - Back button (Submenu) provides context for return navigation

- **Responsive Behavior:**
  - **Mobile only** — 375px fixed width (matches standard mobile viewport)
  - Anchored to bottom of screen (bottom corners are flat)
  - Not for desktop viewports — use Contextual Menu instead

- **Dependencies (dev-mode confirmed):**
  - `Sheets/Mobile/Base` (componentId: `12471:120`) — Used as INSTANCE inside all composed variants. Contains the white background fill and top-rounded corners.
  - `Menu/Control` (component set: `18756:48139`) — Atom component from Contextual Menu (provides menu item states, icons, chevron for submenu)
  - `Divider/Horizontal` — Group separator
  - Icons: Close (X), ChevronLeft (back in Submenu), ChevronRight (submenu indicator on "Move"), Status icons (entity state indicators), various action icons (Pause, Play Arrow, Scanning, Edit, Notifications, Delete, ImportExport, EyeOutline, ChartAreaspline, externalLink, Link, Check, RevokeApproval, SortAscending, SortDescending, ArrowUp, ArrowDown)

- **Variant Node IDs (dev-mode confirmed):**

  | Node ID | Component Name | Type | Size |
  |---|---|---|---|
  | `12471:120` | Sheets/Mobile/Base | COMPONENT | 375×368px |
  | `29946:3407` | Sheets/Mobile/Objects Selected | COMPONENT | 375×304px |
  | `29984:5904` | Sheets/Mobile/Sensor | COMPONENT | 375×700px |
  | `29984:6753` | Sheets/Mobile/Submenu | COMPONENT | 375×286px |

  **Internal sub-node IDs (within composed variants):**

  | Parent | Sub-Node ID | Name | Type |
  |---|---|---|---|
  | Objects Selected | `29946:3391` | Container Menu | GROUP |
  | Objects Selected | `29946:3406` | Sheets/Mobile/Base (instance) | INSTANCE |
  | Objects Selected | `12471:307` | Menu | FRAME |
  | Sensor | `29960:5094` | Container Menu | GROUP |
  | Sensor | `29960:5095` | Sheets/Mobile/Base (instance) | INSTANCE |
  | Sensor | `29960:5096` | Menu | FRAME |
  | Submenu | `29984:6644` | Container Menu | GROUP |
  | Submenu | `29984:6645` | Sheets/Mobile/Base (instance) | INSTANCE |
  | Submenu | `29984:6646` | Menu | FRAME |

  **Showcase/parent frame:** `29960:5434` "Components" FRAME, fill `--background/hover` (VarID:`23879:3179`) — used as page background behind sheets, not part of the sheet component itself.

- **Confirmed Variable Bindings (from dev mode):**

  | Variable ID | Token | Hex (Light) | Used On |
  |---|---|---|---|
  | `23879:3177` | `--background/base` | `#ffffff` | Base component fill (both COMPONENT frame and VECTOR child) |

  > Note: Composed variants have `fills: []` on both root and Base instance — the white background comes from the Base component's internal VECTOR child fill (`23879:3177`). Menu FRAME also has `fills: []` (transparent). Deeper content (Menu/Control items, headers, dividers) uses tokens already confirmed in the Contextual Menu analysis (`--text/base`, `--text/alt`, `--border/alt2`).

- **CSS Implementation Reference:**
  ```css
  /* Sheet container — anchored to bottom of viewport */
  .sheet-mobile {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    width: 375px; /* or 100% on mobile viewports */
    max-height: 90vh; /* prevent covering full screen */
    background: var(--background-base);
    border-radius: 12px 12px 0 0;
    overflow: hidden; /* clip content to rounded corners */
    z-index: var(--z-sheet); /* above page content */
  }

  /* Menu content area */
  .sheet-mobile .menu {
    display: flex;
    flex-direction: column;
    gap: 8px; /* --spacing/8, itemSpacing: 8 */
    border-radius: 12px; /* cornerRadius: 12, visually redundant with parent clip */
    overflow-y: auto; /* scroll if content exceeds height */
  }

  /* Header row — common pattern */
  .sheet-header {
    display: flex;
    align-items: center;
    padding: 16px;
    gap: 8px;
  }
  .sheet-header .title { flex: 1; }
  .sheet-header .close-btn {
    width: 24px;
    height: 24px;
    color: var(--text-base);
    cursor: pointer;
  }

  /* Menu items — reuse Contextual Menu's Menu/Control styles */
  .sheet-mobile .menu-item {
    /* Same styles as .menu-item from Contextual Menu */
    /* Composed padding: 4px 16px (override from atom's 8px) */
  }

  /* Overlay/backdrop (not in Figma but needed for implementation) */
  .sheet-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    z-index: calc(var(--z-sheet) - 1);
  }
  ```

  > **Dev-mode notes (2026-03-03):**
  > - Composed variants use GROUP (not auto-layout) at the root level — the Base INSTANCE provides the background/rounding, the Menu FRAME provides the auto-layout content area
  > - Base instance `fills: []` at instance level — the visual white background comes from the component's internal VECTOR child, not the instance frame itself
  > - Base component constraints `TOP_BOTTOM` + `LEFT_RIGHT` ensure it stretches to fill the parent in both axes
  > - No overlay/backdrop component exists in Figma — implementation should add one for modal behavior

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** Users long-press or tap options on devices, sensors, or monitoring elements; displaying device-specific actions (pause, acknowledge, view details); showing device properties/sensor readings/status info supplementing main view; any scenario where a right-click contextual menu would appear on desktop
  - **Don't use:** Primary navigation (never for main app navigation); complex forms (avoid for multi-step configuration); desktop interface (use traditional contextual menus instead); non-contextual content (avoid for information not directly related to selected item)
  - **Considerations:** Always place in the same position (anchored to bottom of screen) across all UI; if a submenu is displayed, provide a label with the previous option selected for context; on submenus provide a back button (`ChevronLeft`); follow the action behavior table for dismiss/stay-open decisions (single selection → auto-dismiss, configuration → stay open, destructive → auto-dismiss + confirmation, navigation → auto-dismiss, quick feedback → stay open)
  - **Content:** Use concise action-oriented labels. Prioritize quick comprehension. Group related actions with headline labels and dividers.
  - **Accessibility:** Full tab-through support with `Enter` to activate links; provide feedback when an action is triggered; close button (X) must be keyboard-accessible; back button (Submenu) provides context for return navigation
  - **Structure:** Top-rounded container (`12px 12px 0 0`) anchored to screen bottom; header row with entity status icon + name + close button; menu items using `Menu/Control` atom instances; group actions with headline rows and `Divider/Horizontal` separators; 375px fixed width (standard mobile viewport); `--spacing/8` gap between sections

- **Examples:**
  - Objects Selected: `[X Objects selected ✕] → ✓ Acknowledge alarms | ⊘ Clear knowledge alarms | ⊘ Pause objects | ▶ Resume paused objects | ↻ Scan objects`
  - Sensor: `[● Name ✕] → Sensor Actions: ⏸ Pause | ▶ Resume | ↻ Scan Now | ✏ Settings | 🔔 Notification Triggers | 🗑 Delete | ↕ Move > || Channel Actions: 👁 Details | ✏ Settings | 📊 Graphs || ↗ Open in New Tab | 🔗 Copy Link`
  - Submenu: `[< ● Name ✕] → Move: ⬆ Top | ↑ Up | ↓ Down | ⬇ Bottom`

### Toast

- **Purpose:** Provides asynchronous feedback about performed actions and other important updates. Non-blocking notifications that appear briefly to confirm user actions without requiring interaction.
- **Figma Page:** `• Toasts` (node `19155:77969`)
- **Figma Component Name:** `Alert/Toast` (COMPONENT_SET `17515:58779`)
- **Documentation:** [Spectrum](https://spectrum.gitlab.paesslergmbh.de/spectrum/components/toast/toast.html)

- **Props/API:**

  | Prop | Type | Default | Description |
  |---|---|---|---|
  | `Status` | `"Success" \| "Error" \| "Warning" \| "Primary"` | `"Success"` | Visual status variant — controls background fill, border color, and icon |
  | `Button` | `boolean` | `false` | When `true`, shows action button (Small/Ghost) below message |
  | `Icon` | `boolean` | `false` | When `true`, shows status icon in message row |
  | `Caption` | `boolean` | `false` | When `true`, shows secondary caption text below message |
  | `Clearable` | `boolean` | `false` | When `true`, shows close (X) button and/or more options (⋮) |

- **Variants (by Status):**

  | Status | Node ID | Fill (hex) | Fill Variable ID | Stroke (hex) | Stroke Variable ID |
  |---|---|---|---|---|---|
  | Success | `17515:58738` | `#fdffeb` | `VariableID:23879:3198` | `#8f9900` | `VariableID:23880:1338` |
  | Error | `29263:4052` | `#fff6f8` | `VariableID:23879:3193` | `#e3063d` | `VariableID:23880:1336` |
  | Warning | `29263:4078` | `#fff8f3` | `VariableID:23879:3196` | `#de6800` | `VariableID:23880:1337` |
  | Primary | `29263:4104` | `#f5f9ff` | `VariableID:23879:3187` | `#0f67ff` | `VariableID:23880:1335` |

  > **Token match:** Primary fill `#f5f9ff` matches `--background/accentsoft`; Primary stroke `#0f67ff` matches `--text/accent` / `--background/accent`. Other status fills/strokes are new status-specific tokens.

- **Visual Design:**

  | Element | Token / Value | Notes |
  |---|---|---|
  | Container background | Status-specific fill (see table above) | Soft tinted background per status |
  | Container border | Status-specific stroke, `strokeWeight: 1px`, `strokeAlign: INSIDE` | 1px border in status color. Left accent bar appears visually thicker (~3-4px) — **Question:** may use individual stroke weights per side |
  | Corner radius | `4px` | All corners |
  | Shadow | `BoxShadow/Elevation/4` *(tentative)* | `0px 40px 32px rgba(37,41,55,0.16)`, `0px 4px 16px rgba(37,41,55,0.16)`, `0px 0px 4px rgba(37,41,55,0.10)` |
  | Message text | `--text/base` (#31343f) | `Text Regular/Size 2 (base)` — Roboto 400, 14px |
  | Caption text | `--text/base` (#31343f) *(inferred)* | Smaller or muted text below message |
  | Action button | Ghost button (`Small/Ghost`) | Text-only button, e.g. "Click here", "Action", "Undo" |
  | Status icons | Status-specific color | Success: `CheckFill` (green), Error: error circle (red), Warning: triangle (orange), Primary: info circle (blue) |
  | Close button | `Close` icon | 24×24px, shown when `Clearable=true` |
  | More button | `MoreVert` icon | Vertical three-dots, shown when `Clearable=true` |

- **Tokens Used:**
  - **Colors (status-specific, theme-aware):**
    - Success fill: `#fdffeb` (`VariableID:23879:3198`) / Dark: *TBD*
    - Success border: `#8f9900` (`VariableID:23880:1338`) / Dark: *TBD*
    - Error fill: `#fff6f8` (`VariableID:23879:3193`) / Dark: *TBD*
    - Error border: `#e3063d` (`VariableID:23880:1336`) / Dark: *TBD*
    - Warning fill: `#fff8f3` (`VariableID:23879:3196`) / Dark: *TBD*
    - Warning border: `#de6800` (`VariableID:23880:1337`) / Dark: *TBD*
    - Primary fill: `--background/accentsoft` (`#f5f9ff`, `VariableID:23879:3187`)
    - Primary border: `--text/accent` / `--background/accent` (`#0f67ff`, `VariableID:23880:1335`)
  - **Colors (shared):**
    - `--text/base` — Light: `#31343f` — Message text, caption text
  - **Shadows:**
    - `BoxShadow/Elevation/4` *(tentative)* — toast-specific, highest elevation
  - **Spacing (theme-invariant):**
    - `--spacing/8` (8px) — Root vertical padding (paddingTop, paddingBottom)
    - `--spacing/10` (10px) — Root horizontal itemSpacing
    - `--spacing/16` (16px) — Root paddingLeft
    - `--spacing/12` (12px) — Root paddingRight (asymmetric)
    - `--spacing/4` (4px) — Content vertical itemSpacing, Message Container itemSpacing
    - `--spacing/2` (2px) — Content paddingTop/paddingBottom
  - **Typography:**
    - `Text Regular/Size 2 (base)` — Roboto 400, 14px — Message text
  - **Border Radius:**
    - `4px` — Toast container

- **Internal Structure (confirmed via dev mode — identical across all 4 status variants):**
  - Root: COMPONENT, 320×44px (`primaryAxisSizingMode: FIXED` width, HUG height), `layoutMode: HORIZONTAL`
    - `counterAxisAlignItems: CENTER` → CSS: `align-items: center`
    - Padding: `left: 16px`, `right: 12px`, `top: 8px`, `bottom: 8px` (asymmetric left/right)
    - `itemSpacing: 10px` → CSS: `gap: 10px`
    - Fill: status-specific background (with `boundVariables` color binding)
    - Stroke: status-specific border (with `boundVariables` color binding), `strokeWeight: 1px`, `strokeAlign: INSIDE`
    - Effects: 3 `DROP_SHADOW` layers (Elevation/4):
      1. `offset(0, 40) blur(32) rgba(37,41,55, 0.16)` — `showShadowBehindNode: true`
      2. `offset(0, 4) blur(16) rgba(37,41,55, 0.16)` — `showShadowBehindNode: true`
      3. `offset(0, 0) blur(4) rgba(37,41,55, 0.10)` — `showShadowBehindNode: false`
    - Shadow color `#252937` matches `--background/body` dark theme value
    - `cornerRadius: 4px`
  - Children (3 slots, outer 2 toggled by boolean props):
    1. **[Icon]** *(visible when `Icon#29258:21 = true`)*: Status icon instance — not present in default API response (hidden by default)
    2. **Content** (FRAME `id varies per variant`): `layoutGrow: 1` (→ CSS: `flex: 1`), HUG vertical, `layoutMode: VERTICAL`
       - `counterAxisSizingMode: FIXED` (takes parent width minus siblings)
       - `paddingTop: 2px`, `paddingBottom: 2px`, `itemSpacing: 4px`
       - `primaryAxisAlignItems: CENTER` → CSS: `justify-content: center`
       - `counterAxisAlignItems: MAX` → CSS: `align-items: flex-end` (right-aligns HUG children)
       - Children:
         a. **Message Container** (FRAME): `layoutAlign: STRETCH` (→ CSS: `align-self: stretch`, overrides MAX), HUG vertical, `layoutMode: VERTICAL`
            - `primaryAxisAlignItems: CENTER`, `itemSpacing: 4px`
            - Contains: message text node, optional caption text node (visible when `Caption#29258:42 = true`)
         b. **Button Container** (FRAME): HUG × HUG, `layoutMode: HORIZONTAL`, `itemSpacing: 10px` — **`visible: false` by default**
            - `counterAxisAlignItems: CENTER`
            - Contains: `Small/Ghost` button instance (COMPONENT_SET `19908:78371`, props: `Type`: "OnlyText" | "Icon", `Status`: "Default")
            - Toggled visible when `Button#29258:0 = true`
    3. **[Clearable controls]** *(visible when `Clearable#29261:0 = true`)*: Close (X) icon and/or MoreVert (⋮) icon — not present in default API response (hidden by default)

- **Accessibility:**
  - Avoid auto-dismiss for users who may need more time to read
  - Should use `role="alert"` or `role="status"` for screen reader announcements
  - Close button must be keyboard-accessible
  - Include enough time for users to read content before auto-dismiss

- **Responsive Behavior:**
  - Desktop: appears at bottom-left of screen
  - Mobile: appears at bottom-center of screen
  - Fixed width (320px), height grows with content
  - Keep content consistent across breakpoints

- **Dependencies:**
  - Buttons: `Small/Ghost` (COMPONENT_SET `19908:78371`) — used in Button Container
  - Icons: `CheckFill` (success), `Placeholder` (error/warning/primary status icons), `Close` (clearable), `MoreVert` (clearable more options)

- **Figma Prop Name Mapping (from COMPONENT_SET `17515:58779`):**
  - `Status` → `Status` (variant: "Success" | "Error" | "Warning" | "Primary")
  - `Button#29258:0` → `Button` (boolean, default: false) — toggles Button Container visibility
  - `Icon#29258:21` → `Icon` (boolean, default: false) — toggles status icon visibility
  - `Caption#29258:42` → `Caption` (boolean, default: false) — toggles caption text visibility inside Message Container
  - `Clearable#29261:0` → `Clearable` (boolean, default: false) — toggles Close/MoreVert controls visibility

- **Icon Sizes:**
  - Status icon (CheckFill, error, warning, info): size inferred from layout — positioned left of content
  - Close button (X): **24×24px**
  - MoreVert (⋮): **24×24px**

- **Documentation Notes (Implementation Guidelines):**
  - **When to use:** Asynchronous feedback not requiring user interaction; confirming actions (e.g., "Saved!", "Sent!"); appears at bottom-left on desktop, bottom-center on mobile; can auto-dismiss or stay visible briefly
  - **Don't use:** Critical messages or actions that block user progress; when user must respond to continue (use Modal or Inline Alert instead); for essential or irreversible actions
  - **Considerations:** Include button to trigger action only if absolutely necessary (e.g. "Undo"); include link or handler in message; limit to 2 toasts on same screen; avoid placing essential or irreversible actions inside toast; use `Status` variants to reflect message tone (success, warning, error, primary); keep content consistent across breakpoints; fixed 320px width, height grows with content
  - **Content:** Use `Status` variant to indicate message tone; include button only if needed (e.g., "Undo", "Click here"); add caption for supporting details if necessary; keep message text concise and scannable
  - **Accessibility:** Use `role="alert"` or `role="status"` for screen reader announcements; avoid auto-dismiss for users who may need more time to read; close button must be keyboard-accessible; include enough time for users to read content before auto-dismiss
  - **Structure:** Horizontal layout: [Icon (optional)] + [Content: message + caption + button] + [Clearable controls]; container has status-specific fill and 1px border with left accent bar; `Elevation/4` shadow for prominence; `cornerRadius: 4px`; asymmetric padding (`left: 16px`, `right: 12px`, `top/bottom: 8px`)

- **Examples:**
  - Success (minimal): `[✓ Success message here.]` — green tint, left accent bar
  - Success + Button: `[✓ Success message here. Click here]` — with ghost button link
  - Warning + Caption + Clearable: `[⚠ Warning message here. | Caption, if needed, goes here | ✕ ⋮]`
  - Primary + Button + Caption + Clearable: `[ℹ Warning message here. | Caption, if needed, goes here | ✕ | Action]`

- **CSS Implementation Reference:**
  ```
  /* Toast container */
  .toast {
    display: flex;
    flex-direction: row;
    align-items: center;              /* counterAxisAlignItems: CENTER */
    width: 320px;                      /* primaryAxisSizingMode: FIXED */
    padding: 8px 12px 8px 16px;        /* asymmetric: top right bottom left */
    gap: 10px;                         /* itemSpacing: 10 */
    border: 1px solid var(--border-status);  /* strokeWeight: 1, strokeAlign: INSIDE */
    border-radius: 4px;
    background: var(--bg-status);
    box-shadow:
      0px 40px 32px rgba(37,41,55, 0.16),
      0px 4px 16px rgba(37,41,55, 0.16),
      0px 0px 4px rgba(37,41,55, 0.10);
  }
  /* Content wrapper */
  .toast__content {
    flex: 1;                           /* layoutGrow: 1 */
    display: flex;
    flex-direction: column;            /* layoutMode: VERTICAL */
    align-items: flex-end;             /* counterAxisAlignItems: MAX */
    justify-content: center;           /* primaryAxisAlignItems: CENTER */
    padding: 2px 0;
    gap: 4px;
  }
  /* Message container */
  .toast__message {
    align-self: stretch;               /* layoutAlign: STRETCH */
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
  }
  /* Button container (hidden by default) */
  .toast__actions {
    display: none;                     /* visible: false */
    flex-direction: row;
    align-items: center;
    gap: 10px;
  }
  .toast--has-button .toast__actions { display: flex; }
  ```

- **Open Questions:**
  - Left accent bar: REST API confirms uniform `strokeWeight: 1px` across all variants. The visually thicker left bar (~3-4px) likely uses Figma's individual stroke weights per side (`strokeTopWeight`, `strokeLeftWeight`, etc.) which require plugin API access to read. Desktop Bridge was not connected to the Design System file during analysis — **needs verification with plugin running in Design System file**.
  - Auto-dismiss timing: Documentation mentions auto-dismiss capability but no specific duration token or timing is defined.
  - Dark theme: None of the status-specific fill/stroke colors have confirmed dark variants yet.
  - Hidden children: Icon and Clearable control children are not returned by API when their boolean props are `false`. Full child structure with all elements visible needs either Desktop Bridge access or a variant screenshot with all booleans toggled `true`.

---

## Restructuring Log

<!-- Track what has been restructured and when -->
| Component | Date | Changes Summary | Status |
|-----------|------|-----------------|--------|
| Checkbox | 2026-03-03 | Dev mode deep analysis: confirmed all 20 variants (10 states × 2 devices). 4 structural patterns identified: Unchecked (fill+stroke), Checked (accent fill+icon), Focus (dual-layer FRAME+RECTANGLE), Disabled Selected (01-Base/Background naming). 5 NEW variable binding confirmations: `--background/hover` (`23879:3179`), `--border/base` (`23880:1098`), `--border/alt2` (`23880:1100`), disabled fill (`23879:3182`), disabled text (`23879:2980`). KEY FINDING: Same-hex/different-variable pairs (hover vs disabled fill, border/base vs disabled text) — will diverge in dark theme. Focus ring uses dual-layer (outer FRAME 4px OUTSIDE + inner RECTANGLE 2px INSIDE). Icon component IDs confirmed: Check (`303:1431`), Remove (`5901:457`). CSS implementation reference added. | Dev-confirmed |
| FAB | 2026-03-03 | Dev mode deep analysis: confirmed identical structure across all 4 states via `figma_get_component_for_development`. No auto-layout on root — uses constraints-based centering. 4 NEW variable binding confirmations: `--background/accent` (`23879:3183`), `--background/accentalt` (`23879:3184`), `--background/accentalt2` (`23879:3185`), `--text/overlay` (`23879:2987`). Confirmed Grid icon componentId (`29782:5923`) with dual-Vector structure (transparent bounding + white glyph). Focus ring confirmed: 4px `strokeAlign: OUTSIDE`. Contextual Menu confirmed as hidden child of Pressed variant (`Menu/Example` `18756:48876`). CSS implementation reference added. All sub-component IDs documented. | Dev-confirmed |
| Alert (Inline) | 2026-03-03 | Initial analysis via dev mode: 5 status variants (Success/Error/Warning/Primary/Secondary) × 2 type variants (ShortText/LongText), `Dismiss#30235:0` boolean prop. Discovered DUAL-BORDER PATTERN (Root soft outer + Wrapper accent inner for left bar effect). 1 NEW soft border token (`--border/successsoft` #dce55c, `VariableID:23880:1109`). Confirmed `--border/alt` variable binding (`VariableID:23880:1099`). Found Alert-specific accent border variables separate from Toast's (different VarIDs, Warning has different hex: #c45c00 vs #de6800). Found LongText inconsistencies: 3/5 variants missing Wrapper frame (Figma file bugs). Alert vs Banner vs Toast comparison table. | Analyzed |
| Banner | 2026-03-03 | Initial analysis via dev mode: 3 type variants (Information/Error/Warning) × 1 content variant (Single Line), `Close#29548:0` boolean prop. Discovered 2 NEW soft border tokens (`--border/errorsoft` #ff779a, `--border/warningsoft` #ffb067), confirmed `--border/accentsoft` variable binding (`VariableID:23880:1103`), confirmed `--text/base` (`VariableID:23337:93155`) and `--text/accent` (`VariableID:23879:2981`) bindings. Invisible spacer pattern documented. Banner vs Toast comparison table. Shared fill tokens with Toast, softer border tokens. CSS implementation reference. | Analyzed |
| Toast | 2026-03-03 | Dev mode deep analysis: confirmed identical structure across all 4 variants via `figma_get_component_for_development`, exact Figma property IDs with hash suffixes (`Button#29258:0`, `Icon#29258:21`, `Caption#29258:42`, `Clearable#29261:0`), confirmed `layoutGrow:1`/`counterAxisAlignItems:MAX`/`layoutAlign:STRETCH` layout behavior, `Small/Ghost` button component (`19908:78371`) with Type/Status props, 3-layer shadow details with `showShadowBehindNode` flags, added CSS implementation reference, updated Open Questions with API limitations | Dev-confirmed |
| All 9 components | 2026-03-03 | Re-analysis: added Figma Prop Name Mapping, Icon Sizes, enriched Documentation Notes with implementation guidelines, accessibility details, and structure details for all components. Added global Icon Sizes section and Component Construction Patterns section. | Enriched |
| Checkbox | 2026-03-02 | Initial analysis: 10 states × 2 devices, token mapping, documentation extracted | Analyzed |
| Contextual Menu | 2026-03-03 | Dev mode deep analysis: confirmed all 17 variants (12 atoms: 6 states × 2 icon + 5 composed Action Menus). 4 structural patterns: Default/Hover/Pressed (no border), Selected (4px INSIDE --border/accent), Focus (4px OUTSIDE --border/accentsoft), Disabled (dedicated VarID 23879:2980). 3 NEW variable binding confirmations: `--text/alt` (`23879:2979`), `--background/pressed` (`23879:3180`), `--border/accent` (`23880:1102`). KEY FINDING: Composed menus override atom padding py:8px→4px (36px→28px height). Selected strokeAlign:INSIDE vs Focus strokeAlign:OUTSIDE. Disabled text uses dedicated text-namespace variable (23879:2980), NOT --border/base despite same hex. Sub-component IDs confirmed: ChevronRight (0:1050), Divider (830:495), Headline (18756:48627). CSS implementation reference added. | Dev-confirmed |
| Contextual Menu | 2026-03-02 | Initial analysis: 6 states × 2 icon variants (atom), 5 composed Action Menu variants, token mapping, new `--background/pressed` token discovered | Analyzed |
| CTA Bar | 2026-03-03 | Dev mode deep analysis: confirmed all 24 variants (16 Desktop + 8 Mobile) from component set data. KEY CORRECTION: Info text IS disabled in Disabled state — uses dedicated disabled text variable (VarID `23879:2980` #a4a6af), NOT --text/base. Existing docs were wrong. KEY FINDING: Disabled primary button fill uses VarID `23879:3186` (#74abff) — a **separate background-namespace variable** from `--border/accentsoft` (`23880:1103`) despite same hex. Same-hex/different-variable pattern continues. Desktop layout uses `primaryAxisAlignItems: MAX` with Button group `layoutGrow: 1` for left-right alignment (2 variants use SPACE_BETWEEN as alternative). Mobile uses VERTICAL layout with `layoutAlign: STRETCH` on all children. All 6 button component IDs confirmed (3 types × 2 states). Shadow Elevation/3 confirmed: 3-layer with exact values. Figma prop hash IDs confirmed for Desktop (31271:x) and Mobile (31278:x). CSS implementation reference added. | Dev-confirmed |
| CTA Bar | 2026-03-02 | Initial analysis: Desktop (16 variants) + Mobile (8 variants), button token mapping, new typography token `Text Bold/Size 2`, new spacing tokens (`--spacing/10`, `--spacing/20`, `--spacing/32`) | Analyzed |
| Empty State | 2026-03-02 | Initial analysis: 2 type variants (Content/Search), new typography token `Text Medium/Size 4 Medium` (20px), icon-prefixed button pattern documented | Analyzed |
| Footer | 2026-03-02 | Initial analysis: Single component (no variants), desktop-only, first confirmed variable binding (`VariableID:23879:3178` = `--background/body`), `--border/base` used as muted text color | Analyzed |
| Sheet (Mobile) | 2026-03-03 | Dev mode analysis: confirmed all 4 components via `figma_get_component_for_development`. Confirmed GROUP-based composition pattern (not auto-layout at root). Base component (12471:120): `--background/base` (VarID:23879:3177) fill on both COMPONENT frame AND VECTOR child, `rectangleCornerRadii: [12,12,0,0]`, constraints `TOP_BOTTOM`+`LEFT_RIGHT`. Composed variants: Root COMPONENT → GROUP "Container Menu" → [Base INSTANCE + Menu FRAME]. Base INSTANCE `fills: []` (background from component's VECTOR child). Menu FRAME: VERTICAL auto-layout, `itemSpacing: 8`, `cornerRadius: 12`, both axes FIXED, width 375px. Constraint patterns vary per variant (Base: TOP_BOTTOM/SCALE for Objects Selected/Sensor, SCALE/SCALE for Submenu; Menu: SCALE for Objects Selected/Submenu, TOP for Sensor). Menu height < parent height in Sensor (611.9/700) and Submenu (250/286). Sub-component node IDs confirmed for all 3 composed variants. Showcase frame (29960:5434) uses `--background/hover` (23879:3179) as page background. CSS implementation reference added. | Dev-confirmed |
| Sheet (Mobile) | 2026-03-02 | Initial analysis: 4 individual components (Base + 3 composed), mobile-only replacement for Contextual Menu, confirmed `--background/base` variable binding (`VariableID:23879:3177`), action behavior rules table, top-rounded container pattern (`12px 12px 0 0`) | Analyzed |
| Toast | 2026-03-02 | Initial analysis: 4 status variants (Success/Error/Warning/Primary) × 4 boolean toggles (Button/Icon/Caption/Clearable), 8 new variable bindings (4 fill + 4 stroke), 6 new status color tokens, new shadow level (Elevation/4 tentative), `--background/accentsoft` variable binding confirmed | Analyzed |
