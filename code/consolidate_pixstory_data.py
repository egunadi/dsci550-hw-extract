import pandas as pd 
import csv

def convert_tsv_to_csv(input_file, output_file):
    input_path = '../data/pixstory/' + input_file
    output_path = '../data/pixstory/' + output_file
    
    table_df = pd.read_table(input_path, sep='\t')
    
    return table_df.to_csv(output_path, index=False)

def combine_features():
    pixstory_filepath = '../data/pixstory/pixstory_v2.csv'
    # original dataset
    
    translations_filepath = '../data/pixstory/pixstory_translations.csv'
    # contains features tika_lan_code and ggl_lan_code

    detoxify_filepath = '../data/pixstory/pixstory_detoxify.csv'
    # contains features media_captions, media_objects, narrative_translation, 
    # toxicity, severe_toxicity, obscene, identity_attack, insult, threat, and sexual_explicit
    
    geo_filepath = '../data/pixstory/geo_df.csv'
    # contains feature Location
    
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    translations_df = pd.read_csv(translations_filepath, delimiter=',', encoding='utf-8')
    detoxify_df = pd.read_csv(detoxify_filepath, delimiter=',', encoding='utf-8')
    geo_df = pd.read_csv(geo_filepath, delimiter=',', encoding='utf-8')
    
    geo_df = geo_df.rename(columns={'storyPrimaryID': 'Story Primary ID'})
    
    pixstory_df = pixstory_df.drop_duplicates(subset=['Story Primary ID'])
    translations_df = translations_df.drop_duplicates(subset=['Story Primary ID'])
    detoxify_df = detoxify_df.drop_duplicates(subset=['Story Primary ID'])
    geo_df = geo_df.drop_duplicates(subset=['Story Primary ID'])
    
    translations_df = translations_df[['Story Primary ID', 'tika_lan_code', 'ggl_lan_code']]
    detoxify_df = detoxify_df[['Story Primary ID', 'media_captions', 'media_objects', 
                               'narrative_translation', 'toxicity', 'severe_toxicity', 'obscene', 
                               'identity_attack', 'insult', 'threat', 'sexual_explicit']]
    geo_df = geo_df[['Story Primary ID', 'Location']]
    
    pixstory_df = pixstory_df.merge(translations_df,  on='Story Primary ID', how='left')
    pixstory_df = pixstory_df.merge(detoxify_df,  on='Story Primary ID', how='left')
    pixstory_df = pixstory_df.merge(geo_df,  on='Story Primary ID', how='left')
    
    pixstory_df.to_csv('../data/pixstory/pixstory_final.csv', encoding='utf-8', index=False)
    
def convert_csv_to_tsv(input_file, output_file):
    input_path = '../data/pixstory/' + input_file
    output_path = '../data/pixstory/' + output_file
    
    with    open(input_path, 'r', encoding='utf-8') as csvin, \
            open(output_path, 'w', encoding='utf-8') as tsvout:
                csvin = csv.reader(csvin)
                tsvout = csv.writer(tsvout, dialect='excel-tab')
 
                for row in csvin:
                    tsvout.writerow(row)

if __name__ == '__main__':
    convert_tsv_to_csv('pixstory_v2.tsv', 'pixstory_v2.csv')
    combine_features()
    convert_csv_to_tsv('pixstory_final.csv', 'pixstory_final.tsv')
