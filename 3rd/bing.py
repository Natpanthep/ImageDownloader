import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from pathlib import Path
import uuid
from multiprocessing import Pool, cpu_count

def clean_filename(text):
    return text.replace(" ", "_").replace("/", "_")

def download_images_bing(args):
    query, save_base, max_images = args
    view_type = clean_filename(query.split()[1]) if " " in query else "general"
    save_dir = Path(save_base) / f"{view_type}_{clean_filename(query)}"
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    query_encoded = quote(query)
    url = f"https://www.bing.com/images/search?q={query_encoded}&form=HDRSC2"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")
        image_elements = soup.find_all("a", class_="iusc")
    except Exception as e:
        print(f"❌ Failed to fetch results for {query}: {e}")
        return

    count = 0
    for img in image_elements:
        if count >= max_images:
            break
        try:
            m = img.get("m")
            if not m:
                continue
            m_url = m.split('"murl":"')[1].split('"')[0]
            ext = m_url.split(".")[-1].split("?")[0]
            if ext.lower() not in ["jpg", "jpeg", "png", "webp"]:
                ext = "jpg"
            filename = f"{clean_filename(query)}_{uuid.uuid4().hex[:8]}.{ext}"
            filepath = save_dir / filename
            r = requests.get(m_url, timeout=10)
            with open(filepath, "wb") as f:
                f.write(r.content)
            count += 1
            print(f"[{query}] ({count}) Saved: {filename}")
        except Exception as e:
            print(f"[{query}] ❌ Failed to download image: {e}")

# ✅ รายการ keyword ที่ต้องการดาวน์โหลด
keywords = [
    "drone top view",
    "drone side view",
    "drone under view",
    "military drone side",
    "uav flying over city",
    "agriculture drone spraying",
    "inspection drone industrial",
    "drone with camera from above",
    "drone aerial photography",
    "drone landscape view",
    "drone over forest",
    "drone over water",
    "drone over mountains",
    "drone over fields",
    "drone over cityscape",
    "drone over construction site",
    "drone over power lines",
    "drone over solar panels",
    "drone over wind turbines",
    "drone over crops",
    "drone over farm",
    "drone"
]

if __name__ == "__main__":
    # ตั้งค่าพื้นที่จัดเก็บ
    save_base_path = r"D:\drone_dataset"
    max_images_per_keyword = 250

    # เตรียม arguments สำหรับ multiprocessing
    tasks = [(kw, save_base_path, max_images_per_keyword) for kw in keywords]

    # ใช้ multiprocessing เท่ากับจำนวน CPU (หรือจะปรับตามต้องการ)
    with Pool(processes=cpu_count()) as pool:
        pool.map(download_images_bing, tasks)

























# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import quote
# from pathlib import Path
# import uuid

# def download_images_bing(query, save_dir, max_images=100):
#     query_encoded = quote(query)
#     url = f"https://www.bing.com/images/search?q={query_encoded}&form=HDRSC2"

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }

#     resp = requests.get(url, headers=headers)
#     soup = BeautifulSoup(resp.text, "html.parser")
#     image_elements = soup.find_all("a", class_="iusc")

#     Path(save_dir).mkdir(parents=True, exist_ok=True)

#     count = 0
#     for img in image_elements:
#         if count >= max_images:
#             break
#         try:
#             m = img.get("m")
#             if not m:
#                 continue
#             m_url = m.split('"murl":"')[1].split('"')[0]
#             ext = m_url.split(".")[-1].split("?")[0]
#             if ext.lower() not in ["jpg", "jpeg", "png", "webp"]:
#                 ext = "jpg"
#             filename = f"{query.replace(' ', '_')}_{uuid.uuid4().hex[:8]}.{ext}"
#             filepath = os.path.join(save_dir, filename)
#             r = requests.get(m_url, timeout=10)
#             with open(filepath, "wb") as f:
#                 f.write(r.content)
#             count += 1
#             print(f"[{count}] Downloaded: {filename}")
#         except Exception as e:
#             print(f"❌ Failed to download image: {e}")

# # 🧪 ทดลองใช้งาน
# download_images_bing(
#     query="drone top view",
#     save_dir=r"D:\Drone\my_dataset\topview",
#     max_images=1000
# )
