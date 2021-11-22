import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader
import PyPDF2
from io import BytesIO
from OpenGovCore.models import Bills
import os
import tempfile
EOF_MARKER = b'%%EOF'
def bills_details_scraper(url):
    #sources = Bills.objects.values('source')
    #for source in sources:
    url = url
    file_name = url.rsplit("/")[-1].split('.')
    file_name = file_name[0]+'.txt'
    pdf_bytes = requests.get(url).content
    p = BytesIO(pdf_bytes)
    p.seek(0, os.SEEK_END)
    try:
        read_pdf = PyPDF2.PdfFileReader(p)
        number_of_pages = read_pdf.getNumPages()
        #print(source)
        #print(number_of_pages)
        pdf_text=""
        for p in range(number_of_pages):
            page=read_pdf.getPage(p)
            text = page.extractText()
            text = text.replace('\n', ' ')
            pdf_text+= str(text)
    except:
        exit
    pdf_text = pdf_text
    #bill_temp = pdf_to_text_file(pdf_text)
    return file_name,pdf_text

def pdf_to_text_file(pdf_text):
    temp_data = tempfile.NamedTemporaryFile(mode='w+t',delete=True)
    try:
        temp_data.write(pdf_text)
        temp_data.flush()
        #temp_data.seek(0)
        #data = temp_data.read()
        print("File written")
    except:
        print("Not written")
        exit
    return temp_data
