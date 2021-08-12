"""
A very long pdf page will be formate to small pages to get print.

prerequist libraries -> PyPDF2

usage ->
===> To change all the files present in folder
        1) change dirctory_path
        2) run main 
        3) change output location

===> To change single file
        1) change file_path
        2) change output location

"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def formate_pdf_to_A4(file_name, file_path, output_path):
    print(f"processing - {file_name}")
    
    file_path += '/' + file_name
    with open(file_path, 'rb') as file:
        pdf = PdfFileReader(file)
    output = PdfFileWriter()
    page = pdf.getPage(0)
    orignal_size = page.mediaBox.getUpperRight_y()

    top = 0
    bottom = 1500
    while top < orignal_size:
        
        file = open(file_path, 'rb')
        pdf = PdfFileReader(file) 
        page = pdf.getPage(0)
        
        page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y() - top)
        page.mediaBox.lowerLeft  = (0, page.mediaBox.getUpperRight_y()  - bottom)
        output.addPage(page)

        top += bottom

    outputStream = open(f"{output_path}/{file_name}",'wb') 
    output.write(outputStream) 
    outputStream.close()

    print(f'Done... {file_name}\n')


def main(dir_path, output_path):
    for file_name in os.listdir(dir_path):
        formate_pdf_to_A4(file_name, dir_path, output_path)


dir_path = './tmp'
output_path = './result'

main(dir_path, output_path)
