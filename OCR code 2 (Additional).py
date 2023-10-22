import os
import glob
from pdfminer.high_level import extract_text
import pdfplumber
import pandas as pd
import camelot
import openpyxl as op
import numpy as np
import tabula
import re
import cv2 
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
from pytesseract import image_to_string
import datefinder


#construction of the functions

def convert_pdf_to_img(pdf_file):
    """
    @desc: this function converts a PDF into Image
    
    @params:
        - pdf_file: the file to be converted
    
    @returns:
        - an interable containing image format of all the pages of the PDF
    """
    return convert_from_path(pdf_file, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')


def convert_image_to_text(file, psm):
    """
    @desc: this function extracts text from image
    
    @params:
        - file: the image file to extract the content
    
    @returns:
        - the textual content of single image
    """
    custom_config = f"-l eng --oem 1 --psm {psm}"
    text = image_to_string(file, config = custom_config)
    return text


def get_text_from_any_pdf(pdf_file, psm):
    """
    @desc: this function is our final system combining the previous functions
    
    @params:
        - file: the original PDF File
    
    @returns:
        - the textual content of ALL the pages
    """
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        final_text += os.linesep
        final_text += "Page n°{}".format(pg)
        final_text += os.linesep
        final_text += convert_image_to_text(img,psm)
        #print("Page n°{}".format(pg))
        #print(convert_image_to_text(img))
    
    return final_text




#calling the function

print(get_text_from_any_pdf("TETUAN MASJID NURUL HIKMAH.pdf", 12)) #note that the PSM defines the OCR formatting criteria. I used no. 12 here. You can test any other numbers you want for getting the best OCR results


