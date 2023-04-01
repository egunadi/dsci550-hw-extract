import requests
import time
import concurrent.futures
import glob
from pathlib import Path
import pandas as pd

rtg_url = 'http://localhost:6060/translate'
# Docker instance of "rtg-model:500toEng-v1" must be running on port 6060

narrative_path = '../data/pixstory/narratives_original'
narrative_files = glob.glob(f"{narrative_path}/*")

def get_translation(text_input, file_output):
    Path("../data/pixstory/narratives_translated").mkdir(parents=True, exist_ok=True)
    
    parameters = dict(source = text_input)
    response = requests.get(url = rtg_url, 
                            params = parameters)    
    response_json = response.json()
    
    translation = response_json['translation'][0]
    translation_name = f'../data/pixstory/narratives_translated/{file_output}.txt'
    
    with open(translation_name, 'w') as file_handler:
        file_handler.write(translation)

def get_translation_files():
    pixstory_filepath = '../data/pixstory/pixstory_captions.csv'
    
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for narrative_file in narrative_files:
            filename = Path(narrative_file).name
            executor.submit(get_translation, filename)
            
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took almost 8.5 hours to finish on local machine
    
# def get_translation_df():
#     translation_path = '../data/pixstory/narratives_translated'
#     translation_files = glob.glob(f"{translation_path}/*")
    
#     translation_list = []
#     for translation_file in translation_files:
#         with open(translation_file, 'r') as file_handler:
#             narrative_name = 'https://image.pixstory.com/' + Path(translation_file).stem
#             objects = file_handler.read()
#             translation_list.append((narrative_name, objects))
    
#     translation_df = pd.DataFrame(translation_list, columns=['Media', 'narrative_translations'])
    
#     return translation_df
    
# def flag_pixstory_translations():
#     pixstory_filepath = '../data/pixstory/pixstory_captions.csv'
#     pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
#     translation_df = get_translation_df()
    
#     pixstory_df = pixstory_df.merge(translation_df, on='Media', how='left')
    
#     pixstory_df.to_csv('../data/pixstory/pixstory_translations.csv', encoding='utf-8', index=False)
    # took about 3 minutes to finish on local machine

if __name__ == '__main__':
    # get_translation_files()
    # flag_pixstory_translations()
