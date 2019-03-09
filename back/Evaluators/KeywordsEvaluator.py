from Evaluators.BasicEvaluator import BasicEvaluator
from Models.PartialFeedback import PartialFeedback
from Evaluators.BasicEvaluator import FitzDoc

class KeywordsEvaluator(BasicEvaluator):
    programming_languages = ['javaScript','python','java','c','c++','php','swift','c#','ruby','objective-c',
                             'sql','kotlin','assembly','matlab','octave','go','typescript','f#','groovy',
                             'erlang','ocaml','lua','shell']

    # ?????????????????
    frond_end = ['javaScript','html','css','typescript']
    back_end = ['javaScript','python','java','php','ruby','typescript','c++','node']
    mobile = ['java','kotlin','swift','ios','android']
    # ?????????????????

    paragraphs = ['experience', 'projects', 'education', 'skills', 'awards']

    # Most of the words that fall into this list are CV cliches that have been around
    # so long that they no longer carry any real meaning.
    bad_personal_words = ['Flexible','Motivated','Independent','Self-motivated']

    good_personal_words = ['accurate','adaptable','confident','hard-working','innovative','pro-active',
                           'reliable','responsible','achieved']

    def evaluate(self, py_pdf: FitzDoc):
        extracted_text = ''
        feedback_list = []

        for page_num in range(py_pdf.pageCount):
            extracted_text += py_pdf[page_num].getText()

        extracted_text = str.lower(extracted_text)
        extracted_text = extracted_text.replace(' ', '').replace('\n','')
        # print(extracted_text)

        # programming languages check
        found = self.count_words(extracted_text, KeywordsEvaluator.programming_languages)
        feedback_list.append(self.get_feedback('You should mention at least 5 programming languages', found >= 5))

        # bad self describing words
        found = self.count_words(extracted_text, KeywordsEvaluator.bad_personal_words)
        feedback_list.append(self.get_feedback('You should not use clichés to describe yourself', found == 0))

        # good self describing words
        found = self.count_words(extracted_text, KeywordsEvaluator.good_personal_words)
        feedback_list.append(self.get_feedback('You may use at least 2 interesting self describing words', found >= 2))

        # check for paragraphs
        # print('what?')
        found = self.count_words(extracted_text, KeywordsEvaluator.paragraphs)
        feedback_list.append(self.get_feedback('You need to include all the mandatory paragraphs', found == len(KeywordsEvaluator.paragraphs)))

        return feedback_list

    def count_words(self, text, words_list):
        total = 0
        for word in words_list:
            if word in text:
                print(word, end=';')
                total += 1
        # print('--')
        return total

    def get_feedback(self, message, correctness):
        if correctness:
            return PartialFeedback(message, 1, 'Keywords', 'KeywordEvaluator extra info (TO do)')
        return PartialFeedback(message, 0, 'Keywords', 'KeywordEvaluator extra info (TO do)')


# file = open('C:\W ork\CFR\Data\CV_MirceaSorinSebastian.pdf', 'rb')
# file = open('..\Data\\' + 'Cosmin.pdf', 'rb')
# pyPDFReader = PyPDF2.PdfFileReader(file)
# for item in KeywordsEvaluator().evaluate(pyPDFReader):
#     print(item)
