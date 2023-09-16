import PyPDF2

with open("./files/dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    page.rotate(270)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("./files/updated_dummy.pdf", "wb") as new_file:
        writer.write(new_file)
