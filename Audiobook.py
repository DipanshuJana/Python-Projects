import PyPDF2
import pyttsx3
import datetime
import os    
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

converter = pyttsx3.init()
converter.setProperty('rate', 160)
converter.setProperty('volume', 1)
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id)

def readFile(path):
    with open(path, "rb") as book:
        pdf_reader = PyPDF2.PdfFileReader(book)

        pages = pdf_reader.numPages
        print("Total Pages: ", pages)

        for page_num in range(pages):
            print("Current page: ", page_num + 1)
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            print(text)
            curr_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            converter.save_to_file(text, f"{curr_datetime}.mp3")
            converter.runAndWait()
        converter.runAndWait()

readFile("1.pdf");

# www.gcptutorials.com/post/python-extract-text-from-pdf-files