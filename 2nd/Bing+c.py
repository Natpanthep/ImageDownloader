from icrawler.builtin import BingImageCrawler
from pathlib import Path
import uuid

def clean_filename(text):
    return text.replace(" ", "_").replace("/", "_")

def download_bing_images(keyword, view_type, max_num=100):
    # เปลี่ยน path ตรงนี้ได้ตามต้องการ
    base_path = Path(r"D:\Drone\my_dataset")
    folder = base_path / f"{view_type}_{clean_filename(keyword)}"
    folder.mkdir(parents=True, exist_ok=True)

    # ตั้งชื่อไฟล์ด้วย uuid เพื่อไม่ให้ซ้ำ
    def custom_naming(task, url, index):
        uid = uuid.uuid4().hex[:10]
        return str(folder / f"{view_type}_{clean_filename(keyword)}_{uid}.jpg")

    # เรียกใช้งาน Bing crawler
    crawler = BingImageCrawler(storage={"root_dir": str(folder)})
    crawler.downloader.rename = custom_naming
    crawler.crawl(keyword=keyword, max_num=max_num)
    print(f"✅ Downloaded {max_num} images for '{keyword}' to: {folder}")

# 🔽 Example เรียกใช้
download_bing_images("drone top view", "topview", max_num=350)
download_bing_images("drone side view", "sideview", max_num=350)
download_bing_images("quadcopter bottom", "underview", max_num=350)