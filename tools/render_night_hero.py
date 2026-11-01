"""A hand-drawn pixel landscape with a small stargazer and looping night sky.

Render at 400x150, then enlarge exactly 2x to preserve crisp pixel edges.
Requires Pillow. There is deliberately no text in the artwork.
"""
from math import cos, pi, sin
from pathlib import Path
from random import Random
from PIL import Image, ImageDraw, ImageChops

ROOT = Path(__file__).resolve().parents[1]
W, H, N = 400, 150, 48
rng = Random(18)
STARS = [(rng.randrange(8, 392), rng.randrange(5, 76), rng.randrange(N), rng.random() > .88) for _ in range(75)]


def tree(d, x, y, size, color):
    d.rectangle((x-1, y-size, x+1, y), fill=color)
    for j in range(4):
        top = y-size + j*size//6
        half = 2+j*2
        d.polygon([(x, top), (x-half, top+size//3), (x+half, top+size//3)], fill=color)


def landscape():
    im = Image.new('RGB', (W, H), '#0B0B21')
    d = ImageDraw.Draw(im)
    for y in range(20, 90, 10):
        # Flat colour bands give the sky the feel of a limited-palette game.
        k = (y-20)//10
        d.rectangle((0,y,W,y+10),fill=(15+k*3,13+k*2,37+k*5))

    # Small moon, deliberately built from blocky steps.
    d.ellipse((66,15,100,49), fill='#17152F')
    d.polygon([(77,21),(89,21),(89,23),(94,23),(94,28),(96,28),(96,39),(93,39),
               (93,43),(88,43),(88,45),(77,45),(77,43),(72,43),(72,38),(70,38),
               (70,28),(73,28),(73,24),(77,24)],fill='#C4B5FD')
    d.rectangle((78,25,81,28),fill='#A396CE')
    d.rectangle((86,35,91,39),fill='#A396CE')
    d.rectangle((76,37,79,39),fill='#A396CE')
    d.line((77,23,87,23),fill='#E5DAFF')

    # Distant lavender clouds and two overlapping mountain ridges.
    for x,y,l in [(16,60,40),(215,44,42),(287,64,50),(130,71,34)]:
        d.rectangle((x,y,x+l,y+2),fill='#322449')
        d.rectangle((x+8,y-2,x+l-12,y),fill='#322449')
    d.polygon([(0,90),(24,80),(37,82),(68,56),(93,80),(119,68),(147,94),
               (180,75),(207,83),(244,57),(279,85),(304,68),(340,92),(374,74),(400,90),(400,120),(0,120)],fill='#3F315B')
    d.polygon([(49,73),(68,56),(87,76),(73,67),(68,69),(64,64)],fill='#76628F')
    d.polygon([(227,73),(244,57),(262,74),(249,67),(244,70),(240,65)],fill='#76628F')
    d.polygon([(0,95),(40,88),(77,98),(107,82),(145,100),(179,91),(217,102),
               (256,86),(295,102),(330,89),(368,100),(400,91),(400,120),(0,120)],fill='#251D3D')
    for x in range(0,405,9):
        tree(d,x,105+rng.randrange(-3,4),rng.randrange(10,21),'#1A172C')

    # Lake and distant shoreline.
    d.rectangle((0,106,400,137),fill='#131426')
    d.line((0,106,400,106),fill='#514165')
    for x,y,l in [(15,111,24),(137,110,37),(233,117,27),(175,128,48),(32,124,28),(341,113,37)]:
        d.line((x,y,x+l,y),fill='#28223D')

    # Tiny lakeside cabin and its warm windows.
    d.rectangle((41,98,65,108),fill='#322535')
    d.polygon([(37,98),(52,87),(69,98)],fill='#100F21')
    d.line((39,97,52,88),fill='#79617C')
    d.rectangle((46,100,50,104),fill='#E5B786')
    d.rectangle((57,99,62,105),fill='#E5B786')
    d.line((59,99,59,105),fill='#694D57')
    d.rectangle((61,88,64,93),fill='#302132')

    # Foreground bank: all silhouettes have clear, stepped pixel outlines.
    d.polygon([(0,124),(24,126),(47,130),(66,133),(97,131),(126,138),(163,140),
               (199,138),(228,134),(265,132),(285,125),(308,124),(319,120),
               (337,119),(348,124),(371,120),(400,118),(400,150),(0,150)],fill='#080A17')
    d.line([(265,132),(285,125),(308,124),(319,120),(337,119),(348,124)],fill='#665078',width=1)
    for x,y,size in [(10,132,52),(24,135,37),(389,130,57),(373,133,39)]:
        tree(d,x,y,size,'#080A17')
    for x,y in [(31,139),(81,140),(183,147),(272,143),(354,137)]:
        d.line((x,y,x-2,y-5),fill='#21192F')
        d.line((x,y,x+3,y-4),fill='#21192F')
    return im


base = landscape()
frames = []
for frame in range(N):
    im = base.copy()
    d = ImageDraw.Draw(im)
    for x,y,phase,large in STARS:
        if 65<x<102 and 14<y<50:
            continue
        value = (cos((frame+phase)*2*pi/N)+1)/2
        color = '#E4DDF9' if value>.86 else '#9A87C1' if value>.42 else '#4D416B'
        d.point((x,y),fill=color)
        if large and value>.86:
            d.line((x-1,y,x+1,y),fill=color)
            d.line((x,y-1,x,y+1),fill=color)

    # Slow shimmer beneath the moon, never a full-screen flash.
    for j in range(7):
        y = 109+j*3
        x = 82 + round(sin(frame*2*pi/N+j)*3)
        half = 3+j
        shade = '#514267' if (frame//8+j)%3 else '#75618B'
        d.line((x-half,y,x+half,y),fill=shade)

    # A seated stargazer in a pale hoodie, looking left over the lake.
    d.rectangle((319,109,326,117),fill='#81709C')
    d.rectangle((319,107,325,111),fill='#C4B5DD')
    d.rectangle((317,102,324,108),fill='#E0D7EF')
    d.rectangle((316,104,319,107),fill='#A996BD')
    d.rectangle((317,102,322,103),fill='#F1E9FA')
    d.rectangle((315,114,322,118),fill='#50475E')
    d.rectangle((315,118,318,121),fill='#8E7BA4')
    d.rectangle((323,118,327,120),fill='#8E7BA4')
    # Scarf tips move only a pixel or two, preserving the quiet scene.
    scarf_y = 109 + (1 if sin(frame*2*pi/N)>0 else 0)
    d.rectangle((324,108,328,110),fill='#A78BFA')
    d.line([(328,109),(332,scarf_y),(335,scarf_y-1)],fill='#A78BFA',width=2)
    d.rectangle((327,112,330,117),fill='#392747')

    frames.append(im.resize((800,300),Image.Resampling.NEAREST))

palette = frames[0].quantize(colors=96,method=Image.Quantize.MEDIANCUT)
indexed = [im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
output = ROOT/'assets/profile-hero.gif'
indexed[0].save(output,save_all=True,append_images=indexed[1:],duration=140,loop=0,disposal=1,optimize=True)
frames[0].save(ROOT/'assets/profile-hero.png')
print(f'{output.name}: {output.stat().st_size:,} bytes; {N} frames; 800x300')
