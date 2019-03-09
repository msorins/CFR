class MarkUpPDF:
    def __init__(self):
        pass

import fitz

### READ IN PDF

doc = fitz.open('..\Data\Cosmin.pdf')
page = doc[0]

text = "google"
text_instances = page.searchFor(text)

### HIGHLIGHT

for inst in text_instances:
    highlight = page.addStrikeoutAnnot(inst)


### OUTPUT

doc.save("output.pdf", garbage=4, deflate=True, clean=True)

# pdfInput = PdfFileReader(open('..\Data\Cosmin.pdf', "rb"))
# pdfOutput = PdfFileWriter()
#
# page1 = pdfInput.getPage(0)
#
# highlight = createHighlight(100, 400, 400, 500, {
#     "author": "",
#     "contents": "Bla-bla-bla"
# })
#
# addHighlightToPage(highlight, page1, pdfOutput)
#
# pdfOutput.addPage(page1)
#
# outputStream = open("output.pdf", "wb")
# pdfOutput.write(outputStream)