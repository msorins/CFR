import string
import PyPDF2
from Evaluators.BasicEvaluator import BasicEvaluator
from API.spellcheck import spellcheck
from Models.PartialFeedback import PartialFeedback
from typing import List

class SpellCheckEvaluator(BasicEvaluator):

    def _sanitise_text(self, text: str) -> str:
        text = text.replace('¥', '\n')
        text = text.replace('Õ', "'")
        allowed_chars = list(string.ascii_lowercase)
        allowed_chars += list(string.ascii_uppercase)
        allowed_chars += list(string.digits)
        allowed_chars += [' ', '\n', '-', '_', '@', '!', '?', "'", '@', '.', ',', ':']
        for c in text:
            if c not in allowed_chars:
                text = text.replace(c, '')
        text = text.replace('\n ', '\n')
        text = text.replace(',\n', ',')
        text = text.replace('\n,', ',')
        print(text)
        return text

    def evaluate(self, pdf: PyPDF2) -> List[PartialFeedback]:
        for idx in range(pdf.numPages):
            page = pdf.getPage(idx)
            text = page.extractText()
            text = self._sanitise_text(text)

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
                        "Spell checker"
                    ))

            if len(feedback) == 0:
                feedback.append(PartialFeedback(
                    f"No misspelling!",
                    1,
                    "Spell checker"
                ))

            return feedback
