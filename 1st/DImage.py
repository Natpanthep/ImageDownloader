from icrawler.builtin import BingImageCrawler
import os

def download_images(keyword, save_dir, max_num=1000):
    crawler = BingImageCrawler(storage={'root_dir': save_dir})
    crawler.crawl(keyword=keyword, max_num=max_num)

if __name__ == "__main__":
    with open("search_terms.txt", "r") as f:
        terms = f.read().splitlines()

    for term in terms:
        folder = term.replace(" ", "_")
        os.makedirs(f"./dataset/{folder}", exist_ok=True)
        download_images(term, f"./dataset/{folder}", max_num=1000)
