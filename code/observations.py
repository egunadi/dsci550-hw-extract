import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

df = pd.read_csv('../data/pixstory/geo_df.csv')
ld = pd.read_csv('../data/pixstory/pixstory_langdetect.csv')
dt = pd.read_csv('../data/pixstory/pixstory_detoxify.csv')


gender=df.value_counts(subset=['Gender','Location']).reset_index(name='count')
print(gender)
age=df.value_counts(subset=['Age','Location']).reset_index(name='count')
print(age[35:])
loc=df.value_counts('Location').reset_index(name='count')
print(loc)
lang= ld.value_counts('ggl_lan_code').reset_index(name='count')
print(lang)
sport=df.value_counts(subset=['sport_event','Location']).reset_index(name='count')
print(sport[44:])
fest=df.value_counts(subset=['Festivals','Location']).reset_index(name='count')
print(fest[48:])

dt["GLAAD"] = df["GLAAD"].astype(int)
glaad_corr = dt["GLAAD"].corr(dt["toxicity"])
print(glaad_corr)

dt["ADL"] = df["ADL"].astype(int)
adl_corr = dt["ADL"].corr(dt["toxicity"])
print(adl_corr)

dt["sarc"] = df["sarc"].astype(int)
sarc_corr = dt["sarc"].corr(dt["toxicity"])
print(sarc_corr)

cap_gen = dt.value_counts(subset=['Gender','media_captions']).reset_index(name='count')
print(cap_gen)

cap_age = dt.value_counts(subset=['Age','media_captions']).reset_index(name='count')
print(cap_age)