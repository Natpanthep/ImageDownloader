from multiprocessing import Pool
from icrawler.builtin import BingImageCrawler
import os

def crawl(term):
    folder = term.replace(" ", "_")
    os.makedirs(f"./dataset/{folder}", exist_ok=True)
    crawler = BingImageCrawler(storage={'root_dir': f"./dataset/{folder}"})
    crawler.crawl(keyword=term, max_num=1000)

if __name__ == "__main__":
    with open("search_terms.txt", "r") as f:
        terms = f.read().splitlines()

    with Pool(processes=10) as pool:  # ปรับจำนวนตาม CPU
        pool.map(crawl, terms)
