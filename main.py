from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfminer import high_level
import os
if not os.path.exists('output'):
    os.makedirs('output')

pdf_filename = input('Enter pdf to split:')

inputpdf = PdfFileReader(open(pdf_filename, "rb"))

for i in range(inputpdf.numPages):
    # Get Name
    pages = [i] # just the first page

    extracted_text = high_level.extract_text(pdf_filename, "", pages)
    # print('===== EXTRACTED CONTENT ===== [START]')
    # print(extracted_text)
    # print('===== EXTRACTED CONTENT ===== [END]')

    pos_name = extracted_text.find('Name ')
    start_parse = pos_name + 5

    if pos_name == -1:
        pos_name = extracted_text.find('Name')
        start_parse = pos_name + 4

    pos_sexfemale = extracted_text.find('SexFemale')
    pos_sexmale = extracted_text.find('SexMale')

    # print(pos_name)
    # print(pos_sexfemale)
    # print(pos_sexmale)

    
    end_parse = start_parse + 15

    if pos_sexfemale == -1:
        end_parse = pos_sexmale
    elif pos_sexmale == -1:
        end_parse = pos_sexfemale
        

    extracted_name = extracted_text[start_parse:end_parse]
    print(extracted_name,'=> Processed')

    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    outputpath = './output/'

    with open(outputpath + "%s.pdf" % extracted_name, "wb") as outputStream:
        output.write(outputStream)

    # input("Press Enter to continue...")



