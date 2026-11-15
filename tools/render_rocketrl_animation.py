"""Render the RocketRL card as a short, looping landing animation."""

from io import BytesIO
from pathlib import Path
import os

from PIL import Image
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "rocketrl-card.svg"
OUTPUT = ROOT / "assets" / "rocketrl-landing.gif"

# Descend, settle on the pad, then rise so the loop reconnects smoothly.
HEIGHTS = [90, 91, 93, 96, 100, 105, 111, 117, 122, 125, 125, 125,
           125, 125, 125, 122, 117, 111, 105, 99, 94, 90]
DURATIONS = [105] * len(HEIGHTS)
DURATIONS[11:15] = [170, 170, 170, 170]


def main() -> None:
    svg = SOURCE.read_text(encoding="utf-8")
    frames = []
    with sync_playwright() as playwright:
        chrome = os.environ.get("CHROME_PATH")
        if not chrome:
            candidates = [
                Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
                Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
            ]
            chrome = next((str(path) for path in candidates if path.exists()), None)
        options = {"headless": True}
        if chrome:
            options["executable_path"] = chrome
        browser = playwright.chromium.launch(**options)
        page = browser.new_page(viewport={"width": 800, "height": 210}, device_scale_factor=1)
        page.set_content(f'<html><body style="margin:0;background:#100e20">{svg}</body></html>')
        card = page.locator("svg").first
        for y in HEIGHTS:
            flame_opacity = 0 if y >= 124 else max(0.25, (124 - y) / 34)
            page.evaluate(
                """([y, opacity]) => {
                    document.querySelector('#rocket').setAttribute('transform', `translate(210 ${y})`);
                    document.querySelector('#flame').setAttribute('opacity', String(opacity));
                }""",
                [y, flame_opacity],
            )
            frames.append(Image.open(BytesIO(card.screenshot())).convert("RGB"))
        browser.close()

    palette = frames[0].quantize(colors=192)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(
        OUTPUT,
        save_all=True,
        append_images=indexed[1:],
        duration=DURATIONS,
        loop=0,
        disposal=2,
        optimize=True,
    )
    print(f"Rendered {len(indexed)} frames to {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
