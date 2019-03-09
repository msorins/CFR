import string
import PyPDF2
from Evaluators.BasicEvaluator import BasicEvaluator
from API.spellcheck import spellcheck
from Models.PartialFeedback import PartialFeedback

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
            feedback = []
            for idx, line in enumerate(text.split('\n')):
                had_to_correct, corrected = spellcheck(line)
                if had_to_correct:
                    feedback.append(PartialFeedback(
                        f"Misspeling at line{idx}, try: {corrected}",
                        0
                    ))
                else:
                    feedback.append(PartialFeedback(
                        f"No misspelling on line {idx}",
                        1
                    ))
            return feedback
