from PIL import Image

try:
    img_path = '/Users/matiascardoso/.gemini/antigravity/brain/24cb3677-f62f-4904-8dc4-97c77d1273f8/.user_uploaded/media__1785808802681.png'
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    bg_color = img.getpixel((0,0))
    pixels = img.load()
    
    visited = set()
    # Start flood fill from all 4 corners and all edges just to be sure
    stack = []
    for x in range(width):
        stack.append((x, 0))
        stack.append((x, height-1))
    for y in range(height):
        stack.append((0, y))
        stack.append((width-1, y))
        
    def color_diff(c1, c2):
        return max(abs(c1[0]-c2[0]), abs(c1[1]-c2[1]), abs(c1[2]-c2[2]))
        
    while stack:
        x, y = stack.pop()
        if (x,y) in visited:
            continue
            
        c = pixels[x,y]
        if color_diff(c, bg_color) < 30:
            visited.add((x,y))
            # Set alpha to 0 for background
            pixels[x,y] = (c[0], c[1], c[2], 0)
            
            if x + 1 < width: stack.append((x+1, y))
            if x - 1 >= 0: stack.append((x-1, y))
            if y + 1 < height: stack.append((x, y+1))
            if y - 1 >= 0: stack.append((x, y-1))
            
    # For anti-aliasing pixels on the edge of the fill, we could do a second pass.
    # But a hard cut on a dark website will look fine if the original background was dark.
    img.save('assets/img/logo-horizontal.png', 'PNG')
    print("Fixed logo saved!")
except Exception as e:
    print("Error:", e)

