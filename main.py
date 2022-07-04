from PyPDF2 import PdfReader

def getContentPDF(path):
    txt = ""
    file = str(path)
    reader = PdfReader(file)
    pg_cont = len(reader.pages)
    for i in range(0, pg_cont):
        page = reader.pages[i].extract_text()
        txt += page + "\n"
    return txt.lower()

consult_file = getContentPDF('Lei 14310 CEDM.pdf')

consults = [
    '4º',
    'comenda',
    'estadual',
    'laksjdlaks',
    'hjahsdkj',
]

for i in consults:
    if i in consult_file:
        print(f'{i} is in your file')
    else:
        print(f'{i} is NOT in your file')

# writing the test result in a txt file 
#with open("content.txt", "a") as arquivo:
#   arquivo.write(consult_file)
#
#arquivo.close()