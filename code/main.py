import consolidate_pixstory_data
import media_urls
import media_images
import im2text
import inception
import language_code
import google_translate
import geotopic_parsing
import run_detoxify

if __name__ == '__main__':
    # 1. ensure '../data/pixstory/pixstory_v2.tsv' is present
    
    # 2. consolidate pixstory data
    consolidate_pixstory_data.convert_tsv_to_csv('pixstory_v2.tsv', 'pixstory_v2.csv')
    media_urls.get_urls()
    media_images.download_images()
    
    # 3. add features (may need to run one at a time)
    im2text.get_caption_files()
    im2text.flag_pixstory_captions()
    inception.get_object_files()
    inception.flag_pixstory_objects()
    language_code.run_google_lan_det()
    google_translate.get_clean_narratives()
    google_translate.get_translation_files()
    google_translate.flag_pixstory_translations()
    geotopic_parsing.create_geo_df()
    run_detoxify.run_detoxify()
    
    # 4. combine features (if needed) and convert final csv to tsv
    # consolidate_pixstory_data.combine_features() # not needed if functions here are run in order
    consolidate_pixstory_data.convert_csv_to_tsv('pixstory_detoxify.csv', 'pixstory_final.tsv')
    