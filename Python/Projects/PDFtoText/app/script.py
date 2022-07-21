#!/usr/bin/env python3
"""
created: 2022-07-20 20:20:16
@author: seraph★776
contact: seraph776@gmail.com
project: Extract Text from PDF
license: MIT
"""

import PyPDF2


# STEP 1: open PDF and convert to text
def extract_text_from_pdf(pdf_filename: str) -> str:
    text_output = ''
    with open(pdf_filename, 'rb') as pdf_object:
        pdf_reader = PyPDF2.PdfFileReader(pdf_object)
        for i in range(0, pdf_reader.numPages):
            page_obj = pdf_reader.getPage(i)
            text_output += page_obj.extractText()
    return text_output


# STEP 2: Save Text to File
def save_converted_text(text_file: str, filename: str) -> None:
    with open(filename, 'w+', encoding='utf8') as file_obj:
        file_obj.write(text_file)
    print(f'{text_file} has been successfully saved.')


if __name__ == '__main__':
    # extract text from PDF
    text_from_pdf = extract_text_from_pdf('theraven.pdf')
    # save extracted text
    save_converted_text(text_from_pdf, 'theraven.txt')
