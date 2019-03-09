from Evaluators.OnePage import OnePage
from Utils.ReadPDF import ReadPDF

readUtils = ReadPDF()
cv = readUtils.read('/Users/so/Desktop/Projects/CFR/Data/CV_MirceaSorinSebastian.pdf')
onePageEval = OnePage()
result = onePageEval.evaluate(cv)
print(result)