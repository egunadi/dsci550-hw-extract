import pandas as pd
import requests 
import json 
from tika import tika
from tika import parser

#take in text string and use .from_buffer to parse text with geotopic mime
#extract location information- name, latitude, and longitde
def location_info(text):
    location = {}
    print('text', text)
    if not pd.isna(text):
        headers = {'Content-Type': 'application/geotopic'}
        parsed = parser.from_buffer(text, headers=headers)
        metadata = parsed['metadata']
        # if hasattr(metadata, 'Geographic_NAME') and hasattr(metadata, 'Geographic_LATITUDE') and hasattr(metadata, 'Geographic_LONGITUDE')
        location['name'] = metadata.get('Geographic_NAME')
        location['latitude'] = metadata.get('Geographic_LATITUDE')
        location['longitude'] = metadata.get('Geographic_LONGITUDE')
        # print('location$$$', location)
    return location

def create_geo_df():
    pixstory = '../data/pixstory/pixstory_translations.csv'
    pixstory_df = pd.read_csv(pixstory, header=1)
    # print(pixstory_df)
    # print(pixstory_df.columns)
    
    #apply function to each row of 'Narrative' column in pixstory_df
    #location info stored in the new 'Location' column in pixstory_df
    pixstory_df['Location'] = pixstory_df['Narrative'].apply(location_info)
    
    print('made it past @@@@@@@@@@@@@@@@@@@@@@@@@@')
    
    pixstory_df.to_csv('../data/pixstory/geo_df.csv', index=False)
    
if __name__ == '__main__':
    create_geo_df()
