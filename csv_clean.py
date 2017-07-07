import pandas as pd
import numpy as np

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to a CSV or HDF file')
    args = parser.parse_args()
    df = pd.read_csv(args.filename, index_col=0)
    print(df.index.get_level_values(0).get_duplicates())


if __name__ == '__main__':
    main()