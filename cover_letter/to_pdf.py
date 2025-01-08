import os
from docx2pdf import convert
from constants.files import DOCX_FILE, PDF_FILE


def save_docx_as_pdf(company, move_to: str = None) -> None:
    docx_filepath = f"{DOCX_FILE['path']}{DOCX_FILE['name']}_{company}.docx"
    pdf_filepath = f"{PDF_FILE['path']}{PDF_FILE['name']}_{company}.pdf"

    if move_to:
        pdf_filepath = f"{move_to}{DOCX_FILE['name']}_{company}.pdf"

    if os.path.exists(pdf_filepath):
        os.remove(pdf_filepath)

    convert(docx_filepath, pdf_filepath)
