from pandas import DataFrame
import string
import fitz
import glob, os

class PDFDataExtractor:

    def __init__(self):
        path = '/home/andreib/Desktop/CFR/back/ML/data/positive'
        os.chdir(path)
        self.filenames = [filename for filename in glob.glob('*.pdf')]


    def get_data(self) -> DataFrame:
        def sanitize_input(txt: str) -> str:
            allowed = list(string.ascii_uppercase)
            allowed += list(string.ascii_lowercase)
            allowed += list(string.digits)
            for c in txt:
                if c not in allowed:
                    text = txt.replace(c, '')
            return text

        df = DataFrame({'text': [], 'polarity': []})
        text_column = []

        for filename in self.filenames:
            pdf = fitz.open(filename)
            text = ''
            for page in range(pdf.pageCount):
                text += pdf[page].getText()
            text = sanitize_input(text)
            text_column.append(text)

        df['text'] = text_column
        df['polarity'] = 1

        return df
