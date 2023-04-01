import requests
import time
import concurrent.futures
import glob
from pathlib import Path
import pandas as pd

im2text_url = 'http://localhost:8764/inception/v3/caption/image'
# Docker instance of "im2txt-rest-tika" must be running on port 8764

media_path = '../data/pixstory/media_files'
media_files = glob.glob(f"{media_path}/*")

def get_caption(filename):
    Path("../data/pixstory/media_captions").mkdir(parents=True, exist_ok=True)
    
    media_url= 'http://192.168.1.8:8000/' + filename
    # Images in "data/pixstory/media_files" must be served on port 8000 
    # ex. using `python -m http.server` 
    
    parameters = dict(url = media_url)
    response = requests.get(url = im2text_url, 
                            params = parameters)    
    response_json = response.json()
    
    caption = response_json['captions'][0]['sentence']
    caption_name = f'../data/pixstory/media_captions/{filename}.txt'
    
    with open(caption_name, 'w') as file_handler:
        file_handler.write(caption)

def get_caption_files():
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for media_file in media_files:
            filename = Path(media_file).name
            executor.submit(get_caption, filename)
            
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took a little over 31 hours to finish on local machine
    
def get_caption_df():
    caption_path = '../data/pixstory/media_captions'
    caption_files = glob.glob(f"{caption_path}/*")
    
    caption_list = []
    for caption_file in caption_files:
        with open(caption_file, 'r') as file_handler:
            media_name = 'https://image.pixstory.com/' + Path(caption_file).stem
            captions = file_handler.read()
            caption_list.append((media_name, captions))
    
    caption_df = pd.DataFrame(caption_list, columns=['Media', 'media_captions'])
    
    return caption_df
    
def flag_pixstory_captions():
    pixstory_filepath = '../data/pixstory/pixstory_v2.csv'
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
    caption_df = get_caption_df()
    
    pixstory_df = pixstory_df.merge(caption_df, on='Media', how='left')
    
    pixstory_df.to_csv('../data/pixstory/pixstory_captions.csv', encoding='utf-8', index=False)
    # took about a minute to finish on local machine

if __name__ == '__main__':
    get_caption_files()
    flag_pixstory_captions()
