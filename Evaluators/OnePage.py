import PyPDF2

from Evaluators.BasicEvaluator import BasicEvaluator
from Models.PartialFeedback import PartialFeedback


class OnePage(BasicEvaluator):
    def evaluate(self, pyPDF: PyPDF2):
        numPages = pyPDF.getNumPages()

        if(numPages == 1):
            return [ PartialFeedback("One page is enough for a CV", 1) ]
        else:
            return [ PartialFeedback("One page is enough for a CV", 0) ]