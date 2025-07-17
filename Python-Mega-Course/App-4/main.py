import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="portrait", unit="mm", format="A4")

for files in filepaths:
    pdf.add_page()
    filename = Path(files).stem
    name = filename.title()
    pdf.set_font(family="Times",size= 16, style="B")
    pdf.cell(w=50, h=8, txt=name,ln=1)

    with open(files,"r") as file:
        content = file.read()
    
    pdf.set_font(family="Times", size =12)
    pdf.multi_cell(w=0,h=6,txt=content)

pdf.output("the_ouput.pdf")

