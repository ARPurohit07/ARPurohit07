"""A hand-drawn pixel landscape with a fishing sprite and looping night sky.

Render at 400x150, then enlarge exactly 2x to preserve crisp pixel edges.
Requires Pillow. There is deliberately no text in the artwork.
"""
from math import cos, pi, sin
from pathlib import Path
from random import Random
from PIL import Image, ImageDraw

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
    d.line((77,23,87,23),fill='#D9E8FF')
    d.line((73,25,71,30),fill='#9ABFF1')

    # Distant lavender clouds and two overlapping mountain ridges.
    for x,y,l in [(16,60,40),(215,44,42),(287,64,50),(130,71,34)]:
        d.rectangle((x,y,x+l,y+2),fill='#322449')
        d.rectangle((x+8,y-2,x+l-12,y),fill='#322449')
    d.polygon([(0,90),(24,80),(37,82),(68,56),(93,80),(119,68),(147,94),
               (180,75),(207,83),(244,57),(279,85),(304,68),(340,92),(374,74),(400,90),(400,120),(0,120)],fill='#3F315B')
    d.polygon([(49,73),(68,56),(87,76),(73,67),(68,69),(64,64)],fill='#76628F')
    d.polygon([(227,73),(244,57),(262,74),(249,67),(244,70),(240,65)],fill='#76628F')
    d.line([(68,57),(62,65),(57,69),(53,75)],fill='#92A8D4')
    d.line([(244,58),(238,67),(233,71)],fill='#92A8D4')
    d.polygon([(0,95),(40,88),(77,98),(107,82),(145,100),(179,91),(217,102),
               (256,86),(295,102),(330,89),(368,100),(400,91),(400,120),(0,120)],fill='#251D3D')
    for x in range(0,405,9):
        tree(d,x,105+rng.randrange(-3,4),rng.randrange(10,21),'#1A172C')

    # Lake and distant shoreline.
    d.rectangle((0,106,400,137),fill='#10192D')
    d.line((0,106,400,106),fill='#52658B')
    d.line((106,107,177,107),fill='#2B3D61')
    d.line((207,108,263,108),fill='#2B3D61')
    for x,y,l in [(15,111,24),(137,110,37),(233,117,27),(175,128,48),(32,124,28),(341,113,37)]:
        d.line((x,y,x+l,y),fill='#233455')

    # Tiny lakeside cabin and its warm windows.
    d.rectangle((41,98,65,108),fill='#322535')
    d.polygon([(37,98),(52,87),(69,98)],fill='#100F21')
    d.line((39,97,52,88),fill='#79617C')
    d.rectangle((46,100,50,104),fill='#E5B786')
    d.rectangle((57,99,62,105),fill='#E5B786')
    d.line((59,99,59,105),fill='#694D57')
    d.rectangle((61,88,64,93),fill='#302132')
    d.line((43,110,51,110),fill='#67505E')
    d.line((56,112,62,112),fill='#59424E')
    d.line((49,115,59,115),fill='#3D303F')

    # Foreground bank: all silhouettes have clear, stepped pixel outlines.
    d.polygon([(0,124),(24,126),(47,130),(66,133),(97,131),(126,138),(163,140),
               (199,138),(228,134),(265,132),(285,125),(308,124),(319,120),
               (337,119),(348,124),(371,120),(400,118),(400,150),(0,150)],fill='#080A17')
    d.line([(265,132),(285,125),(308,124),(319,120),(337,119),(348,124)],fill='#665078',width=1)
    d.line([(281,127),(292,126),(298,126)],fill='#8CAAD2')
    d.line([(332,121),(339,122),(343,124)],fill='#A396B4')
    d.line([(298,128),(307,127),(310,129)],fill='#30263F')
    for x,y,size in [(10,132,52),(24,135,37),(389,130,57),(373,133,39)]:
        tree(d,x,y,size,'#080A17')
    for x,y in [(31,139),(81,140),(183,147),(272,143),(354,137)]:
        d.line((x,y,x-2,y-5),fill='#21192F')
        d.line((x,y,x+3,y-4),fill='#21192F')
    return im


base = landscape()
sky_colors = {(11,11,33)} | {(15+k*3,13+k*2,37+k*5) for k in range(7)}
frames = []
for frame in range(N):
    im = base.copy()
    d = ImageDraw.Draw(im)
    for x,y,phase,large in STARS:
        if base.getpixel((x,y)) not in sky_colors:
            continue
        value = (cos((frame+phase)*2*pi/N)+1)/2
        color = '#DCEBFF' if value>.86 else '#9A9ED5' if value>.42 else '#4D416B'
        d.point((x,y),fill=color)
        if large and value>.86:
            d.line((x-1,y,x+1,y),fill=color)
            d.line((x,y-1,x,y+1),fill=color)

    # Slow shimmer beneath the moon, never a full-screen flash.
    for j,(y,offset,half) in enumerate([(109,-1,3),(112,2,5),(115,-4,4),(118,1,7),
                                      (122,-3,6),(126,4,9),(130,-1,8)]):
        x = 82 + offset + round(sin(frame*2*pi/N+j)*2)
        shade = '#465D83' if (frame//8+j)%3 else '#849FD0'
        d.line((x-half,y,x-2,y),fill=shade)
        d.line((x+1,y,x+half//2,y),fill=shade)
        d.point((x+half,y+1),fill='#30466A')

    # Fishing line, float and small expanding ripples, drawn on the lake.
    bob = round(sin(frame*2*pi/N)*1.2)
    rod_lift = 1 if 18 <= frame < 30 else 0
    tip_x, tip_y = 286, 91-rod_lift
    float_x, float_y = 278, 119+bob
    d.line([(315,111),(307,99),(296,91-rod_lift),(tip_x,tip_y)],fill='#A4B6D5')
    d.line([(315,111),(310,104)],fill='#796193',width=2)
    d.line([(tip_x,tip_y),(283,103),(float_x,float_y-2)],fill='#6685B0')
    ripple = 2 + (frame//6)%4
    ripple_color = '#45658B' if ripple < 4 else '#2A4161'
    d.line((float_x-ripple,float_y+2,float_x-2,float_y+2),fill=ripple_color)
    d.line((float_x+2,float_y+2,float_x+ripple,float_y+2),fill=ripple_color)
    d.point((float_x-ripple-1,float_y+1),fill='#304F75')
    d.rectangle((float_x,float_y-2,float_x+1,float_y-1),fill='#C4B5FD')
    d.rectangle((float_x,float_y,float_x+1,float_y+1),fill='#7DBEFA')
    # A faint fish passes beneath the surface, turning back in the loop.
    fish_x = 226 + round(sin(frame*2*pi/N)*12)
    facing = 1 if cos(frame*2*pi/N)>0 else -1
    d.line((fish_x-2,123,fish_x+2,123),fill='#29476D')
    d.point((fish_x-3*facing,122),fill='#29476D')
    d.point((fish_x-3*facing,124),fill='#29476D')

    # A seated fisher in a pale hoodie, hands wrapped around the rod.
    d.rectangle((320,108,326,115),fill='#81709C')
    d.rectangle((319,108,324,111),fill='#B5A7CB')
    d.polygon([(318,101),(322,101),(324,103),(324,107),(319,108),(317,106),(317,103)],fill='#BAACD0')
    d.line((319,101,322,101),fill='#DFD5EC')
    d.rectangle((317,104,319,106),fill='#6E597D')
    d.line([(320,110),(317,111),(314,111)],fill='#BBD1ED',width=2)
    d.point((314,110),fill='#E0D0DF')
    d.polygon([(319,114),(325,115),(324,118),(319,117),(316,115),(314,116),(314,120),(312,120),(312,114),(315,112)],fill='#625771')
    d.line([(314,113),(317,114),(320,116)],fill='#A89ABB')
    d.rectangle((312,120,316,121),fill='#A89ABB')
    d.rectangle((321,118,325,120),fill='#8E7BA4')
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
