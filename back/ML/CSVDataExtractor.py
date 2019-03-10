from pandas import DataFrame, read_csv


class CSVDataExtractor:

    def __init__(self):
        self.path = '/home/andreib/Desktop/CFR/back/ML/data/negative/train.csv'


    def get_data(self) -> DataFrame:
        df = read_csv(self.path)
        df['polarity'] = 0
        return df
