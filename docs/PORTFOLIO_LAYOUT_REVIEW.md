# Portfolio layout redesign

The project and toolkit sections were rebuilt around the user's pasted redesign brief. The fishing hero, casual introduction, Sun-to-centre Galaxy screenshot, public destinations and private source-code boundary are preserved.

## Design

- Two single-column project panels use native GitHub tables only as frames. Their headings, descriptions and compact stack labels remain selectable HTML text. Galaxy comes first; GoodFlow is identified as the featured local-AI build.
- Each panel has a short value proposition and a consistent linked SVG button. Portfolio and LinkedIn use the same button treatment.
- The toolkit uses four self-contained SVG panels with consistent icon sizes and adjacent labels. Panels form two columns at desktop width and wrap into a single column on phones. Technology names are not repeated as a separate list.
- Recognizable logo artwork is stored locally with its upstream license. Five concepts use deliberately simple illustrative glyphs rather than claiming to be official logos.

## Five review perspectives

- **Recruiter:** the project titles and value propositions precede technical detail; the main action is immediately visible.
- **GitHub visitor:** the live Galaxy demo and public GoodFlow repository have clear destinations. Private Galaxy source links remain absent.
- **Designer:** consistent card framing, violet buttons, local toolkit panels and short paragraphs replace long centered blocks and repeated icon captions.
- **Mobile viewer:** checked at a 390-pixel viewport. Both tables fit their container without internal horizontal scrolling; the toolkit wraps to one column, labels remain adjacent to icons, and all images load.
- **Technical reviewer:** descriptions retain the C++/WebAssembly/WebGL2 renderer, HYG/Gaia versus procedural-field distinction, and GoodFlow's local Qwen2.5-VL/Ollama workflow. The GoodFlow image remains explicitly identified as an illustration.

## Validation and limits

GitHub's Markdown API rendered the actual README markup. That output was inspected in a local preview with approximate GitHub dark-theme CSS, rather than claiming an authenticated GitHub-page screenshot. Desktop and mobile image loading, table widths, overflow and labels were inspected. Local paths, SVG XML/unique IDs, project ordering, public CTAs and `git diff --check` passed.

Screenshots: [desktop toolkit](toolkit-redesign-desktop.jpg), [mobile toolkit](toolkit-redesign-mobile.jpg), [mobile project card](project-cards-mobile.jpg).
