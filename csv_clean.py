import pandas as pd
import numpy as np

def main():

    # Read in input file
    df = pd.read_csv('input_data.csv', index_col=0)

    # Remove duplicate indexes, keep the first instance
    nodupes = df[~df.index.duplicated(keep='first')]

    # Remove NaNs from dataset
    nonulls = nodupes.dropna(subset=['q2', 'q4'])

    # Read in q3 values
    df_q3 = pd.read_csv('q3_column.csv', index_col=0)

    # Merge q3 values with rest of dataframe
    finaldf = nonulls.join(df_q3, how='left')

    finaldf.to_csv('cleaned.csv')

if __name__ == '__main__':
    main()