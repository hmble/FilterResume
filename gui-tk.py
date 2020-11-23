# gui import
import tkinter as tk
from tkinter import filedialog
from tkinter import Text

# extracting text import
import os
import docx
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# Extract text from docx file


def getDocxText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    original_text = '\n'.join(fullText)
    filter_text = "\n".join([ll.rstrip() for ll in original_text.splitlines() if
                             ll.strip()])
    return filter_text.lower()

# Extract text from PDF files.


def getPDFText(filename):
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    original_text = output_string.getvalue()
    filter_text = "\n".join([ll.rstrip() for ll in original_text.splitlines() if
                             ll.strip()])

    return filter_text.lower()

# get keyword count


def getCount(filter_text, keyword):
    return filter_text.count(keyword.lower())


# Notes
#
# To open a pdf with adobe you need pass an argument of pdfpath to .exe file
# like below:
# <Acrobat path> /A "<parameter>=<value>" "<PDF path>"
# Reference: https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/pdf_open_parameters.pdf
# for this we need to use os.subprocess(exepath, arguments)
# canvas size
HEIGHT = 800
WIDTH = 800

root = tk.Tk()


# canvas size
#
# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()

e = tk.Entry(root)
e.pack()

dirname = ""


def callback():
    global dirname
    dirname = filedialog.askdirectory()


def recursive_read():
    global dirname
    for root, subdir, files in os.walk(dirname):
        for docs in files:
            text = get_text(os.path.join(root, docs))
            count = getCount(text, e.get())
            print('{}: {}'.format(docs, count))


def get_text(filename):
    if filename.lower().endswith('.pdf'):
        text = getPDFText(filename)
        return text
    elif filename.lower().endswith('.docx'):
        text = getDocxText(filename)
        return text
    else:
        return ""


button = tk.Button(root, text="Open directory", command=callback)
button.pack()

buttonCommit = tk.Button(root, height=1, width=10, text="Print count",
                         command=recursive_read)
# command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()


root.mainloop()
