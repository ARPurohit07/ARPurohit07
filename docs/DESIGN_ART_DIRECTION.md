# Galaxy art direction

## Harsh critique

The supplied screenshot is a control-panel dump, not a compelling project feature. Star labels collide; the bright top band, dense grid, overview, scale ladder, and bottom shortcuts compete equally. The tiny overview communicates “galaxy” better than the main scene. Soft text and crowded white points become visual noise at README width. Authenticity is good; this composition wastes it.

Reviewed: the supplied clipboard screenshot, current README, `assets/galaxy-preview.jpg`, `assets/profile-hero.png`, `assets/goodflow-card.svg`, and existing review notes. No live app inspection; controls below are conditional on actual availability.

## Capture brief for the main agent

- **Subject:** capture the real app's galaxy-scale view. Show the disc and recognizable spiral arms as the dominant subject, with one meaningful selected location if supported. Avoid the current crowded local-star neighborhood.
- **Camera:** start roughly 25–35 degrees away from face-on so arms remain legible and the disc has depth. Rotate its long axis slightly diagonally. Place the luminous core around 55% across and 45% down; keep the complete disc inside the frame with about 10% breathing room. Adjust by eye, not coordinates alone.
- **Hierarchy:** galaxy first, one location second, minimal native controls third. Use genuine app toggles to reduce labels and grid if available. Close search/help panels. Retain one compact orientation or scale cue; hide a redundant overview only through supported controls. If toggles are unavailable, choose a cleaner camera/zoom state rather than erase UI afterward.
- **Format:** target **16:9**, replacing the current shallow 8:3 strip. Capture a 1280 × 720 CSS viewport at device scale 2 if supported, saving the original 2560 × 1440 PNG. Higher resolution cannot fix a low-resolution app canvas: verify its rendering resolution and label sharpness. Avoid JPEG, upscaling, or sharpening the existing image.
- **Fallback:** if the galaxy view lacks enough structure, capture a sparse region with one selected star and readable native detail panel. Do not force a beautiful but uninformative view. Preserve a single dominant subject and the same 16:9 frame.
- **Authenticity:** use the live application at its real URL. No generated galaxy art, simulated interface, reconstructed labels, compositing, or painted purple overlays. Cropping may remove browser chrome but must not misrepresent application state. Keep native scientific colors.

## README composition and links

1. Preserve the text-free animated pixel night hero and reduced-motion still. Keep Galaxy first; GoodFlow follows.
2. Use an unlinked project heading, then two short sentences: what visitors can explore, followed by the C++ → WebAssembly/WebGL2 engineering contribution. Keep catalogue/procedural distinctions accurate.
3. Place the single real capture immediately below. No inset collage, decorative frame, badges, or text burned into the image. Write alt text describing the actual captured state.
4. Below the capture, use **[Explore the map](https://star-map-three.vercel.app)** as Galaxy's only public CTA. Remove Source code and Catalogue sources links; do not repeat the live link on the heading or image. The user reports the source repository is verified private (`isPrivate: true`); it must remain private. Do not change repository visibility or publish repository contents.
5. Match surrounding authored visuals to the existing purple family: deep night `#100C1A`, lavender `#A78BFA`, light lavender `#C4B5FD`. GitHub controls normal link colors; do not fake purple buttons. Leave the real app capture untinted.

## Acceptance check

Inspect at approximately 800 px desktop content width and 360 px mobile content width. In two seconds, the viewer should recognize the galaxy and locate the primary link. Desktop labels must be sharp and non-overlapping; mobile recognition must not depend on reading tiny UI. Reject captures with a clipped disc, blown-out core obscuring arms, or overlays dominating the scene. If the application cannot produce a cleaner truthful view, report that limit rather than fabricate one.

No emojis, vanity metrics, experience section, or BioLit. This handoff changes only `docs/DESIGN_ART_DIRECTION.md`; browser capture, README edits, and asset replacement belong to the main agent. No commit or push.
