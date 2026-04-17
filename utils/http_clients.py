import threading
import requests
import time


def download_image(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    if resp.status_code == 200:
        print(f"Finished downloading from {url} size {len(resp.content) / 1024 / 1024:.2f} MB")
    else:
        print(f"Failed to download from {url} with status code {resp.status_code}")


if __name__ == "__main__":
    urls = [
        "https://httpbin.org/image/jpeg",
        "https://httpbin.org/image/png",
        "https://httpbin.org/image/svg",
    ]

    start = time.time()
    threads = []

    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


    end = time.time()
    print(f"Downloaded {len(urls)} images in {end - start:.2f} seconds")