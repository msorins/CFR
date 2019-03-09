import fitz

class ReadPDF():
    def read(self, path):

        return fitz.open(path)
