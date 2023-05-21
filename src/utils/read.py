import pandas as pd

def read_file_as_df(file_path):
    ## check if the file exists
    try:
        open(file_path)
        df = pd.read_csv(file_path, header=None, names=['BrandName', 'ItemName', 'Link'])
        return df
    except FileNotFoundError:
        return None