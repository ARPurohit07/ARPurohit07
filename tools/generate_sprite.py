"""Generate the small, looping pixel scene used in the profile README."""

from math import sin, pi
from pathlib import Path
from random import Random

from PIL import Image, ImageDraw


WIDTH, HEIGHT = 400, 120
SCALE = 2
FRAMES = 24
OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "galaxy-sprite.gif"

BG = "#0B1020"
STAR = "#CBD5E1"
BLUE = "#38BDF8"
PURPLE = "#A78BFA"

rng = Random(47)
stars = [(rng.randrange(WIDTH), rng.randrange(HEIGHT), rng.choice((1, 1, 1, 2)), rng.randrange(FRAMES)) for _ in range(72)]


def pixel(draw, x, y, color, size=1):
    draw.rectangle((x, y, x + size - 1, y + size - 1), fill=color)


def ship(draw, x, y, frame):
    # Hull, fins, cockpit and a short two-frame engine flame.
    draw.polygon([(x, y + 8), (x + 9, y + 3), (x + 26, y + 3), (x + 34, y + 8),
                  (x + 26, y + 13), (x + 9, y + 13)], fill="#E2E8F0")
    draw.rectangle((x + 10, y, x + 17, y + 3), fill="#64748B")
    draw.rectangle((x + 10, y + 13, x + 17, y + 16), fill="#64748B")
    draw.rectangle((x + 23, y + 6, x + 28, y + 9), fill=BLUE)
    draw.rectangle((x + 3, y + 6, x + 7, y + 10), fill="#334155")
    flame = 7 + (frame % 3) * 2
    draw.polygon([(x + 3, y + 7), (x - flame, y + 8), (x + 3, y + 10)], fill="#F59E0B")
    pixel(draw, x - flame - 4, y + 8, "#FDE68A", 2)


def planet(draw, frame):
    cx, cy, radius = 306, 64, 39
    # Chunked rings stay behind the planet.
    draw.ellipse((cx - 58, cy - 19, cx + 58, cy + 19), outline="#2DD4BF", width=3)
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill="#32235C")
    draw.ellipse((cx - radius + 4, cy - radius + 4, cx + radius - 4, cy + radius - 4), fill="#6D4BB0")
    draw.polygon([(cx - 29, cy - 8), (cx - 7, cy - 15), (cx + 22, cy - 8),
                  (cx + 27, cy), (cx - 7, cy - 2)], fill="#D8B4FE")
    draw.polygon([(cx - 28, cy + 12), (cx + 3, cy + 7), (cx + 29, cy + 14),
                  (cx + 18, cy + 25), (cx - 18, cy + 25)], fill="#4C3486")
    # Tiny surface highlights shift by a few pixels across the loop.
    offset = int(3 * sin(frame * 2 * pi / FRAMES))
    draw.rectangle((cx - 10 + offset, cy - 24, cx + 3 + offset, cy - 22), fill="#C4B5FD")
    draw.rectangle((cx + 13 - offset, cy + 6, cx + 22 - offset, cy + 8), fill="#C4B5FD")
    draw.arc((cx - radius, cy - radius, cx + radius, cy + radius), 210, 350, fill="#F59E0B", width=2)


images = []
for frame in range(FRAMES):
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)

    # Two speeds of scrolling stars, with deterministic twinkles.
    for x, y, size, phase in stars:
        drift = frame * (2 if size == 2 else 1)
        shade = BLUE if (frame + phase) % 12 < 2 else STAR if size == 2 else "#64748B"
        pixel(draw, (x - drift) % WIDTH, y, shade, size)
    for x, y in ((29, 23), (187, 34), (370, 96)):
        if frame % 12 < 8:
            draw.line((x - 3, y, x + 3, y), fill=BLUE)
            draw.line((x, y - 3, x, y + 3), fill=BLUE)

    draw.line((0, 109, WIDTH, 109), fill="#1E293B")
    draw.line((18, 113, 121, 113), fill="#334155")
    draw.line((270, 113, 382, 113), fill="#334155")
    planet(draw, frame)

    y = 52 + round(3 * sin(frame * 2 * pi / FRAMES))
    x = 107 + round(8 * sin(frame * 2 * pi / FRAMES))
    ship(draw, x, y, frame)
    images.append(image.resize((WIDTH * SCALE, HEIGHT * SCALE), Image.Resampling.NEAREST))

images[0].save(
    OUTPUT,
    save_all=True,
    append_images=images[1:],
    duration=90,
    loop=0,
    optimize=True,
    disposal=2,
)
print(f"{OUTPUT}: {OUTPUT.stat().st_size:,} bytes, {FRAMES} frames")
