import requests
import time
import concurrent.futures
from pathlib import Path
import pandas as pd
from ast import literal_eval

rtg_url = 'http://localhost:6060/translate'
# Docker instance of "rtg-model:500toEng-v1" must be running on port 6060

def get_translation(text_input, index, file_output):
    Path("../data/pixstory/narratives_translated").mkdir(parents=True, exist_ok=True)   
        
    parameters = dict(source = text_input)
    response = requests.get(url = rtg_url, 
                            params = parameters)    
    response_json = response.json()
    
    translation = response_json['translation'][0]
    translation_name = f'../data/pixstory/narratives_translated/{file_output}_{index}.txt'
    
    with open(translation_name, 'w') as file_handler:
        file_handler.write(translation)

def get_translation_files():
    narrative_filepath = '../data/pixstory/clean_narratives.csv'
    narrative_df = pd.read_csv(narrative_filepath, delimiter=',', encoding='utf-8')
    narrative_df = narrative_df.rename(columns={'Story Primary ID': 'ID',
                                                'narrative_chunks': 'text_list'})
    narrative_df['text_list'] = narrative_df['text_list'].apply(literal_eval)
    
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for narrative in narrative_df.itertuples():
            filename = narrative.ID
            text_list = narrative.text_list

            for index in range(len(text_list)):
                text_input = text_list[index]
                executor.submit(get_translation(text_input, index, filename))
    
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took almost 2 minutes for 5 posts
    # there are almost 25,000 posts, so est time to complete is 
    # 10,000 minutes = 7 days  

if __name__ == '__main__':
    get_translation_files()
