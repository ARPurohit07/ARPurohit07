# Profile review: five independent judges

These are subjective baseline assessments of the profile before the revisions in this review. Judges reviewed the README and local artwork independently. They did not all inspect the live application or GitHub rendering; each review states its limits. No post-change scores are claimed.

## Art director (Anscombe)

**Art direction: 6/10.** The night hero establishes atmosphere. The project images occupy substantial space without showing enough about the work.

**Observed flaws, ranked**

1. **Galaxy’s image sells the wrong experience.** `assets/galaxy-sprite.gif` shows a spacecraft beside a large ringed planet—visually suggesting an arcade game, while the README describes an astronomical exploration tool. **Smallest good fix:** replace this banner with one actual Galaxy view showing spatial depth and a selected celestial object. Keep Galaxy first.

2. **The approved hero needs clearer lighting and silhouette work.** In `assets/profile-hero.png` and `.gif`, the stargazer’s bright square head dominates its indistinct body; the forest and shoreline merge into a dark strip. The lake’s reflection resembles stacked horizontal rungs. **Smallest good fix:** redraw the seated figure with readable knees, torso and gaze; add a restrained lavender rim light; break the reflection into irregular, tapering pixel clusters. Preserve the moon, cabin, mountains, lake and text-free composition.

3. **Image proportions flatten the hierarchy.** `README.md` displays all three images at full width: the hero is 800×300, and each project visual is 800×240. Each illustration gets nearly hero-level space regardless of information density. **Smallest good fix:** retain the hero’s dimensions, give Galaxy a useful product view, and reduce GoodFlow’s decorative strip to roughly 140–160 pixels high at 800 pixels wide.

4. **Purple is shared, but the palette lacks discipline.** The hero uses subdued dusty purples; Galaxy introduces much stronger violet plus a conspicuous orange planetary rim and exhaust. GoodFlow’s SVG explicitly uses `#A78BFA`, but its blue-grey rules introduce another accent. **Smallest good fix:** use `#a78bfa` for selected highlights and `#6d28d9` for saturated midtones, with darker derived shades. Keep warm light concentrated in the cabin; remove Galaxy’s orange rim.

5. **GoodFlow communicates only a generic conversion.** `assets/goodflow-card.svg` turns a landscape-image icon into blank nodes. It doesn’t visually establish workflow recognition or editability, and its smooth rounded geometry differs from the pixel artwork. **Smallest good fix:** replace the landscape icon with a miniature photographed flowchart and show corresponding output nodes with one selection handle.

**Keep:** Galaxy first, GoodFlow second; approved night scene; sparse stars; no header text; restrained cabin warmth.

**Change:** hero lighting and pixel clusters, project-image usefulness, palette consistency, GoodFlow height.

**Remove:** redundant decorative rules beneath Galaxy and around GoodFlow.

**Uncertainty:** I inspected both hero assets, sampled GIF frames and a rendered SVG. Live animation smoothness and GitHub’s mobile rendering remain unverified. Portfolio matching is assessed against your supplied hex values. No repository files changed.

---

## Skeptical engineering recruiter (Jason)

**Score: 6/10 — skeptical engineering recruiter.** The engineering signal is credible but arrives after substantial decoration. In ten seconds, I learn your broad interests more readily than what distinguishes your work.

Observed flaws, ranked:

1. **Project visuals illustrate themes rather than demonstrate software.** [Galaxy’s sprite](C:/Users/rohan/OneDrive/Desktop/Game_tst/assets/galaxy-sprite.gif) shows a spaceship and planet; [GoodFlow’s card](C:/Users/rohan/OneDrive/Desktop/Game_tst/assets/goodflow-card.svg) is a schematic. Neither establishes that the described interaction works. **Smallest fix:** put each project’s functional description and stack above its visual. Replace illustrations with actual application captures when available; do not fabricate interfaces.

2. **The strongest differentiator is buried.** In [README.md](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md), “interactive graphics, applied AI, and computer vision” could describe thousands of applicants. C++/WebAssembly graphics and local model integration are more specific. **Smallest fix:** use existing facts in the opening: “Software engineer building interactive 3D graphics with C++/WebAssembly and image-to-diagram tools with local vision-language models.”

3. **Decoration delays evidence.** The full-width hero is 800×300; Galaxy adds another 800×240 image before its explanatory paragraph. At their native widths, that is 540 pixels of artwork before readers finish the first project’s pitch. **Smallest fix:** retain the approved text-free, twinkling hero, but display it more compactly; move Galaxy’s description ahead of its animation.

4. **The technology wall exceeds the visible evidence.** The README lists eleven icons, including Node.js, PyTorch, PostgreSQL, and Docker, without connecting those four to the featured projects. This is an inventory, not demonstrated proficiency. **Smallest fix:** remove the icon section and let the explicit project stacks carry the skills signal. This questions presentation, not whether you know those tools.

5. **The recruiting intent is last, and the closing action is vague.** “Open to software engineering and applied AI opportunities” appears below the technology section; “Explore my work” repeats the portfolio destination. **Smallest fix:** move availability beneath the introduction and retain the existing Portfolio button. No new contact details are needed.

**Keep:** Galaxy first, GoodFlow second; purple palette; approved text-free hero; concise project descriptions; direct demo/source links.

**Change:** opening specificity, image prominence, description placement, availability placement.

**Remove:** redundant technology wall and closing portfolio invitation.

**Uncertainty:** I inspected local content and image frames, not a rendered GitHub page, live applications, or linked source repositories. Exact fold position, animation quality, link accessibility, and implementation claims remain unverified. No repository files were changed.

---

## Senior software engineer (Heisenberg)

**Score: 5/10 — technical portfolio evidence.** The README identifies two concrete products, but its visuals sell atmosphere and its descriptions leave the difficult engineering unsubstantiated.

Observed flaws, ranked:

1. **Galaxy’s visual does not demonstrate Galaxy.** [galaxy-sprite.gif](C:/Users/rohan/OneDrive/Desktop/Game_tst/assets/galaxy-sprite.gif) shows a pixel spaceship and ringed planet, not the advertised astronomical map. Your first project’s largest visual proves nothing about navigation, data, or rendering. **Smallest good fix:** replace this project illustration with a short actual screen recording showing navigation and object inspection. Keep the approved hero.

2. **“True-scale” is a strong, undefined claim.** The Galaxy paragraph in [README.md](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md:15) names “astronomical catalogues” without identifying them or explaining scale. Readers cannot distinguish catalogue-derived positions from illustrative placement, or positional scale from enlarged object markers. **Smallest good fix:** name the catalogues actually used and explain what “true-scale” covers, including any visual exaggeration.

3. **GoodFlow shows a concept, not a demonstrated transformation.** [goodflow-card.svg](C:/Users/rohan/OneDrive/Desktop/Game_tst/assets/goodflow-card.svg) contains a generic image symbol, arrow, and diagram shapes. It supplies no actual input, extracted labels, editor interface, or export. The description also leaves “then export” unspecified. **Smallest good fix:** show one real workflow image beside its resulting editable diagram; name the local model and supported export formats.

4. **Technology lists substitute for engineering substance.** Both project descriptions name frameworks but explain no implementation decision or personal contribution. C++, WebGL2, and WebAssembly are potentially compelling, yet their respective roles remain unclear. **Smallest good fix:** add one factual sentence per project explaining what you implemented and one consequential design choice—for example, the C++/browser boundary or how model output becomes an editable graph.

5. **The technology grid exceeds the demonstrated scope.** [Technologies](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md:27) includes PyTorch, PostgreSQL, Docker, and Node.js without connecting them to either featured project. These are unsupported signals, not necessarily false claims. **Smallest good fix:** retain only technologies supported by the showcased work, or connect each additional tool to a concrete artifact.

**Keep:** Galaxy first, GoodFlow second; purple palette; approved text-free pixel night hero; concise structure and direct project links.

**Change:** project visuals, claim precision, implementation specificity.

**Remove:** unsupported tool icons and unqualified “true-scale” wording until substantiated.

**Uncertainty:** live-site retrieval failed; functionality and implementation claims remain unverified, not disproven. Private repository visibility is not a flaw. No files changed.

---

## Accessibility and mobile specialist (Epicurus)

**Accessibility/mobile score: 6.5/10.** Readable prose and sensible project order, but motion handling and the technology strip need work. No files changed.

Observed flaws, ranked:

1. **Uncontrolled looping animation.** [README.md:1](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md:1) embeds the hero GIF; line 14 embeds Galaxy’s GIF. Both loop indefinitely: 6.72 seconds and 2.16 seconds per cycle. There is no static selection or pause mechanism in the markup. This creates avoidable distraction and motion exposure. **Smallest fix:** retain the approved animated hero, but select the existing PNG for reduced-motion users; provide a still for Galaxy too. GitHub supports [`<picture>`](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#the-picture-element); using `prefers-reduced-motion` is a candidate requiring GitHub verification. A static image with an explicit animation link is the dependable fallback.

2. **Thirteen image elements depend on external services.** [README.md:6](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md:6) uses two Shields badges; lines 31–42 use eleven skillicons images. The technology section has no visible text labels while images load normally, forcing sighted readers to recognize logos. Failed loading leaves presentation dependent on browser alt-text handling. **Smallest fix:** use ordinary text links for the two badges and a wrapping text list for technologies, or store icons locally with visible labels.

3. **Image-link alternatives emphasize illustration over destination.** [README.md:22](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md:22) names a transformation but never identifies GoodFlow or its repository. Galaxy’s alternative leads with decorative scenery. Each card also repeats destinations already linked in its heading and footer, adding keyboard stops. **Smallest fix:** remove redundant card links, or use concise functional alternatives: “Open Milky Way Star Map” and “View GoodFlow repository.”

4. **Technology layout encodes a desktop row.** [README.md:31](C:/Users/rohan/OneDrive/Desktop/Game_tst/README.md:31) places seven 40-pixel icons before a forced break: 280 pixels before whitespace. Narrow content areas will require additional wrapping, potentially producing awkward fragments. **Smallest fix:** remove the forced `<br>` and use naturally wrapping, labeled content.

**Needs rendering verification:** actual overflow at 320/375 pixels, badge wrapping, zoom behavior, GoodFlow’s fine connector visibility, reduced-motion image selection, and link availability. GIF timing alone does **not** establish hazardous flashing.

- **Keep:** Galaxy first, GoodFlow second; purple palette; text-free pixel-night hero; concise project descriptions; percentage-width artwork.
- **Change:** motion alternatives, technology presentation, linked-image names.
- **Remove:** forced technology break and redundant card links.

---

## Ruthless editorial minimalist (Descartes)

**Score: 6.5/10 — ruthless editorial minimalism.** The projects contain useful substance, but repeated links, ornamental banners, and a technology inventory dilute it.

Observed issues, ranked:

1. **Too many routes to the same destination.**  
   **Evidence:** `README.md` links Galaxy through its badge, heading, image, and “Explore the map.” GoodFlow has three repository links; the portfolio appears twice.  
   **Why it hurts:** Repeated invitations compete without offering different actions.  
   **Smallest fix:** Keep one plain “Portfolio” link near the introduction. Use unlinked project headings and images, followed by **“Explore the map · Source code”** for Galaxy and **“View repository”** for GoodFlow. Delete the closing “Explore my work.”

2. **Galaxy’s banner repeats the atmosphere without explaining the project.**  
   **Evidence:** `assets/galaxy-sprite.gif` depicts a spaceship and ringed planet; `README.md` displays it at full width beneath the already substantial night-sky hero.  
   **Why it hurts:** A second space illustration consumes attention while suggesting a game more readily than an astronomical map.  
   **Smallest fix:** Remove the Galaxy banner from the README. Keep Galaxy first and preserve the approved text-free, twinkling hero.

3. **The technology section reads like inventory.**  
   **Evidence:** Eleven icons in `README.md`, including several technologies already named in the project descriptions.  
   **Why it hurts:** Familiar logos add little evidence of capability; the project stacks are more informative.  
   **Smallest fix:** Remove the entire “Technologies” section. Keep the stacks beside the work they explain.

4. **The opening and closing use generic professional language.**  
   **Evidence:** “working across interactive graphics, applied AI, and computer vision”; “Open to software engineering and applied AI opportunities.”  
   **Why it hurts:** Broad categories obscure the specific work immediately below.  
   **Smallest fix:** Open with **“Software engineer building interactive maps and AI-assisted diagram tools.”** If availability matters, close with **“B.E. in Computer Science. Seeking software engineering or applied AI roles.”**

5. **GoodFlow’s illustration is less specific than its description.**  
   **Evidence:** `assets/goodflow-card.svg` shows a landscape-image symbol becoming a graph.  
   **Why it hurts:** It implies arbitrary image conversion rather than workflow-image conversion.  
   **Smallest fix:** Replace only the landscape symbol with a miniature photographed or scanned flowchart.

**Keep:** Galaxy first; GoodFlow second; purple palette; approved hero; concrete project capabilities and stacks.  
**Change:** Intro, availability sentence, GoodFlow input symbol, link hierarchy.  
**Remove:** Galaxy banner, technology icons, duplicate CTAs.

**Uncertainty:** GIF timing, live GitHub layout, destination access, and “true-scale” accuracy were not verified. No files changed.

## Implementation decisions

- Keep the approved text-free purple pixel night hero and Galaxy-first ordering.
- Improve the seated figure, shoreline separation and broken moonlight reflections.
- Replace the decorative Galaxy animation in the README with a real application capture.
- Put specific project explanations before supporting visuals; remove duplicate image/heading links.
- Replace GoodFlow's landscape-input symbol with a workflow-input diagram; label it as an illustration.
- Keep six core technology icons with text labels, honoring the user's icon preference while reducing clutter.
- Provide a still hero for reduced-motion preferences, and test GitHub's preserved markup.
- Preserve privacy; no BioLit, employer history, vanity metrics, invented achievements or contact details.

## Implemented and verified

- Galaxy now uses an actual capture of the live application, with its search context, named stars, spatial grid and overview visible. It remains the first project.
- The introduction names the work and technologies directly. Catalogue-based positions are distinguished from the procedural galaxy field, and the verified catalogue source file is linked.
- GoodFlow now has a compact 800 × 160 workflow illustration with corresponding input/output topology and editing handles. It is explicitly labeled as an illustration. A real GoodFlow interaction capture remains a useful future improvement; none was fabricated.
- The hero retains its 800 × 300 proportions and animation, with refined stargazer anatomy, shoreline lighting and irregular reflection clusters.
- The six-icon row has readable text labels. One external icon-image service remains; the other artwork is stored in this repository.
- The local README preview was inspected at desktop and 390-pixel phone widths. All four images loaded, proportions were preserved and there was no horizontal overflow. Preview screenshots use approximate GitHub dark-theme styling, not a capture of the authenticated GitHub profile page.
- The browser reported reduced motion enabled and selected the static PNG. GitHub's Markdown API also preserved the picture/source media query. Animation remains the default fallback for other preferences.
- Portfolio, Galaxy and source links were checked against their actual sites or GitHub API results. No visibility change was made.

Preview evidence: [desktop](profile-preview-desktop.jpg), [desktop projects](profile-preview-projects.jpg), [phone](profile-preview-mobile.jpg), [phone projects](profile-preview-mobile-projects.jpg).

