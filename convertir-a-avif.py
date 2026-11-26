"""
Convierte tus fotos a AVIF para que la web cargue más rápido.

Uso:
  1. Poné tus fotos en la carpeta  fotos-originales/  con estos nombres
     (JPG, PNG o WebP): hero, nido, fogon, alero, nosotros, galeria-1 ... galeria-4
  2. Instalá las dependencias (una sola vez):
        pip install pillow pillow-avif-plugin
  3. Ejecutá:
        python convertir-a-avif.py
  Las imágenes optimizadas quedan en  img/  listas para la web.
"""
from pathlib import Path
from PIL import Image
try:
    import pillow_avif  # noqa: F401  (solo hace falta en versiones viejas de Pillow)
except ImportError:
    pass

ENTRADA = Path("fotos-originales")
SALIDA = Path("img")
ANCHO_MAX = 1920   # px; las fotos más grandes se reducen
CALIDAD = 55       # 0-100; 50-60 es un buen equilibrio peso/calidad

SALIDA.mkdir(exist_ok=True)
for f in sorted(ENTRADA.iterdir()):
    if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
        continue
    im = Image.open(f).convert("RGB")
    if im.width > ANCHO_MAX:
        im = im.resize((ANCHO_MAX, round(im.height * ANCHO_MAX / im.width)), Image.LANCZOS)
    destino = SALIDA / (f.stem + ".avif")
    im.save(destino, format="AVIF", quality=CALIDAD)
    print(f"{f.name}: {f.stat().st_size//1024} KB -> {destino.name}: {destino.stat().st_size//1024} KB")
