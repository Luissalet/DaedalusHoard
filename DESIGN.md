---
name: Daedalus's Hoard
description: Local image-to-3D generation, comparison and retained versions.
colors:
  accent: "#73d1be"
  accent-strong: "#9bdfd1"
  accent-dim: "#54a895"
  accent-ink: "#10221e"
  accent-soft: "rgba(115,209,190,.14)"
  accent-line: "rgba(115,209,190,.38)"
  canvas: "#171919"
  sunken: "#121414"
  surface: "#1e2121"
  elevated: "#282b2c"
  hover: "#303334"
  line: "#3a3d3e"
  control: "#5e6364"
  ink: "#e1eaec"
  muted: "#b4bcbe"
  dim: "#9ba4a6"
  field: "#222a2b"
  danger: "#f09086"
typography:
  brand:
    fontFamily: "Cinzel, 'Iowan Old Style', Charter, Georgia, 'Liberation Serif', 'Noto Serif', 'Times New Roman', serif"
    fontSize: "19px"
    fontWeight: 600
    letterSpacing: "0.01em"
  headline:
    fontFamily: "Cinzel, 'Iowan Old Style', Charter, Georgia, 'Liberation Serif', 'Noto Serif', 'Times New Roman', serif"
    fontSize: "23px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Cinzel, 'Iowan Old Style', Charter, Georgia, 'Liberation Serif', 'Noto Serif', 'Times New Roman', serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.4
  body:
    fontFamily: "'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "12px"
    fontWeight: 600
  small:
    fontFamily: "'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans', 'Liberation Sans', Arial, sans-serif"
    fontSize: "12px"
    lineHeight: 1.55
rounded:
  label: "4px"
  control: "5px"
  overlay: "6px"
  field: "7px"
  upload: "8px"
  dialog: "10px"
spacing:
  tight: "7px"
  control: "10px"
  compact: "12px"
  inset: "20px"
  section: "24px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.control}"
    padding: "11px 15px"
  button-primary-hover:
    backgroundColor: "{colors.accent-strong}"
    textColor: "{colors.accent-ink}"
  button-primary-active:
    backgroundColor: "{colors.accent-dim}"
    textColor: "{colors.accent-ink}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 12px"
  button-quiet:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "7px 9px"
    height: "36px"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 11px"
  model-field:
    backgroundColor: "{colors.field}"
    rounded: "{rounded.field}"
  version-selected:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "9px 10px"
---

# Design System: Daedalus's Hoard

## Overview

**Creative North Star: "The Hoard Model Workbench"**

The implemented world is the existing Hoard family: shared charcoal surfaces, Cinzel headings, Source Sans 3 controls and Daedalus's turquoise accent. Luis explicitly requested this family style and icon, superseding the earlier light inspection-bench direction. The north star below describes that implemented family workbench; it does not establish a new identity or an approved naming preference.

A compact, flat workspace surrounds a distinct model field. Preparation, retained versions, optional refinement or learned enlargement from an original 512 result to 1024, and export stay legible around the actual geometry. Equal comparison panes and linked orbit let the user inspect an original beside a later version; common clay material supports shape comparison, while color mode restores the available model color or materials.

This record follows the finished client and the final mechanical/owl front and quarter comparison captures plus the full mobile page. Construction was explicitly code-led: no approved visual comp, QUALITY BAR card or generated critique-reference exists, and no comp-fidelity claim is made. FINISH-R3.md reports SHIP only at its inspected scope. The single earlier detector pass was DEGRADED and regex-only with parsers absent; it was not repeated for this refresh. Those are evidence limits, not additional design rules.

**Key Characteristics:**

- Inherited charcoal surfaces with a single turquoise action accent.
- Self-hosted Cinzel headings and Source Sans 3 operational text.
- The supplied curled dragon, gold cube and caliper icon as family identity.
- Flat persistent panels, fine dividers and restrained corner radii.
- Actual model geometry, aligned comparison and separately retained versions.

## Colors

The palette combines the shared neutral charcoal layers with one turquoise accent. The frontmatter records effective values after the app overrides the vendored theme; it does not import unrelated Hoard palettes.

### Primary

- **Daedalus Turquoise** (`accent`): brand text, primary actions, active navigation, focus, checked controls and live progress.
- **Light Turquoise / Deep Turquoise** (`accent-strong`, `accent-dim`): primary hover and active states; the light tone also identifies checked resolution text.
- **Dark Accent Ink** (`accent-ink`): readable text on filled turquoise actions.
- **Turquoise Wash / Turquoise Boundary** (`accent-soft`, `accent-line`): selected versions, pressed controls and radio selection without filling entire panels with accent.

### Neutral

- **Deep Charcoal / Sunken Charcoal** (`canvas`, `sunken`): continuous workspace and reference/thumbnail wells.
- **Control Charcoal / Elevated Charcoal / Hover Charcoal** (`surface`, `elevated`, `hover`): header and fields, temporary surfaces, and hover response.
- **Fine Divider / Control Outline** (`line`, `control`): structural boundaries and stronger field outlines.
- **Pale Ink / Muted Ink / Dim Ink** (`ink`, `muted`, `dim`): primary text, supporting copy and placeholder/icon detail.
- **Inspection Charcoal** (`field`): the model field, distinct from the surrounding controls.
- **Error Coral** (`danger`): error text and error notices; an error notice uses dark ink and a written message.

**The Family Surface Rule.** Use the inherited charcoal layers and the app accent for controls; preserve the model field as a distinct inspection surface.

The gold details belong to the supplied brand artwork, not a second action accent. Sidecar tonal ramps are synthesized inspection aids, not additional implemented palette tokens.

## Typography

**Display / Heading Font:** Cinzel with the inherited serif fallback stack.

**Body / Control Font:** Source Sans 3 with the inherited sans-serif fallback stack.

Both families are self-hosted under `client/vendor/fonts/` with swap loading. Cinzel supplies the family character on brand, page and section headings; Source Sans 3 keeps fields, navigation, model titles and metadata compact. There is no separate hero display scale or implemented monospace UI role.

### Hierarchy

- **Brand:** The frontmatter brand role is used in the desktop header; it becomes (16px) on phones, where the family suffix is hidden.
- **Headline:** The page heading uses the headline role and reduces to (22px) in phone preparation.
- **Title:** Section headings use the title role. Empty-model and dialog headings have local larger variants; these do not create another universal display ramp.
- **Body:** The body role covers ordinary text and field values. Paragraphs use the body line height; buttons use a compact line height (1.3).
- **Label:** Visible field names use the label role; controls remain sentence case.
- **Small:** Helpers use the small role. Existing secondary metadata also uses (11px), with some phone labels reaching (10px); this is recorded as incumbent density, not a recommended readability floor.

**The Task Label Rule.** Use short, sentence-case Spanish labels that name an action, object or state; Cinzel provides the family heading character without slogans or ornamental eyebrows.

## Layout

The desktop workbench is a centered three-column grid capped at (1920px): preparation (276px), a flexible inspection column with a (300px) minimum, and results (258px). At (1500px) and above, the side columns become (300px) and (280px), with a (400px) inspection minimum. The header is (72px) tall. This records the existing workbench rather than prescribing a three-column template for all future screens.

At (1150px) and below, results move into a three-column strip under preparation and inspection; Recents occupies a full row and remains available. At (700px) and below, controls stack in source order, the header becomes (64px), the family suffix and hardware text are abbreviated, and viewer actions may wrap. Results regain horizontal section dividers. Phone model fields are (440px) high and comparison keeps equal side-by-side panes. Above phone width the inspection region is sticky with viewport-relative height and a (590px) minimum.

The spacing vocabulary is compact around controls and wider between tasks. The library is separately centered, capped at (1460px), and uses an automatic grid with a (230px) minimum card width; phones use two columns, stacked metadata and vertical filters. Preparation, versions, refinement, export and library remain accessible at phone widths.

## Elevation & Depth

Persistent panels are flat. Charcoal tone changes and fine borders supply structure; library cards have no floating outer shell. Shadows belong to transient overlapping progress, notices and the settings dialog. Actual model contact shading is a viewer effect, not a card elevation style.

### Shadow Vocabulary

- **Progress overlay** (`0 7px 22px rgba(0,0,0,.3)`): live progress over the model field.
- **Notice** (`0 6px 24px rgba(0,0,0,.3)`): a transient message above the page.
- **Dialog** (`0 20px 70px rgba(0,0,0,.4)`): settings modal, paired with a black half-opacity backdrop.

**The Flat Workspace Rule.** Keep persistent panels flat; use elevation when a temporary surface overlaps the work.

## Shapes

Controls use gently curved corners, smaller label corners and slightly softer model-field corners. Single-pixel lines carry structure. Upload wells have a dashed boundary; the modal uses the largest recorded corner radius. These container treatments do not imply a universal pill or raised-card system. The small hardware status indicator is circular. Operational icons are inline stroked SVGs; the brand uses the supplied raster artwork, showing a curled dragon around a gold cube and caliper.

## Components

### Buttons

Compact rectangular controls establish a clear action order.

- **Primary:** Turquoise fill with Dark Accent Ink, semibold text and the frontmatter padding/radius. Hover uses Light Turquoise and active uses Deep Turquoise.
- **Secondary:** Control Charcoal, Pale Ink and a stronger outline. Hover uses Hover Charcoal and the accent border.
- **Quiet:** A smaller control with a fine divider border; hover and pressed state use Turquoise Wash and Turquoise Boundary. Minimum height is (36px).
- **Icon:** Transparent at rest with a Hover Charcoal response, inline SVG and a final minimum target of (40px) in each dimension.
- **Text:** A small turquoise action without a filled container; hover underlines the label.
- **Focus / disabled:** Interactive elements have an accent outline (2px) offset by (3px). Disabled buttons use half opacity and a default cursor. State transitions last (.18s); reduced motion removes transitions.

### Chips

Library status badges are read-only labels over thumbnails, using Control Charcoal, Pale Ink and compact rounded corners. Padding is (4px 7px), with (11px) text, reduced to (10px) in the incumbent phone cards. They are status labels, not action filters.

### Cards / Containers

Library cards are whole-cell buttons with no outer border, fill or shadow. Their sunken thumbnail is the bounded visual surface, with the title and secondary state/date below it. Hover scales only the contained image (1.025) over (.2s); reduced motion removes the transition. Use actual model thumbnails when available and the selected reference while a thumbnail is unavailable. An empty upload preview is hidden until a reference exists; it is not a broken-image state to reproduce.

### Inputs / Fields

Control Charcoal fields use Pale Ink, Control Outline borders and visible labels above values. Focus follows the shared accent outline. The two-part resolution radio group uses Turquoise Wash, Light Turquoise text and an inset accent line for the checked option. Checkboxes retain native behavior with the accent color. Export size shows its unit beside the numeric input. Engine parameters are available in small native details disclosures.

### Navigation

The header uses plain sans-serif view buttons. Active navigation gains turquoise text, semibold weight and a bottom rule (2px), with `aria-current` exposing the active view. Phone navigation remains visible while the brand suffix and hardware text abbreviate. The brand image is (44px) square on desktop and (36px) on phones. The shared Faustus launcher retains its family mark and accessible name rather than acquiring another local identity.

### Version Inspection

Versions are full-width, left-aligned buttons with a compact name and a supporting engine/state description. Selection uses Turquoise Wash, Turquoise Boundary and `aria-pressed`. Original, refined and enlarged versions remain separately selectable, with resolution or engine/token details named rather than implying a quality ranking. The optional “Ampliar a 1024” action uses the existing secondary button, separated from refinement by a fine divider and supporting copy. It appears for a completed original 512 generation and retains the source as a separate version.

Comparison divides the model field into equal flex panes with a fine central line and small elevated-charcoal labels. Camera changes are linked. Entering comparison or activating the full-view control selects common clay geometry. “Vista completa” loads the full mesh; “Vista ligera” returns to the preview. The footer explicitly identifies full geometry or the preview face count. In the full view, “Ver color” restores the full mesh's vertex color/PBR-light appearance; the preview uses “Ver materiales”. These controls expose inspection choices, not a quality score. The viewer's full/light setting is separate from the export geometry checkbox.

Direct links retain the selected job and the active comparison/full-view states through `job`, `compare=1` and `full=1` query parameters. A comparison link selects the original alongside its later version in clay; the ordinary single-version view remains available. This state behavior belongs to the workbench, without introducing a new visual primitive.

## Do's and Don'ts

### Do:

- **Do** load the shared Hoard theme before the app stylesheet and retain the local font assets.
- **Do** use the supplied app icon for the brand and the shared Faustus launcher for copilot access.
- **Do** keep the model field distinct, compare aligned versions and retain the original.
- **Do** expose selected state through fill, border and semantic state attributes.
- **Do** retain visible keyboard focus, native control behavior and reduced motion.
- **Do** keep export units beside the entered dimension and keep library access visible on phones.

### Don't:

- **Don't** reintroduce the superseded light paper palette or replace the family icon with a generic cube mark.
- **Don't** raise every persistent panel with a shadow or add decorative scenery around the model.
- **Don't** use a refined model's visual prominence to imply automatic improvement or print readiness.
- **Don't** replace real output with a demonstration model or overwrite the original with a refined version.
- **Don't** turn the incumbent 10–11px metadata sizes into a new minimum-size standard for future surfaces.

<!-- Refreshed after the final UI correction from client/style.css, client/vendor/hoard-theme.css, client/index.html and client/app.js, following PRODUCT.md and .impeccable/surfaces/workbench.md. Final evidence in the parent research directory: upscale-mechanical-front-full.png, upscale-mechanical-quarter-full.png, upscale-owl-front-full.png, upscale-owl-quarter-full.png, mobile-upscale-full.png and FINISH-R3.md (SHIP at its inspected scope). Preserves the explicit Hoard-family world and existing token frontmatter; the earlier light inspection-bench direction remains superseded. Not canonized: 10–11px metadata density, absent parser coverage, absent comp/QUALITY BAR/critique-reference artifacts, and historical stale-DESIGN detector warnings. No new detector pass. -->
