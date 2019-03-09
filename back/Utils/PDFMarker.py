from back.Utils.MarkUpPDF import MarkUpPDF

cliche_words = ['Flexible','Motivated','Independent','Self-motivated']
file_path = 'TO DO'

py_pdf = 'TO DO'
extracted_text = ''

for page_num in range(py_pdf.pageCount):
    extracted_text += py_pdf[page_num].getText()

extracted_text = str.lower(extracted_text)
extracted_text = extracted_text.replace(' ', '').replace('\n','')

to_cut = []
for word in cliche_words:
    if word in extracted_text:
        to_cut.append(word)

MarkUpPDF(file_path, c_words=to_cut)