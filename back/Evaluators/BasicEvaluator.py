from typing import NewType

FitzDoc = NewType('FitzDoc', str)

class BasicEvaluator:
    def evaluate(self, pdf: FitzDoc):
        """
        :param pdf:
        :return: a list of PartialFeedback
        """
        pass
