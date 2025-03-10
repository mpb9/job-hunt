import os
import stat
from datetime import datetime

from docx2pdf import convert

from constants.cover_letter_const import DOCX_FILE, PDF_FILE


def make_directory_if_not_exists(directory_path: str):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        os.chmod(
            directory_path,
            stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH,
        )


def alter_file_if_exists(
    file_name: str,
    file_type: str,
    directory_path: str,
    how: str = "rename",
):
    file_path = f"{directory_path}/{file_name}.{file_type}"
    if os.path.exists(file_path):
        match how:
            case "remove":
                os.remove(file_path)
            case "rename":
                iterations = 1
                while os.path.exists(
                    f"{directory_path}/{file_name}_{iterations}.{file_type}"
                ):
                    iterations += 1
                os.rename(
                    file_path, f"{directory_path}/{file_name}_{iterations}.{file_type}"
                )


def delete_docx(company):
    directory_path = f"{DOCX_FILE["path"]}{company}"
    file_path = f"{directory_path}/{DOCX_FILE["name"]}.docx"
    if os.path.exists(file_path):
        os.remove(file_path)


def save_docx(docx, company):
    directory_path = f"{DOCX_FILE["path"]}{company}"
    make_directory_if_not_exists(directory_path)

    file_path = f"{directory_path}/{DOCX_FILE["name"]}.docx"
    alter_file_if_exists(DOCX_FILE["name"], "docx", directory_path, "rename")

    docx.core_properties.created = datetime.now()
    docx.save(file_path)

    # Set permissions to rw-r--r--
    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


def save_docx_as_pdf(company):
    docx_filepath = f"{DOCX_FILE["path"]}{company}/{DOCX_FILE['name']}.docx"

    directory_path = f"{PDF_FILE['path']}{company}"
    make_directory_if_not_exists(directory_path)

    pdf_filepath = f"{directory_path}/{PDF_FILE['name']}.pdf"
    alter_file_if_exists(PDF_FILE["name"], "pdf", directory_path, "rename")

    convert(docx_filepath, pdf_filepath)
