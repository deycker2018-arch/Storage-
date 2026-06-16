import os
from PIL import Image, ImageDraw

size = 112
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Paleta de colores de Mindustry
BG_DARK = (45, 47, 54, 255)       
BORDER_MED = (73, 78, 89, 255)    
ACCENT_BLUE = (137, 221, 255, 255) 
ACCENT_GLOW = (0, 191, 255, 180)   
DARK_HOLE = (20, 21, 26, 255)     

#结构 Base
draw.rectangle([4, 4, size-5, size-5], fill=BORDER_MED)
draw.rectangle([8, 8, size-9, size-9], fill=BG_DARK)

# Esquineros
draw.rectangle([4, 4, 16, 16], fill=BORDER_MED)
draw.rectangle([size-17, 4, size-5, 16], fill=BORDER_MED)
draw.rectangle([4, size-17, 16, size-5], fill=BORDER_MED)
draw.rectangle([size-17, size-17, size-5, size-5], fill=BORDER_MED)

# Conductos
draw.rectangle([48, 8, 64, size-9], fill=BORDER_MED)
draw.rectangle([8, 48, size-9, 64], fill=BORDER_MED)

# Núcleo
center = size // 2
draw.ellipse([center-32, center-32, center+32, center+32], fill=BORDER_MED)
draw.ellipse([center-28, center-28, center+28, center+28], fill=BG_DARK)
draw.ellipse([center-20, center-20, center+20, center+20], fill=ACCENT_GLOW)
draw.ellipse([center-14, center-14, center+14, center+14], fill=ACCENT_BLUE)
draw.ellipse([center-8, center-8, center+8, center+8], fill=DARK_HOLE)

# Rejillas
for i in range(16, size-16, 20):
    draw.rectangle([i, 10, i+8, 14], fill=DARK_HOLE)
    draw.rectangle([i, size-15, i+8, size-11], fill=DARK_HOLE)
    draw.rectangle([10, i, 14, i+8], fill=DARK_HOLE)
    draw.rectangle([size-15, i, size-11, i+8], fill=DARK_HOLE)

# NUEVA UBICACIÓN PARA MINDUSTRY MOBILE
os.makedirs("sprites/blocks", exist_ok=True)
img_optimized = img.convert("P", palette=Image.ADAPTIVE, colors=256)
# Guardamos como exige el motor del juego: sprites/blocks/nombre-del-json.png
img_optimized.save("sprites/blocks/reactor-superpotente.png", "PNG", optimize=True)
print("¡Imagen guardada en la carpeta de texturas oficial!")
