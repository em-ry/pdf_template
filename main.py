from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
# stop auto page break so nothing spills over into the next page
pdf.set_auto_page_break(auto=False, margin=0)

for index, rows in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=rows["Topic"], ln=1, align='L')
    # the numbers below represents: x1,y1 x2,y2(i.e. coordinates)
    pdf.line(10, 26, 200, 26)

    # Set the footer
    pdf.ln(250)
    pdf.set_font(family='Times', style='BI', size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=rows["Topic"], align='R')

    # create other pages after the header
    for i in range(rows["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(275)
        pdf.set_font(family='Times', style='BI', size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=rows["Topic"], align='R')

pdf.output('output.pdf')
