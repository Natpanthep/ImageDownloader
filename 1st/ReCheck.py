import imagehash
from PIL import Image
import os

hashes = set()
duplicates = []

for root, _, files in os.walk('./dataset'):
    for f in files:
        try:
            path = os.path.join(root, f)
            h = imagehash.average_hash(Image.open(path))
            if h in hashes:
                duplicates.append(path)
            else:
                hashes.add(h)
        except:
            pass  # ภาพเสีย

for d in duplicates:
    os.remove(d)
