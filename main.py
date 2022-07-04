from PyPDF2 import PdfReader

reader = PdfReader('Lei 14310 CEDM.pdf')
# page = reader.pages[1]

pg_cont = len(reader.pages)
txt = ""
for i in range(0, pg_cont):
    page = reader.pages[i].extract_text()
    #print(page)
    txt += page + "\n"

with open("content.txt", "a") as arquivo:
    arquivo.write(txt)
    
# print(txt)
# print(page.extract_text())

#text = page.extract_text()

# print(type(text))

#my_list = ['camaradagem', '4º', '3º', 'bjalskliak']

#for i in my_list:
    #if i in text:
        #print(f'Parâmetro << {i} >> localizado.')

    #else:
        #print(f'Parâmetro << {i} >> não encontrado.')
