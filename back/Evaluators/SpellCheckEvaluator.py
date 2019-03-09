import string
import PyPDF2
from Evaluators.BasicEvaluator import BasicEvaluator
from API.spellcheck import spellcheck
from Models.PartialFeedback import PartialFeedback
from typing import List
from Evaluators.BasicEvaluator import FitzDoc


class SpellCheckEvaluator(BasicEvaluator):

    def evaluate(self, pdf: FitzDoc) -> List[PartialFeedback]:
        for idx in range(pdf.pageCount):
            page = pdf[idx]
            text = page.getText()

            corrected_text = spellcheck(text)

            feedback = []
            old_l = text.split('\n')
            new_l = corrected_text.split('\n')

            for idx, lines in enumerate(list(zip(old_l, new_l))):
                old_l, new_l = lines
                if old_l != new_l:
                    feedback.append(PartialFeedback(
                        f"Misspeling at line {idx}, try: {new_line}",
                        0,
                        "Spell checker",
                        "Making a typo may look you bad, first impression matters!"
                    ))

            if len(feedback) == 0:
                feedback.append(PartialFeedback(
                    f"No misspelling!",
                    1,
                    "Spell checker",
                    "Making a typo may look you bad, first impression matters!"
                ))

            return feedback
