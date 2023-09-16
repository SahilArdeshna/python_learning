import sys
import PyPDF2

subject = sys.argv[1]
watermaker = sys.argv[2]


def add_watermark(subject_pdf, watermaker_pdf):
    subject_reader = PyPDF2.PdfReader(subject_pdf)
    subject_reader_length = len(subject_reader.pages)

    writer = PyPDF2.PdfWriter()
    for index in list(range(0, subject_reader_length)):
        subject_page = subject_reader.pages[index]
        mediabox = subject_page.mediabox

        watermark_reader = PyPDF2.PdfReader(watermaker_pdf)
        watermark_page = watermark_reader.pages[0]

        watermark_page.merge_page(subject_page)
        watermark_page.mediabox = mediabox
        writer.add_page(watermark_page)

    with open("./files/watermark.pdf", "wb") as file:
        writer.write(file)


add_watermark(subject, watermaker)
