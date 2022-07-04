from PyPDF2 import PdfReader

class PdfConsult:
    def __init__(self, path):
        self.path = path
        self.file = path

    def getContentPDF(self, path):
        txt = ""
        file = str(self.path)
        reader = PdfReader(file)
        pg_cont = len(reader.pages)
        for i in range(0, pg_cont):
            page = reader.pages[i].extract_text()
            txt += page + "\n"
            txt.lower()
        #self.file = file
