# Drone Image Collector (Multi-Source, No API Required)

เก็บภาพโดรน (Drone Images) สำหรับ Dataset ได้มากถึง 10,000,000 ภาพภายใน 1 วัน โดยใช้การดาวน์โหลดแบบอัตโนมัติจากเว็บภาพยอดนิยม 

---

## ✅ ใช้งานได้ 3 วิธี (เลือกวิธีใดวิธีหนึ่ง)

| วิธีที่ | แหล่งภาพ | จุดเด่น | ใช้ไลบรารี |
|--------|-----------|--------|------------|
| 1️⃣     | DuckDuckGo | ไม่ใช้ API / ไม่ติดลิขสิทธ์ / ควบคุมได้สูง | ✅ `duckduckgo`, `requests` |
| 2️⃣     | Bing Images (`requests + iCrawler`) | ไม่ใช้ API / โหลดเร็ว / ควบคุมได้สูง | ✅ `icrawler`, `requests` |
| 3️⃣     | Bing Images (`requests + BeautifulSoup`) | ไม่ใช้ API / โหลดเร็ว / ควบคุมได้สูง | ✅ `beautifulsoup4`, `requests` |

---

## 🔧 โครงสร้างการเก็บภาพ

ภาพที่โหลดมาจะถูกจัดเก็บเป็นโฟลเดอร์ดังนี้:

---

## 🛠 To Do (Optional)
 - เพิ่มการตรวจภาพซ้ำ (dedup)

 - จัดเก็บ metadata เป็น .csv/.json

 - เพิ่มระบบควบคุมการโหลดขนาน (parallel crawling)

---

