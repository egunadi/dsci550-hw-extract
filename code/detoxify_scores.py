from detoxify import Detoxify
import pandas as pd
from collections import defaultdict

def import_pixstory():
    pixstory_df = pd.read_csv('../data/pixstory/pixstory.csv', delimiter=',', encoding='utf-8')
    pixstory_df.columns = pixstory_df.columns.str.replace(' ', '')
    pixstory_df['Narrative'] = pixstory_df['Narrative'].astype(str)

    narrative_dict = defaultdict(dict)
    for pixstory in pixstory_df.itertuples():
        narrative_dict[pixstory.StoryPrimaryID] = pixstory.Narrative
    return narrative_dict

def detoxify_results():
    narrative_dict = import_pixstory()
    results = defaultdict(dict)

    for StoryPrimaryID, words in narrative_dict.items():
        results[StoryPrimaryID] = Detoxify('unbiased').predict(words)

    return dict(results)

x = detoxify_results()
print(x)







# optional to display results nicely (will need to pip install pandas)

''''
import pandas as pd
print(pd.DataFrame(results, index=input_text).round(5))
'''
