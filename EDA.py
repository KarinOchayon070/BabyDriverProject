import pandas as pd
import numpy as np
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(ROOT_PATH, "csvData.csv")


def load_csv():
    df = pd.read_csv(CSV_PATH)
    print(df.head())
    return df


load_csv()
