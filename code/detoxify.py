from detoxify import Detoxify
import pandas as pd

def detoxify(file):
    df = pd.read_csv(file)

    en_yet_detox = df.loc[(df['tika_lan_code'] == 'en') | (df['ggl_lan_code'] == 'en')]
    for row in en_yet_detox.index:
        try:
            narrative = str(df.at[row,'Narrative'])
            score = Detoxify('unbiased').predict(narrative)
            df.at[row, 'toxicity'] = score.get('toxicity')
            df.at[row, 'severe_toxicity'] = score.get('severe_toxicity') 
            df.at[row, 'obscene'] = score.get('obscene') 
            df.at[row, 'identity_attack'] = score.get('identity_attack')
            df.at[row, 'insult'] = score.get('insult')
            df.at[row, 'threat'] = score.get('threat')
            df.at[row, 'sexual_explicit'] = score.get('sexual_explicit')
        except Exception as e:
            print(str(e))
            print(row)
            continue

    transed_yet_detox = df.loc[(df['narrative_translation'].notna()) & (df['toxicity'].isna())]
    for row in transed_yet_detox.index:
        try:
            narrative = str(df.at[row,'narrative_translation'])
            score = Detoxify('unbiased').predict(narrative)
            df.at[row, 'toxicity'] = score.get('toxicity')
            df.at[row, 'severe_toxicity'] = score.get('severe_toxicity') 
            df.at[row, 'obscene'] = score.get('obscene') 
            df.at[row, 'identity_attack'] = score.get('identity_attack')
            df.at[row, 'insult'] = score.get('insult')
            df.at[row, 'threat'] = score.get('threat')
            df.at[row, 'sexual_explicit'] = score.get('sexual_explicit')
        except Exception as e:
            print(str(e))
            print(row)
            continue

    df.to_csv('pixstory_detoxify.csv')
    
def run_detoxify():
    pixstory_df_path = "../data/pixstory/geo_df.csv"
    detoxify(pixstory_df_path)
    
if __name__ == '__main__':
    run_detoxify()
