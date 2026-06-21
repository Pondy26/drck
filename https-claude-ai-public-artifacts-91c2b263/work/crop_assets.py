from pathlib import Path
from PIL import Image, ImageEnhance

source = Path(r"D:\Dr C K Japan\Dr C K\C K Web Site\Home page.png")
out = Path("outputs/assets")
out.mkdir(parents=True, exist_ok=True)
image = Image.open(source)

crops = {
    "hero.jpg": (300, 42, 863, 385),
    "portrait-autumn.jpg": (62, 479, 392, 715),
    "collaboration.jpg": (0, 1026, 451, 1210),
    "vision.jpg": (62, 1212, 389, 1331),
    "insight-temple.jpg": (60, 1354, 205, 1464),
    "insight-community.jpg": (214, 1354, 367, 1464),
    "insight-entrepreneurs.jpg": (377, 1354, 531, 1464),
    "insight-global.jpg": (542, 1354, 696, 1464),
    "moment-1.jpg": (21, 1604, 115, 1661),
    "moment-2.jpg": (120, 1604, 213, 1661),
    "moment-3.jpg": (218, 1604, 312, 1661),
    "moment-4.jpg": (317, 1604, 412, 1661),
    "moment-5.jpg": (417, 1604, 511, 1661),
    "moment-6.jpg": (516, 1604, 610, 1661),
    "moment-7.jpg": (615, 1604, 720, 1661),
}

for name, box in crops.items():
    crop = image.crop(box)
    crop = ImageEnhance.Sharpness(crop).enhance(1.12)
    crop.save(out / name, quality=92, optimize=True)
