from Evaluators.BasicEvaluator import BasicEvaluator
from Models.PartialFeedback import PartialFeedback
import PyPDF2
# import textract

class SentenceLengthEvaluator(BasicEvaluator):
    SENTENCE_SIZE_LIMIT = 270

    def evaluate(self, py_pdf: PyPDF2):
        print(py_pdf.numPages)

        sentences = []
        for page_num in range(py_pdf.numPages):
            extracted_text = py_pdf.getPage(page_num).extractText()
            if len(extracted_text) > 0:
                for sentence in py_pdf.getPage(page_num).extractText().split('.'):
                    sentences.append(sentence.strip().replace('\n', '').encode('ascii', errors='ignore').decode())
            else:
                raise RuntimeError('Could not extract text from page ' + page_num)

        feedback = []
        wrongs = 0
        rights = 0
        for x in sentences:
            if len(x) > self.SENTENCE_SIZE_LIMIT:
                wrongs += 1
            else:
                rights += 1
        return [PartialFeedback('Nr. of short sentences: ' + str(rights) + '\nNr. of long sentences: ' + str(wrongs),
                               1 if wrongs == 0 else 0, 'Sentences', 'Long sentences are unlikely to be read by recruitors. Statistics say that they only look on a page for about 5 to 10 seconds. That is short')]



# file = open('C:\Work\CFR\Data\CV_MirceaSorinSebastian.pdf', 'rb')
# file = open('..\Data\\' + 'Cosmin.pdf', 'rb')
# pyPDFReader = PyPDF2.PdfFileReader(file)
# print(SentenceLengthEvaluator().evaluate(pyPDFReader)[0])
