import PyPDF2

class ReadPDF():
    def read(self, path):
        file = open(path, 'rb')

        cv = PyPDF2.PdfFileReader(file)
        return cv