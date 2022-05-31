import sys
import os
from PyPDF2 import PdfFileReader
import PyPDF2
from decimal import *

print("\n Display the PDF Page dimension \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 31 April 2022 \n\n")

filepath1 = input(" Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath)

if os.path.exists(filepath + 'output.txt'):                             # remove the 'output.txt' file if already present in the folder
    os.remove(filepath + 'output.txt')

for fname in os.listdir(filepath):
    if not fname.endswith(".pdf"):
        continue
    path = os.path.join(filepath, fname) 
    print(fname)
    pdfobj = open(path, mode="rb")
    pdfread = PyPDF2.PdfFileReader(pdfobj)    
    text_file = filepath + "output.txt"    
    x = pdfread.numPages
    for i in range(x):
        input_pdf = PdfFileReader(pdfobj)
        media_box = input_pdf.getPage(0).mediaBox
        min_pt = media_box.lowerLeft                   # minimum value from pdf page i.e. (left bottom x =0, left height y =0) & output value will be in points
        max_pt = media_box.upperRight                  # maximum value from pdf page i.e. (right bottom x=value, right height y=value)
        page_num = i + 1
        pdf_width = str(round((max_pt[0] - min_pt[0]) * (Decimal(0.3527777778)), 2))         # Points value will converted into MM
        pdf_height = str(round((max_pt[1] - min_pt[1]) * (Decimal(0.3527777778)), 2))        # Points value will converted into MM
        dimension = fname + ": " + "\t" + "Page" + str(page_num) + "\t" + "Width & Height: " + "\t" + str(pdf_width) + " x " +  str(pdf_height) + "  mm" + "\n"
        f = open(text_file, "a+")
        f.write(str(dimension))
        f.close

