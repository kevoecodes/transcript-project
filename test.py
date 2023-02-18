import pdfkit
import PyPDF2

wkhtmltopdf_config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
options = {
    'orientation': 'landscape',
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'encoding': "UTF-8",
    'quiet': ''
}
css_files = ['style1.css', 'style2.css', 'style3.css']
css_paths = ','.join(css_files)
pdfkit.from_url(
    'http://127.0.0.1:8500/transcript/1?page=1',
    'output1.pdf',
    options=options,
    configuration=wkhtmltopdf_config,
)
pdfkit.from_url(
    'http://127.0.0.1:8500/transcript/1?page=2',
    'output2.pdf',
    options=options,
    configuration=wkhtmltopdf_config,
)



# Open the first PDF file in read-binary mode
with open('output1.pdf', 'rb') as file1:

    # Open the second PDF file in read-binary mode
    with open('output2.pdf', 'rb') as file2:

        # Create a PDF file reader object for the first PDF file
        pdf_reader1 = PyPDF2.PdfReader(file1)

        # Create a PDF file reader object for the second PDF file
        pdf_reader2 = PyPDF2.PdfReader(file2)

        # Create a PDF file writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Loop through each page of the first PDF file and add it to the PDF file writer object
        for page_num in range(len(pdf_reader1.pages)):
            pdf_writer.add_page(pdf_reader1.pages[page_num])

        # Loop through each page of the second PDF file and add it to the PDF file writer object
        for page_num in range(len(pdf_reader2.pages)):
            pdf_writer.add_page(pdf_reader2.pages[page_num])

        # Open a new PDF file in write-binary mode and write the combined PDF file to it
        with open('combined.pdf', 'wb') as combined_file:
            pdf_writer.write(combined_file)
