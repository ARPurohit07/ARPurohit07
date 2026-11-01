"""Render a looping five-arm particle galaxy, adapted from the portfolio motif.

The repeated arm samples make the 72-degree rotation loop seamless.
Run with Python, NumPy and Pillow. No remote assets or rendering service.
"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

ROOT = Path(__file__).resolve().parents[1]
W, H, FRAMES = 960, 360, 64
rng = np.random.default_rng(23)

# The portfolio's five branches and spiral radius; project into an inclined disc.
count = 3500
r = rng.uniform(0.06, 1, count) ** 0.7
angle = r * 5.0 + rng.normal(0, 0.29, count)
height = rng.normal(0, 3.0, count) * r
radius = np.tile(r, 5)
angles = np.concatenate([angle + n * 2 * np.pi / 5 for n in range(5)])
z = np.tile(height, 5)
inside, outside = np.array([255, 217, 244]), np.array([109, 40, 217])
colors = inside[None, :] * (1 - radius[:, None]) + outside[None, :] * radius[:, None]
colors *= rng.uniform(.4, 1.0, (count, 1)).repeat(5, axis=1).T.reshape(-1, 1)

# A symmetric glowing core is static; only the spiral arms rotate.
yy, xx = np.mgrid[:H, :W]
core = np.exp(-((xx - 480) / 42) ** 2 - ((yy - 242) / 13) ** 2)
halo = np.exp(-((xx - 480) / 210) ** 2 - ((yy - 242) / 49) ** 2)
base = np.zeros((H, W, 3), dtype=np.float32)
base[:] = (3, 2, 8)
base += halo[:, :, None] * np.array([19, 8, 40])
base += core[:, :, None] * np.array([190, 159, 180])
bulge_x = np.rint(rng.normal(480, 28, 6000)).astype(int)
bulge_y = np.rint(rng.normal(242, 9, 6000)).astype(int)
np.add.at(base, (bulge_y, bulge_x), np.array([25, 21, 29]))
background = Image.fromarray(np.clip(base, 0, 255).astype('uint8'))
stars = ImageDraw.Draw(background)
for _ in range(100):
    x, y = int(rng.integers(16, W - 16)), int(rng.integers(16, H - 16))
    value = int(rng.integers(20, 70))
    stars.point((x, y), fill=(value, int(value * .8), min(255, value + 30)))

font = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 76)
frames = []
for i in range(FRAMES):
    a = angles + i / FRAMES * 2 * np.pi / 5
    x = np.rint(480 + radius * np.cos(a) * 420).astype(int)
    y = np.rint(242 + radius * np.sin(a) * 80 + z).astype(int)
    layer = np.zeros((H, W, 3), dtype=np.float32)
    np.add.at(layer, (y, x), colors)
    particles = Image.fromarray(np.clip(layer, 0, 255).astype('uint8'))
    glow = particles.filter(ImageFilter.GaussianBlur(1.4))
    frame = ImageChops.add(background, ImageChops.add(particles, glow))
    draw = ImageDraw.Draw(frame)
    draw.text((W / 2, 34), 'Rohan Purohit', font=font, anchor='mt', fill='#FFFFFF')
    # The small purple rule echoes the portfolio's pill-button accent.
    draw.rounded_rectangle((436, 136, 524, 139), radius=2, fill='#A78BFA')
    frames.append(frame)

# Match the 800px project assets; supersampling keeps the type smooth.
frames = [f.resize((800, 300), Image.Resampling.LANCZOS) for f in frames]
# One shared palette keeps the stationary typography and background stable.
palette = frames[0].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
indexed = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
output = ROOT / 'assets/profile-hero.gif'
indexed[0].save(output, save_all=True, append_images=indexed[1:], duration=120,
                loop=0, optimize=False, disposal=1)
frames[0].save(ROOT / 'assets/profile-hero.png')
print(f'{output.name}: {output.stat().st_size:,} bytes; {FRAMES} frames; 800x300')
