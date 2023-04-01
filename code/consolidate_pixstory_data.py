import pandas as pd 
from collections import defaultdict

def convert_tsv_to_csv(input_file, output_file):
    input_path = '../data/pixstory/' + input_file
    output_path = '../data/pixstory/' + output_file
    
    table_df = pd.read_table(input_path, sep='\t')
    
    return table_df.to_csv(output_path, index=False)

def get_clean_narratives():
    pixstory_filepath = '../data/pixstory/pixstory_langdetect.csv'
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
    
    pixstory_df = pixstory_df[  (pixstory_df['tika_lan_code'] != 'en')
                              & (pixstory_df['ggl_lan_code'] != 'en') ]
    
    narrative_df = pixstory_df[['Story Primary ID', 'Narrative']]
    narrative_df = narrative_df.rename(columns={'Story Primary ID': 'ID',
                                                'Narrative': 'text'})
    
    # remove non-alphanumeric characters
    narrative_df['text'] = narrative_df['text'] \
                            .astype(str) \
                            .str.replace('[^0-9a-zA-Z.,-/ ]', '') \
                            
    # split narratives into 100-character chunks
    narrative_dict = defaultdict(dict)
    for narrative in narrative_df.itertuples():
        text_length = len(narrative.text)
        chunks_list = [narrative.text[i:i+100] 
                        for i in range(0, text_length, 100)]
        narrative_dict[narrative.ID] = chunks_list
    
    narrative_df = pd.DataFrame(narrative_dict.items(), columns=['Story Primary ID', 'narrative_chunks'])
    narrative_df.to_csv('../data/pixstory/clean_narratives.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    convert_tsv_to_csv('pixstory_v2.tsv', 'pixstory_v2.csv')
    get_clean_narratives()
