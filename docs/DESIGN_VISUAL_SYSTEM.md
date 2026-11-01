# GoodFlow visual system

## Critique

The previous illustration looked like a generic slide placeholder. Its pale rectangle dominated the composition, the central stack of lines did not communicate a model, and the output graph had little visual connection to the night hero. With no stage labels, viewers had to read the caption to understand the conversion. Rounded containers and arbitrary spacing weakened the pixel vocabulary.

The supplied Galaxy screenshot has a separate problem: dense stars, overlapping labels, grid lines, navigation overlays, and a bright inset compete for attention. At README size, that becomes visual clutter. Galaxy should remain the lead project, but its presentation needs a clearer focal point. Galaxy assets are outside this write scope.

## Implemented direction

`assets/goodflow-card.svg` is a static 800 × 208 vector illustration. Three aligned stages communicate **Screenshot → Local model → Editable diagram**. Input and output use identical branching topology; selection handles indicate editability. A geometric chip represents local computation without pretending to depict the application's interface.

- Night background: `#0D0B1C` to `#171129`.
- Recessed surfaces: `#140F24`, `#281A40`.
- Purple structure: `#71529A`, `#AE8BE7`.
- Primary highlights: `#C6A7FF`, `#E0C9FF`.
- Label color: `#DDD0EF`.
- Pixel vocabulary: stepped corners, square stars, chip pins, square selection handles, stepped arrowheads.
- Typography: three essential labels at 15 px; no text inside nodes or decorative microcopy. Native monospace fallbacks avoid external font dependencies.
- Geometry: mostly 2 px strokes and integer coordinates; no blur, glow, embedded raster images, or external resources. Sparse stars connect to the hero without becoming another star field.

The input image is lighter than the processing and output stages, but compact and tinted lavender. The chip provides a central anchor. Matching graph shapes make conversion understandable even when labels become small on narrow screens. SVG preserves edge quality when scaled; essential labels and accessible descriptions carry the meaning without relying on color alone.

## Boundaries

This is an illustration, not a screenshot or a proposed product interface. It contains no invented application chrome or product controls. SVG title and description identify the transformation and illustration status. The existing README caption also identifies it as an illustration.

Only `assets/goodflow-card.svg` and this document belong to this design scope. README, the text-free animated night hero, and Galaxy assets remain outside it. No emojis, vanity metrics, experience section, or BioLit content are introduced. No commit or push is part of this work.

## Verification

XML parsing and the scoped whitespace check passed. Dimensions and the three essential labels were verified. Browser visual verification could not complete: the bundled Chromium executable was unavailable, and installed Edge exited before rendering. No preview files were added outside the two assigned deliverables.
