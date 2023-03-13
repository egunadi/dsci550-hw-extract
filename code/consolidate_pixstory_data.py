import pandas as pd 

def convert_tsv_to_csv(input_file, output_file):
    input_path = '../data/pixstory/' + input_file
    output_path = '../data/pixstory/' + output_file
    
    table_df = pd.read_table(input_path, sep='\t')
    
    return table_df.to_csv(output_path, index=False)

if __name__ == '__main__':
    convert_tsv_to_csv('pixstory_v2.tsv', 'pixstory_v2.csv')
