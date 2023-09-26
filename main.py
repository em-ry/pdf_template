from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
for index, rows in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=rows["Topic"], ln=1, align='L')
    # the numbers below represents: x1,y1 x2,y2(i.e. coordinates)
    pdf.line(10, 26, 200, 26)

    # create other pages after the header
    for i in range(rows["Pages"] - 1):
        pdf.add_page()

pdf.output('output.pdf')
