from PIL import Image
import math

img = Image.open('assets/img/logo.png').convert("RGBA")
datas = img.getdata()
newData = []
bg = (0, 10, 27)

def color_distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

for item in datas:
    r, g, b, a = item
    dist = color_distance((r,g,b), bg)
    if dist < 45:
        # Smooth alpha curve
        alpha = int((dist / 45.0) ** 1.5 * 255)
        # Prevent black fringing by boosting RGB to match a glowing blue/purple
        # We blend the color towards #00D4FF if it's very transparent
        newData.append((max(r, int(0 * (1-dist/45))), max(g, int(212 * (1-dist/45))), max(b, int(255 * (1-dist/45))), alpha))
    else:
        newData.append((r, g, b, 255))
        
img.putdata(newData)
img.save('assets/img/logo-horizontal.png', 'PNG')
print("Saved to assets/img/logo-horizontal.png")
