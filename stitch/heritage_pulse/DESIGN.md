# Design System: Cultural Fusion Editorial

## 1. Overview & Creative North Star: "The Modern Heritage"
This design system rejects the clinical, sterile nature of traditional SaaS dashboards in favor of a **"Modern Heritage"** aesthetic. The goal is to blend the structural rigor of a premium financial institution with the soulful, artistic warmth of Indian craftsmanship. 

We move away from "flat" design by utilizing intentional asymmetry, editorial-scale typography, and deep tonal layering. This is not just a dashboard; it is a curated digital experience. We break the "template" look by treating the UI as a series of parchment-like surfaces layered over an Ivory canvas, using the high-contrast of Deep Maroon and Secondary Gold to guide the eye through a narrative flow rather than a rigid grid.

---

## 2. Colors & Surface Philosophy
The palette is rooted in earth and royalty. Ivory provides the breathable air, while Maroon and Gold provide the authority and prestige.

### The "No-Line" Rule
**Explicit Instruction:** 1px solid borders for sectioning are strictly prohibited. 
Structural boundaries must be defined solely through background color shifts or subtle tonal transitions. For instance, a side navigation panel should be `surface-container-low`, while the main content area sits on `surface`. This creates a seamless, high-end feel that mimics premium stationery rather than a wireframe.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of fine paper. 
- **Base Layer:** `surface` (#FCF9F2) for the overarching background.
- **Content Sections:** `surface-container-low` (#F6F3EC) for large background regions.
- **Interactive Cards:** `surface-container-lowest` (#FFFFFF) to provide a crisp, elevated focal point.
- **High-Impact Areas:** `primary_container` (#800000) for headers or call-outs, using `on_primary` text for maximum legibility.

### The "Glass & Gradient" Rule
To elevate beyond "out-of-the-box" UI, use **Glassmorphism** for floating elements (like dropdowns or modals). Use semi-transparent surface colors with a `backdrop-blur` of 12px–20px. 
**Signature Gradient:** For primary CTAs and hero states, utilize a linear gradient from `primary` (#570000) to `primary_container` (#800000) at a 135-degree angle. This adds "visual soul" and depth that flat hex codes cannot achieve.

---

## 3. Typography: Editorial Authority
The typography system uses a high-contrast pairing to balance heritage with modern utility.

*   **The Display Scale (Noto Serif):** Used for large numbers, page titles, and hero statements. The serif font provides the "Cultural" weight. Use `display-lg` (3.5rem) sparingly to create editorial impact.
*   **The UI & Navigation Scale (Manrope/Inter):** Used for density and clarity. Manrope’s geometric yet warm nature bridges the gap between the ornate headings and the functional data.
*   **Hierarchical Intent:** Always pair a `headline-sm` (Noto Serif) with a `label-md` (Inter) in all-caps for metadata. This "Big/Small" contrast is a hallmark of high-end editorial design.

---

## 4. Elevation & Depth
We convey hierarchy through **Tonal Layering** and **Ambient Light**, not structural scaffolding.

*   **The Layering Principle:** Instead of a shadow, place a `surface-container-lowest` card inside a `surface-container` section. The subtle shift in hex code creates a "natural lift."
*   **Ambient Shadows:** When a card must float (e.g., a hover state), use a shadow with a blur of `32px` at `6%` opacity. Use a tint of the `on-surface` color (#1C1C18) rather than pure black to keep the shadow feeling "organic."
*   **The "Ghost Border" Fallback:** If accessibility requires a border, use the `outline_variant` token at **15% opacity**. A 100% opaque border is a failure of the system's elegance.
*   **Motif Integration:** Use subtle Indian motifs (mandala patterns) as **watermarks** within `surface-container-high` sections. These should be at 3-5% opacity—visible only to the observant eye, providing a "hidden" layer of luxury.

---

## 5. Components & Primitive Styling

### Buttons
*   **Primary:** A gradient of `primary` to `primary_container`. Border-radius: `lg` (1rem). No border.
*   **Secondary:** `surface-container-lowest` with a `secondary` (#735C00) text color. Use a "Ghost Border" of the secondary color at 20% opacity.
*   **Tertiary:** Text-only in `primary`. Underline on hover with a 2px stroke of `secondary`.

### Cards & Lists
*   **No Dividers:** Forbid the use of line dividers. Use `spacing-6` (2rem) of vertical white space or a subtle background shift to `surface-container-low` to separate list items.
*   **Temple Borders:** For "Featured" cards, apply a subtle 4px top-border gradient of `secondary` to `secondary_fixed_dim`, mimicking a temple frieze.

### Input Fields
*   **Background:** `surface-container-high`.
*   **Focus State:** Shift background to `surface-container-lowest` and add a 1px "Ghost Border" of `secondary`. The transition should be a soft 300ms ease.

### Selection Chips
*   **Default:** `surface-container-highest` with `on_surface_variant` text.
*   **Selected:** `primary` background with `on_primary` text. Use `rounded-full` for a modern, pill-shaped contrast against the serif headings.

---

## 6. Do’s and Don’ts

### Do:
*   **Use Asymmetry:** Place a large serif heading off-center to create a "magazine" feel.
*   **Embrace Negative Space:** Let the `background` (Ivory) breathe. Information density should be managed through progressive disclosure, not cramped grids.
*   **Layer Textures:** Use a very subtle noise grain texture on `surface` layers to simulate high-quality paper.

### Don’t:
*   **Don't use pure black:** Use `tertiary` (#352312) or `on_surface` (#1C1C18) for all "black" elements to maintain warmth.
*   **Don't use 1px dividers:** If you feel the need for a line, use a wide gutter (Spacing 8) or a tonal shift instead.
*   **Don't over-decorate:** Motifs are accents, not the main event. If a motif distracts from the data, remove it. The "Cultural Fusion" is a whisper, not a shout.