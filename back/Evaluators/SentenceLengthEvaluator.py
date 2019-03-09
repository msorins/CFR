from Evaluators.BasicEvaluator import BasicEvaluator
import PyPDF2

class SentenceLengthEvaluator(BasicEvaluator):
    def evaluate(self, pyPDF: PyPDF2):
        pass



file = open('../Data/cv_ex1.pdf', 'rb')
fileReader = PyPDF2.PdfFileReader(file)


# print the number of pages in pdf file
print(fileReader.numPages)
# SentenceLengthEvaluator().evaluate('ha')

page = fileReader.getPage(0)
page_content = page.extractText()
print(page_content)