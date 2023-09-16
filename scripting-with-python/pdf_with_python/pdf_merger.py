import sys
import PyPDF2

inputs = sys.argv[1:]


def merge_pdf(list):
    merger = PyPDF2.PdfMerger()
    for pdf in list:
        merger.append(pdf)

    merger.write("./files/super.pdf")


merge_pdf(inputs)
