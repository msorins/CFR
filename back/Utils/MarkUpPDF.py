# Links
# https://pymupdf.readthedocs.io/en/latest/page/#Page.addStrikeoutAnnot

import PyPDF2
import fitz


class MarkUpPDF:
    def __init__(self, file_path, u_words=None, h_words=None, c_words=None):
        self.file_path = file_path
        if u_words is not None:
            self.u_words = [' ' + word + ' ' for word in u_words]
        if h_words is not None:
            self.h_words = [' ' + word + ' ' for word in h_words]
        if c_words is not None:
            self.c_words = [' ' + word + ' ' for word in c_words]

    # words - list of strings to be underlined
    # pdf_path - string path to the pdf file
    def mark_pdf(self):
        document = fitz.open(self.file_path)
        self.__underline_words(document)
        self.__highlight_words(document)
        self.__cut_words(document)
        doc_name = self.file_path.split('\\')[-1]
        document.save('output.pdf', garbage=4, deflate=True, clean=True)
        # return P

    def __underline_words(self, document):
        if self.u_words is None:
            return
        for page in document:
            for word in self.u_words:
                for instance in page.searchFor(word):
                    page.addUnderlineAnnot(instance)

    def __highlight_words(self, document):
        if self.h_words is None:
            return
        for page in document:
            for word in self.h_words:
                for instance in page.searchFor(word):
                    page.addHighlightAnnot(instance)

    def __cut_words(self, document):
        if self.c_words is None:
            return
        for page in document:
            for word in self.c_words:
                for instance in page.searchFor(word):
                    page.addStrikeoutAnnot(instance)


MarkUpPDF('/home/andreib/Desktop/CFR/back/Data/Cosmin.pdf', u_words=['google', 'qt'], c_words=['the', 'i'], h_words=['algorithms']).mark_pdf()

### READ IN PDF

# doc = fitz.open('..\Data\Cosmin.pdf')
# page = doc[0]
#
# text = "google"
# text_instances = page.searchFor(text)
#
# ### HIGHLIGHT
#
# for inst in text_instances:
#     highlight = page.addStrikeoutAnnot(inst)
#
#
# ### OUTPUT
#
# doc.save("output.pdf", garbage=4, deflate=True, clean=True)

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
