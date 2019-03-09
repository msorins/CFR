from Evaluators.BasicEvaluator import BasicEvaluator
from Models.PartialFeedback import PartialFeedback
from Evaluators.BasicEvaluator import FitzDoc


class OnePage(BasicEvaluator):
    def evaluate(self, pdf: FitzDoc):
        numPages = pdf.pageCount

        if(numPages == 1):
            return [ PartialFeedback("One page is enough for a CV", 1, 'Number of pages', "If you do not have at least 15 years of experience, you shouldn't need more than one page") ]
        else:
            return [ PartialFeedback("One page is enough for a CV", 0, 'Number of pages', "If you do not have at least 15 years of experience, you shouldn't need more than one page") ]
