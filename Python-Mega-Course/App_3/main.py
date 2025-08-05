from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit = "mm", format="A4")
df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(50,123,173)
    pdf.cell(w = 0, h=12, txt = row["Topic"], align="L", ln=1)
    pdf.line(10,20,200,20)

    for i in range(20,298,10):
        pdf.line(10,i,200,i)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        for i in range(20,298,10):
            pdf.line(10,i,200,i)

pdf.output("output.pdf")