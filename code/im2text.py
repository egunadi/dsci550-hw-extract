import requests
import time
import concurrent.futures
import glob
from pathlib import Path

im2text_url = 'http://localhost:8764/inception/v3/caption/image'
# Docker instance of "im2txt-rest-tika " must be running on port 8764

directory_path = '../data/pixstory/media-files'
media_files = glob.glob(f"{directory_path}/*")

def get_caption(filename):
    Path("../data/pixstory/media-captions").mkdir(parents=True, exist_ok=True)
    
    media_url= 'http://192.168.1.8:8000/' + filename
    # Images in "data/pixstory/media-files" must be served on port 8000 
    # ex. using `python -m http.server` 
    
    parameters = dict(url = media_url)
    response = requests.get(url = im2text_url, 
                            params = parameters)    
    response_json = response.json()
    
    caption = response_json['captions'][0]['sentence']
    caption_name = f'../data/pixstory/media-captions/{filename}.txt'
    
    with open(caption_name, 'w') as file_handler:
        file_handler.write(caption)

def get_captions():
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for media_file in media_files:
            filename = Path(media_file).name
            executor.submit(get_caption, filename)
            
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took a little over 31 hours to finish on local machine
    
if __name__ == '__main__':
    get_captions()
