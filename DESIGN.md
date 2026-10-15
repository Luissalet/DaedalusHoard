---
name: Daedalus's Hoard
description: Local image-to-3D generation and version inspection.
colors:
  accent: "#315e47"
  ink: "#26332b"
  muted: "#58675d"
  canvas: "#f4f4ef"
  surface: "#fffefa"
  line: "#d5dacf"
  control: "#839488"
  field: "#dce0d7"
  danger: "#943b32"
typography:
  headline:
    fontFamily: "Segoe UI, system-ui, sans-serif"
    fontSize: "23px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Segoe UI, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.4
  body:
    fontFamily: "Segoe UI, system-ui, sans-serif"
    fontSize: "14px"
    lineHeight: 1.55
  label:
    fontFamily: "Segoe UI, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 600
  small:
    fontFamily: "Segoe UI, system-ui, sans-serif"
    fontSize: "12px"
    lineHeight: 1.55
rounded:
  label: "4px"
  control: "5px"
  overlay: "6px"
  field: "7px"
spacing:
  tight: "7px"
  control: "10px"
  compact: "12px"
  inset: "20px"
  section: "24px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#fff"
    rounded: "{rounded.control}"
    padding: "11px 15px"
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
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 11px"
  model-field:
    backgroundColor: "{colors.field}"
    rounded: "{rounded.field}"
---

# Design System: Daedalus's Hoard

## Overview

**Creative North Star: "The Model Inspection Bench"**

The built interface translates the assigned microscopy workbench direction into a quiet digital inspection bench. Warm paper surfaces, muted green controls and a separate neutral model field keep the specimen legible. Preparation, inspection and preserved versions are visible as working tools rather than decorative laboratory imagery.

The system is compact and task oriented. Small sentence-case headings, plain Spanish labels, fine dividers and restrained rounding give the model more visual weight than the surrounding controls. The comparison view uses equal adjacent panes and linked camera movement, with a common clay mode for judging geometry. Color mode shows the actual model materials.

This is a record of the built client and the existing desktop/mobile screenshots, following a confirmed code-led build. The North Star names the implemented direction; it is not a newly approved brand identity. No approved comp, QUALITY BAR card or generated critique-reference exists, so this document makes no comp-fidelity claim. Daedalus remains an implementation name.

**Key Characteristics:**
- Warm light surfaces with a muted green action accent.
- A distinct neutral field for inspecting real geometry.
- Compact, sentence-case utility typography.
- Flat panels and fine structural dividers.
- Aligned original/refined comparison with preserved version selection.

## Colors

The palette is low-chroma and slightly green, with warmer control surfaces and a cooler, denser model field. Frontmatter values reproduce the current stylesheet; descriptive names explain their use.

### Primary
- **Bench Green** (`accent`): generation and download actions, active navigation, checked controls, focus outlines and the product line mark.

### Neutral
- **Graphite Green** (`ink`): ordinary text, form values and section headings.
- **Muted Sage Ink** (`muted`): helper copy, metadata, unselected navigation and secondary icons.
- **Warm Paper** (`canvas`): the continuous workspace background.
- **Ivory Surface** (`surface`): header, inputs, buttons and transient panels.
- **Fine Sage Divider** (`line`): panel boundaries and quiet control borders.
- **Control Sage** (`control`): input outlines and the upload boundary, stronger than structural dividers.
- **Inspection Grey** (`field`): the model viewing field, keeping silhouettes separate from the controls.

### Feedback
- **Muted Brick** (`danger`): error text and error notices. Status is also expressed in words, never only through hue.

**The Specimen Field Rule.** Keep the model field distinct from the paper control surfaces so the object remains the primary visual evidence.

## Typography

**Body and UI Font:** Segoe UI, with system-ui and sans-serif fallbacks.

**Character:** A practical Windows utility face at compact sizes. This build has no separate editorial or display face; the operational heading is not a display-type identity to copy into future promotional surfaces.

### Hierarchy
- **Headline:** The frontmatter headline role is used for the main page heading; it reduces to (22px) in the phone preparation panel.
- **Title:** The title role distinguishes section headings without large jumps in scale.
- **Body:** The body role covers form values and ordinary copy. Paragraphs use the documented body line-height; controls retain their own compact line-height (1.3).
- **Label:** The label role names fields and controls in sentence case, with no tracking or uppercase decoration.
- **Small:** The small role covers instructions and version descriptions. Secondary metadata also uses (11px); phone viewer metadata reaches (10px), an incumbent detail rather than a new minimum-size standard.

**The Task Label Rule.** Use short, sentence-case labels that name the action, object or state; do not introduce slogans or ornamental eyebrows.

## Layout

The desktop workbench is a three-column grid: preparation (276px), a flexible inspection column with a (300px) minimum, and results (258px). The entire workspace is centered and capped at (1920px). Above (1500px), the side columns become (300px) and (280px), with a (400px) inspection minimum. The header is (72px) tall.

At widths up to (1150px), results become a three-column strip below preparation and inspection; recent items are omitted from that strip while the full library remains available. At widths up to (700px), the header becomes (64px), the workbench stacks in source order, recent items return, and the results sections regain horizontal separators. The model field is (440px) high on phones, retaining side-by-side comparison. Above phone width the inspection area sticks to the viewport and uses its available height, with a (590px) minimum inspection region.

Spacing is compact around controls and more generous between tasks. The reusable rhythm is captured in the frontmatter; preparation and results use roughly one inset around their contents, and section boundaries use the section gap. The library uses a separate centered container capped at (1460px), an automatic grid with a (230px) minimum card width, and two columns on phones. This documents existing surfaces, not a mandatory three-column template for every future view.

## Elevation & Depth

The ordinary workspace is flat. Fine borders and differences in surface tone separate sections; library items do not float inside raised cards. Shadows are reserved for a progress panel over the model field, a floating notice and the settings dialog. Actual model contact shading belongs to the viewer and is not a UI card-shadow rule.

### Shadow Vocabulary
- **Progress overlay** (`0 7px 22px rgba(33,50,36,.12)`): lifts live progress over the model field.
- **Notice** (`0 6px 24px rgba(24,44,28,.2)`): separates a transient message from the page beneath it.
- **Dialog** (`0 20px 70px rgba(28,43,31,.2)`): establishes the modal settings layer, paired with a translucent backdrop.

**The Flat Workspace Rule.** Keep persistent panels flat; use elevation when a temporary surface overlaps the work.

## Shapes

Controls use gently curved corners, with smaller radii on specimen labels and larger radii on model fields and overlays. Single-pixel borders carry structure. The upload area has a dashed outline and slightly softer corners (8px); the dialog is rounder again (10px). These two container-specific treatments do not create a universal pill or card system. Circular shapes are limited to the small status indicator. Icons are simple stroked SVGs.

## Components

### Buttons

Quiet, compact rectangles make action priority explicit.

- **Primary:** Bench Green with white text, semibold weight, the control radius and primary padding from the frontmatter. Hover deepens to (#234b34); active deepens further to (#173a25).
- **Secondary:** Ivory Surface, Graphite Green text and a Control Sage outline. Hover uses a light sage fill (#e9eee4) and the accent border.
- **Quiet:** A smaller surface control with a Fine Sage Divider border; hover and pressed state use a sage fill (#e2ebde) and stronger border (#92a48f).
- **Icon:** A compact square (32px), transparent at rest, with a sage hover fill and an inline stroked SVG.
- **Text:** A small green action without a filled container; hover underlines its label.
- **Focus / disabled:** Interactive elements use a visible accent outline (2px) offset by (3px). Disabled buttons use half opacity and the default cursor. Color transitions last (.18s), and the reduced-motion preference removes transitions.

### Chips

The library status badge is a read-only label over the thumbnail: Ivory Surface, compact text (11px), label-radius corners and padding (4px 7px). It is not a filter chip. On phones it uses (10px) text to fit the existing cards.

### Cards / Containers

Library cards are whole-cell buttons with no outer border or shadow. Their thumbnail is the bounded visual surface, with field-radius corners and a muted neutral fill. Titles sit beneath the thumbnail; status and date remain secondary. Hover enlarges only the contained image slightly (1.025) over (.2s), without lifting the card. The progress panel is the exception for overlapping content, as documented under Elevation & Depth.

### Inputs / Fields

Ivory fields use Graphite Green values, Control Sage borders, the control radius and input padding from the frontmatter. Labels sit above rather than inside the value. Focus uses the shared accent outline. Resolution uses a two-part native radio group: the chosen option has a pale green fill (#e1ebdf), darker text (#244b34) and an inset accent outline. Checkboxes retain native behavior with the accent color. Export dimensions display their unit beside the numeric input.

### Navigation

The header contains plain text buttons. Active navigation gains green text, semibold weight and a bottom rule (2px); inactive navigation is muted. The active view is also exposed through `aria-current`. Phone navigation remains visible while the family suffix and hardware text are abbreviated. The brand line mark is an outlined cube; the separately supplied Faustus launcher follows the shared Hoard family identity rather than establishing another local button style.

### Version Inspection

Version entries are full-width, left-aligned buttons with a compact name and secondary description. Selection uses a pale sage fill (#e2ebde), a fine boundary (#a7b5a1) and `aria-pressed`. The model field has equal flex panes in comparison mode, a fine central divider and small ivory labels identifying original and refined geometry. Camera changes are linked. Entering comparison selects the common geometry material, while the material control can restore color. The original and later versions remain separately selectable.

## Do's and Don'ts

### Do:
- **Do** keep the model field visually distinct from the control surfaces.
- **Do** use sentence-case Spanish labels and compact, visible field names.
- **Do** show version selection through fill, border and a semantic pressed state.
- **Do** compare original and refined geometry in aligned panes with linked orbit.
- **Do** retain visible keyboard focus and honor reduced motion.
- **Do** keep export units visible beside the entered dimension.

### Don't:
- **Don't** add decorative laboratory imagery to express the inspection-bench direction.
- **Don't** raise every persistent panel with a shadow.
- **Don't** use a refined model's visual prominence to imply it is automatically better or print-ready.
- **Don't** replace the original with a refined result or label a synthetic specimen as an actual result.
- **Don't** promote the current small metadata sizes or utility system font into a new display-type standard.

<!-- Evidence: client/style.css, client/index.html, client/app.js, .impeccable/review/desktop.png and mobile.png. Product and direction context: PRODUCT.md and .impeccable/surfaces/workbench.md. Sidecar tonal ramps are synthesized panel aids, not additional implemented palette tokens. -->
