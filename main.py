from fpdf import FPDF
import glob
from pathlib import Path

# Read the file from a folder
filepaths = glob.glob("Texts/*.txt")

# Create a pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each txt file
for filepath in filepaths:
    # Read the data from the file
    data = open(filepath, "r")

    # Get the file name
    filename = Path(filepath).stem
    name = filename.title()

    # Add a page to the PDF file
    pdf.add_page()

    # Write the name to the PDF file
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=name)

# Generate the PDF file
pdf.output("PDFs/output.pdf")

