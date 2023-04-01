import time
import concurrent.futures
import glob
from pathlib import Path
import pandas as pd
from deep_translator import GoogleTranslator

def get_clean_narratives():
    pixstory_filepath = '../data/pixstory/pixstory_langdetect.csv'
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
    # do not translate english narratives and those with junk characters
    pixstory_df = pixstory_df[  (pixstory_df['tika_lan_code'] != 'en')
                              & (pixstory_df['ggl_lan_code'] != 'en') 
                              & (pixstory_df['ggl_lan_code'] != 'zz')]
    
    narrative_df = pixstory_df[['Story Primary ID', 'Narrative', 'ggl_lan_code']]
    narrative_df = narrative_df.rename(columns={'Story Primary ID': 'ID',
                                                'Narrative': 'text',
                                                'ggl_lan_code': 'language'})
    
    # remove non-alphanumeric characters
    narrative_df['text'] = narrative_df['text'] \
                            .astype(str) \
                            .str.replace('[^0-9a-zA-Z.,-/ ]', '') \
                                
    # do not translate post if translation already exists
    translation_df = get_translation_df()
    translated_list = translation_df['ID']  
    narrative_df = narrative_df[~narrative_df['ID'].isin(translated_list)]
                              
    narrative_df.to_csv('../data/pixstory/clean_narratives.csv', encoding='utf-8', index=False)

def get_translation(text, language, file_output):
    Path("../data/pixstory/narratives_translated").mkdir(parents=True, exist_ok=True)   

    translation = GoogleTranslator(source=language, target='en').translate(text)
    translation_name = f'../data/pixstory/narratives_translated/{file_output}.txt'
    
    if isinstance(translation, str):
        with open(translation_name, 'w') as file_handler:
            file_handler.write(translation)

def get_translation_files():
    narrative_filepath = '../data/pixstory/clean_narratives.csv'
    narrative_df = pd.read_csv(narrative_filepath, delimiter=',', encoding='utf-8')
    
    start_time = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for narrative in narrative_df.itertuples():
            executor.submit(get_translation(narrative.text, narrative.language, narrative.ID))
    
    end_time = time.perf_counter()

    print(f'Finished in {end_time - start_time} seconds')
    # took about 10 seconds for 8 posts
    
def get_translation_df():
    translation_path = '../data/pixstory/narratives_translated'
    translation_files = glob.glob(f"{translation_path}/*")
    
    translation_list = []
    for translation_file in translation_files:
        with open(translation_file, 'r') as file_handler:
            narrative_id = Path(translation_file).stem
            translation = file_handler.read()
            translation_list.append((narrative_id, translation))
    
    translation_df = pd.DataFrame(translation_list, columns=['ID', 'translation'])
    
    return translation_df
    
# def flag_pixstory_translations():
#     pixstory_filepath = '../data/pixstory/pixstory_captions.csv'
#     pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
#     translation_df = get_translation_df()
    
#     pixstory_df = pixstory_df.merge(translation_df, on='Media', how='left')
    
#     pixstory_df.to_csv('../data/pixstory/pixstory_translations.csv', encoding='utf-8', index=False)
    # took about 3 minutes to finish on local machine

if __name__ == '__main__':
    get_clean_narratives()
    # get_translation_files()
    # flag_pixstory_translations()
