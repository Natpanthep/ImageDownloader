from duckduckgo_search import ddg_images
import os
import requests
from pathlib import Path
import uuid

def download_duckduckgo_images(query, download_path, max_images=100):
    # Ensure download path exists
    Path(download_path).mkdir(parents=True, exist_ok=True)

    # Search images
    results = ddg_images(query, max_results=max_images)
    print(f"Found {len(results)} results for: {query}")

    for result in results:
        image_url = result['image']
        ext = image_url.split('.')[-1].split("?")[0]
        if ext.lower() not in ['jpg', 'jpeg', 'png', 'webp']:
            ext = 'jpg'  # fallback
        filename = f"{query.replace(' ', '_')}_{uuid.uuid4().hex[:10]}.{ext}"
        filepath = os.path.join(download_path, filename)

        try:
            response = requests.get(image_url, timeout=10)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed: {filename} | Reason: {e}")

# Example usage
download_duckduckgo_images(
    query="drone top view",
    download_path=r"D:\Drone\my_dataset\drone_topview",
    max_images=1000
)
