import pandas as pd

pixstory_filepath = '../data/pixstory/pixstory_v2.csv'

def get_urls():  
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    pixstory_df['Media'] = pixstory_df['Media'].str.replace('.com/', '.com/optimized/')
    
    media_df = pixstory_df['Media']
        
    media_df.to_csv('../data/pixstory/media-urls.csv', encoding='utf-8', index=False)
    
if __name__ == '__main__':
    get_urls()
        