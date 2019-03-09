import PyPDF2
from Evaluators.SpellCheckEvaluator import SpellCheckEvaluator


file = open('Data/cool.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(file)
eval = SpellCheckEvaluator()
eval.evaluate(pdf)
