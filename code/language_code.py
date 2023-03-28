import pandas as pd
from tika import language
from langdetect import detect

def get_pixstory_df(pixstory_df_path):
    pixstory_df = pd.read_csv(pixstory_df_path)
    return pixstory_df 

# create column for language code generated by tika language detector

def tika_lan_det(pixstory_df):
    print("Start tika")
    lang_code_lst = list()
    for narrative in pixstory_df["Narrative"]:
        try:
            lang_code_lst.append(language.from_buffer(narrative))
        except:
            lang_code_lst.append('zz')  #for posts with emoji that runs into error, set language code as "zz"
        lang_code_lst.append(language.from_buffer(narrative))

    lang_code_df = pd.DataFrame(lang_code_lst)
    lang_code_df.columns = ["tika_lan_code"]
    df_concat_tika = pd.concat([pixstory_df, lang_code_df.reset_index(drop=True)], axis = 1)
    return df_concat_tika


# create column for language code generated by Google LangDetect

def google_lan_det(pixstory_tika_df):
    print("Start Goog")
    lang_code_lst = list()
    for narrative in pixstory_tika_df["Narrative"]:
        try:
            lang_code_lst.append(detect(narrative))
        except:
            lang_code_lst.append('zz')  #for posts with emoji that runs into error, set language code as "zz"
        # lang_code_lst.append(detect(narrative))

    lang_code_df = pd.DataFrame(lang_code_lst)
    lang_code_df.columns = ["ggl_lan_code"]
    df_concat_ggl = pd.concat([pixstory_tika_df, lang_code_df.reset_index(drop=True)], axis = 1)

    df_concat_ggl.to_csv('../data/pixstory/pixstory_langdetect.csv', encoding='utf-8', index=False)
    return df_concat_ggl

if __name__ == '__main__':
    pixstory_df_path = "../data/pixstory/pixstory_objects.csv"
    pixstory_df = get_pixstory_df(pixstory_df_path)
    pixstory_df = tika_lan_det(pixstory_df)
    google_lan_det(pixstory_df)