from pathlib import Path
from PIL import Image
import imagehash
import os

def remove_duplicate_images(dataset_root):
    print(f"🔍 Scanning for duplicates in: {dataset_root}")
    image_hashes = set()
    duplicates = []

    dataset_path = Path(dataset_root)

    for image_path in dataset_path.rglob("*.*"):
        try:
            with Image.open(image_path) as img:
                img_hash = imagehash.average_hash(img)
            if img_hash in image_hashes:
                duplicates.append(image_path)
            else:
                image_hashes.add(img_hash)
        except Exception as e:
            print(f"⚠️ Failed to process {image_path}: {e}")

    print(f"\n🧹 Found {len(duplicates)} duplicate images. Deleting...")
    for dup in duplicates:
        try:
            os.remove(dup)
            print(f"🗑️ Deleted: {dup}")
        except Exception as e:
            print(f"❌ Failed to delete {dup}: {e}")

    print("\n✅ Done cleaning duplicates.")

# ✅ เรียกใช้งาน
remove_duplicate_images(r"D:\drone_dataset")
