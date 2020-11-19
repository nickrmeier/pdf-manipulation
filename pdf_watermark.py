from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import sys

original = sys.argv[1]
watermark = sys.argv[2]

with open(original, 'rb') as input_file, open(watermark, 'rb') as watermark_file:
    input_pdf = PdfFileReader(input_file)
    watermark_pdf = PdfFileReader(watermark_file)
    watermark_page = watermark_pdf.getPage(0)
    # merger = PyPDF2.PdfFileMerger()

    output = PdfFileWriter()

    for i in range(input_pdf.getNumPages()):
        pdf_page = input_pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        output.addPage(pdf_page)

    with open('super_watermarked.pdf', 'wb') as merged_file:
        output.write(merged_file)
