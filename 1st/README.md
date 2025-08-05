# 🛰️ DuckDuckGo Image Downloader (Custom Path)

This Python script allows you to search and download images from **DuckDuckGo** into **any custom directory**, such as `D:\my_dataset`, instead of the default `C:` drive. It is useful for building large-scale datasets (e.g., drone imagery, machine learning, etc.).

---

## 📦 Features

- ✅ Download images using keywords from DuckDuckGo
- ✅ Supports saving to any folder (including external drives)
- ✅ Automatic file renaming with UUID to avoid duplicates
- ✅ Filetype filtering (JPG, PNG, WEBP)
- ✅ Error handling for failed downloads

---

## 🚀 Installation

```bash
pip install duckduckgo_search
```

---

## 🧠 Usage
## 🔹 Single Keyword

```python
from duckduckgo_search import ddg_images
import os
import requests
from pathlib import Path
import uuid

def download_duckduckgo_images(query, download_path, max_images=100):
    Path(download_path).mkdir(parents=True, exist_ok=True)
    results = ddg_images(query, max_results=max_images)
    print(f"Found {len(results)} results for: {query}")

    for result in results:
        image_url = result['image']
        ext = image_url.split('.')[-1].split("?")[0]
        if ext.lower() not in ['jpg', 'jpeg', 'png', 'webp']:
            ext = 'jpg'
        filename = f"{query.replace(' ', '_')}_{uuid.uuid4().hex[:10]}.{ext}"
        filepath = os.path.join(download_path, filename)

        try:
            response = requests.get(image_url, timeout=10)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed: {filename} | Reason: {e}")

# Example:
download_duckduckgo_images(
    query="drone top view",
    download_path=r"D:\my_dataset\drone_top_view",
    max_images=100
)
```

## 🔹 Multiple Keywords (Batch)

```python
queries = ["drone top view", "drone side view", "drone under view"]
base_path = r"D:\my_dataset"

for q in queries:
    subfolder = os.path.join(base_path, q.replace(" ", "_"))
    download_duckduckgo_images(q, subfolder, max_images=500)
```

---

## 📌 Tips
- Run with Python 3.8+
- Avoid too many requests too fast to prevent blocking
- You can integrate multiprocessing to speed up downloads for large datasets

---

## 📜 License
MIT License

---


