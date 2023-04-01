import requests
import time
import concurrent.futures
import glob
from pathlib import Path
import pandas as pd

inception_url = 'http://localhost:8764/inception/v4/classify/image'
# Docker instance of "inception-rest-tika" must be running on port 8764

media_path = '../data/pixstory/media_files'
media_files = glob.glob(f"{media_path}/*")

def get_object(filename):
    Path("../data/pixstory/media_objects").mkdir(parents=True, exist_ok=True)
    
    media_url= 'http://192.168.1.8:8000/' + filename
    # Images in "data/pixstory/media_files" must be served on port 8000 
    # ex. using `python -m http.server` 
    
    parameters = dict(topn = 2,
                      min_confidence = 0.03,
                      url = media_url)
    response = requests.get(url = inception_url, 
                            params = parameters)    
    response_json = response.json()
    
    object_list = response_json['classnames']
    object_string = ', '.join(object_list)
    object_name = f'../data/pixstory/media_objects/{filename}.txt'
    
    with open(object_name, 'w') as file_handler:
        file_handler.write(object_string)

def get_object_files():
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for media_file in media_files:
            filename = Path(media_file).name
            executor.submit(get_object, filename)
            
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took almost 8.5 hours to finish on local machine
    
def get_object_df():
    object_path = '../data/pixstory/media_objects'
    object_files = glob.glob(f"{object_path}/*")
    
    object_list = []
    for object_file in object_files:
        with open(object_file, 'r') as file_handler:
            media_name = 'https://image.pixstory.com/' + Path(object_file).stem
            objects = file_handler.read()
            object_list.append((media_name, objects))
    
    object_df = pd.DataFrame(object_list, columns=['Media', 'media_objects'])
    
    return object_df
    
def flag_pixstory_objects():
    pixstory_filepath = '../data/pixstory/pixstory_captions.csv'
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
    object_df = get_object_df()
    
    pixstory_df = pixstory_df.merge(object_df, on='Media', how='left')
    
    pixstory_df.to_csv('../data/pixstory/pixstory_objects.csv', encoding='utf-8', index=False)
    # took about 3 minutes to finish on local machine

if __name__ == '__main__':
    get_object_files()
    flag_pixstory_objects()
