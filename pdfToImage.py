import fitz
import os
import PyPDF2
from PIL import Image
import pytesseract
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
pdffile = askopenfilename()
outputFile = pdffile+"text.txt"
open(outputFile, "w+")
reader = PyPDF2.PdfFileReader(open("HW 6.pdf", mode="rb"))
pages = reader.getNumPages()
doc = fitz.open(pdffile)
custom_config = ("r'-l eng + equ --psm 6'")
for i in range(0 , pages):
    page = doc.loadPage(i)  # number of page
    pix = page.get_pixmap(dpi=600)
    outputName = "outfile" + str(i+1) + ".png"
    pix.save(outputName)
    custom_config = r'-l eng + equ --psm 6'
    data_eng = pytesseract.image_to_string(Image.open(outputName), config=custom_config)
    os.remove(outputName)
    file = open(outputFile, "a+")
    file.write(data_eng)
    file.close()