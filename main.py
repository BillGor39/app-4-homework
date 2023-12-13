from fpdf import FPDF
import glob
from pathlib import Path

# Read the file from a folder
filepaths = glob.glob("Texts/*.txt")

# Create a pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each txt file
for filepath in filepaths:
    # Get the file name
    filename = Path(filepath).stem
    name = filename.title()

    # Add a page to the PDF file
    pdf.add_page()

    # Write the page name to the PDF file
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=name, ln=1)

    # Read the data from the file
    with open(filepath, "r") as file:
        content = file.read()

    # Write the content to the page
    pdf.set_font(family="Times", style="", size=12)
    pdf.multi_cell(w=0, h=5, txt=content, border=0)


# Generate the PDF file
pdf.output("PDFs/output.pdf")

