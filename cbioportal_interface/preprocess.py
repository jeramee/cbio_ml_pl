import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class PreprocessML:
    def __init__(self, df):
        self.df = df

    def normalize_data(self, columns):
        scaler = MinMaxScaler()
        self.df[columns] = scaler.fit_transform(self.df[columns])
        return self.df

    def standardize_data(self, columns):
        scaler = StandardScaler()
        self.df[columns] = scaler.fit_transform(self.df[columns])
        return self.df

    # Additional preprocessing methods can go here
