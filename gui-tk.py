import tkinter as tk

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

button = tk.Button(root, text="Resume Dir")
button.pack()

root.mainloop()
