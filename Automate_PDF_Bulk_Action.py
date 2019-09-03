from pdf2image import convert_from_path
from PIL import Image
import PyPDF2
from pdf2image import exceptions

while True:
    try:
        pdfName = input("Please enter the name of the pdf, here is an example: 'myPdf.pdf' "
                        " make sure the pdf is in the same folder as this .py application: ")
        pages = convert_from_path(pdfName, 1000, '/')  # 2nd parameter determines DPI (resolution)
        break
    except exceptions.PDFPageCountError:
        print("Oops! That was not a valid file name. "
              "My suggestion would be: right click and copy the file name, then paste it here!")

counter = 0
string_out = ''  # name of the output file
string_Parse = ''  # each individual page in the PDF file turned into String

pdfFileObj = open(pdfName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for page in pages:  # Converts each page into String, removes whitespace, then checks for text
    pageObj = pdfReader.getPage(counter)
    string_Parse = pageObj.extractText()
    string_Parse = string_Parse.replace(" ", "")  # removes all white space to avoid ambiguity

    # Testing only:
    # print(string_Parse)
    # print(counter)

    if "thetrademarkidentifiedbelowhas" in string_Parse:  # change the string depending on the needs of the user
        string_out = str(counter) + pdfName + 'out.jpg'
        page.save(string_out, 'jpeg')
        img = Image.open(string_out)
        new_img = img.resize((285, 368), Image.ANTIALIAS)  # change the dimension of the output image as required
        quality_val = 100  # Can be changed according to needs
        new_img.save(string_out, "JPEG", quality=quality_val)
    counter += 1
