import requests
import time
import pandas as pd
import concurrent.futures
import glob
from pathlib import Path

im2text_url = 'http://localhost:8764/inception/v3/caption/image'
# Docker instance of "im2txt-rest-tika " must be running on port 8764

directory_path = '../data/pixstory/media-files-test'
media_files = glob.glob(f"{directory_path}/*")

def get_caption(filename):
    media_url= 'http://192.168.1.8:8000/' + filename
    # Images in "data/pixstory/media-files" must be served on port 8000 
    # ex. using `python -m http.server` 
    
    parameters = dict(url = media_url)
    response = requests.get(url = im2text_url, 
                            params = parameters)    
    response_json = response.json()
    
    print(response_json['captions'][0]['sentence'])

def get_captions():
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for media_file in media_files:
            filename = Path(media_file).name
            executor.submit(get_caption, filename)
            
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took approximately 15 minutes to finish on local machine
