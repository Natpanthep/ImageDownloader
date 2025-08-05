# 🛸 Drone Image Dataset Collector (from Bing)

This Python script allows you to **automatically download drone images** from Bing Image Search using multiple search keywords. It supports:

- ✅ Custom download directory (e.g., D:\drone_dataset)
- ✅ Multi-keyword input
- ✅ Multiprocessing for high-speed downloads
- ✅ Automatic deduplication using perceptual hashing
- ✅ No API key required

---

## ⚙️ Requirements

```bash
pip install requests beautifulsoup4 pillow imagehash
```

--- 

## 🚀 How to Use
## 1. Modify keywords list
Edit main.py and add your keywords:

```python
keywords = [
    "drone top view",
    "drone side view",
    "agriculture drone spraying",
    "military drone",
    ...
]
```

## 2. Run the downloader

```bash
python main.py
```

This script will:
- Search Bing for each keyword
- Download images (default: 100 per keyword)
- Save to subfolders named after each keyword
- Use multiprocessing to download multiple keywords in parallel

---

## 🧠 Notes
This does not use any Bing API or paid services
You may occasionally hit rate-limits from Bing; adding time.sleep() or rotating IPs helps
Filenames are auto-generated using UUIDs to prevent collision

---

## 📌 License
MIT License. You are free to use and modify this project for dataset generation, computer vision training, or academic purposes.

---


