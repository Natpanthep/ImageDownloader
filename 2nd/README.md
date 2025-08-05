# Drone Image Downloader (Bing + Python)

A Python script to automatically download large batches of drone-related images (e.g., top view, side view, under view) from **Bing Image Search**, and save them to a custom folder (e.g., `D:\drone_dataset`), outside the C drive.

This project uses [`icrawler`](https://github.com/hellock/icrawler) and includes custom filename generation to avoid duplicates.

---

## 🚀 Features

- 🔍 Search via Bing (no API key required)
- 📁 Save to any custom path (e.g., D:\)
- 📸 Auto filename with `view_type`, keyword, and UUID
- ✅ Create subfolders per search keyword
- 🧱 Compatible with future dataset pipelines

---

## 🧰 Requirements

- Python 3.6+
- pip

Install dependencies:

```bash
pip install icrawler
```

---

## 🧑‍💻 Usage
Edit and run the following Python script

---

## ✅ Tips
- Run with different keywords to increase dataset size
- To parallelize downloads, use multiprocessing or run in separate processes
- You can change the naming pattern or use timestamps if needed

---

## 📄 License
MIT License

----

## 🙏 Credits
icrawler - Easy and extensible image crawler

---


