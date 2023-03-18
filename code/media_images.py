import requests
import time
import pandas as pd
import concurrent.futures

url_df = pd.read_csv('../data/pixstory/media-urls.csv', names=['url'])
"""
sample URL:
https://image.pixstory.com/optimized/Pixstory-image-165895631710621.png
"""

def download_images(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    img_name = f'../data/pixstory/media-files/{img_name}'
    
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)

if __name__ == '__main__':
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for line in url_df.itertuples():
            executor.submit(download_images, line.url)
            
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took approximately 15 minutes to finish on local machine
