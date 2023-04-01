import pandas as pd 

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
    
    # remove non-alphanumeric characters
    narrative_df['Narrative'] = narrative_df['Narrative'].str.replace('[^0-9a-zA-Z.,-/ ]', '')
    
    narrative_df.to_csv('../data/pixstory/clean_narratives.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    # convert_tsv_to_csv('pixstory_v2.tsv', 'pixstory_v2.csv')
    get_clean_narratives()
