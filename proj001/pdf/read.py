from PyPDF2 import PdfFileReader


def get_num_pages(p):
    """Return the pdf object"""

    with open(p, 'rb') as f:
        pdf = PdfFileReader(f)
        return pdf.getNumPages()


def get_info(p):
    """
    Return a DocumentInformation object containing the basic information
    of the .pdf
    """
    with open(p, 'rb') as f:
        pdf = PdfFileReader(f)
        return pdf.getDocumentInfo()
