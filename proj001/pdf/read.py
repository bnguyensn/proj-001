from PyPDF2 import PdfFileReader


def get_info(p: str) -> dict:
    """"Return a dictionary containing the basic information of a .pdf"""

    with open(p, 'rb') as f:
        pdf = PdfFileReader(f)
        return pdf.getDocumentInfo()
