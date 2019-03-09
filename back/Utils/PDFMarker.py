import fitz
from MarkUpPDF import MarkUpPDF

cliche_words = ['(Mountain', 'Flexible','Motivated','Independent','Self-motivated']
file_path = 'back/Data/Cosmin.pdf'

py_pdf = fitz.open(file_path)
extracted_text = ''

for page_num in range(py_pdf.pageCount):
    extracted_text += py_pdf[page_num].getText()

extracted_text = str.lower(extracted_text)
extracted_text = extracted_text.replace(' ', '').replace('\n','')

to_cut = []
for word in cliche_words:
    if word in extracted_text:
        to_cut.append(word)

MarkUpPDF('output.pdf', c_words=to_cut)
