import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../data/trackFeatures.csv')
    print(df.head())