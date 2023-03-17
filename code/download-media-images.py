import requests
import time
import pandas as pd

# urls = '../data/pixstory/media-urls-test.csv'
"""
sample URL:
https://image.pixstory.com/optimized/Pixstory-image-165895631710621.png
"""

url_df = pd.read_csv('../data/pixstory/media-urls-test.csv', names=['url'])

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    img_name = f'../data/pixstory/media-files/{img_name}'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)

t1 = time.perf_counter()
for line in url_df.itertuples():
    download_image(line.url)
t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
