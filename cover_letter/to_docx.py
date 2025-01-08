import os
from datetime import datetime
from docx import Document, shared
from utils import format_date, skip_line
from constants.paragraphs import INTRO, BODY1, BODY2, CONCLUSION
from constants.attributes import COMPANY_ATTRIBUTES, PERSONAL_ATTRIBUTES
from constants.files import DOCX_FILE


# MARK: INITIALIZE .DOCX
def init_docx():
    docx = Document()
    docx.styles["Normal"].font.name = "Times New Roman"
    docx.styles["Normal"].font.size = shared.Pt(12)
    docx.styles["Normal"].paragraph_format.line_spacing = 1
    docx.styles["Normal"].paragraph_format.space_before = shared.Pt(0)
    docx.styles["Normal"].paragraph_format.space_after = shared.Pt(0)
    docx.sections[0].left_margin = shared.Inches(1)
    docx.sections[0].right_margin = shared.Inches(1)
    docx.sections[0].top_margin = shared.Inches(1)
    docx.sections[0].bottom_margin = shared.Inches(1)
    docx.sections[0].page_width = shared.Inches(8.5)
    docx.sections[0].page_height = shared.Inches(11)
    return docx


# MARK: WRITE .DOCX
def write_docx(
    docx: Document,
    company: str,
    role: str,
    languages: dict,
    technologies: dict,
    attribute: int,
    hiring_manager: str,
):
    docx.add_paragraph("Michael Beebe")
    docx.add_paragraph("New York, NY")
    docx.add_paragraph("(847) 274-3448")
    docx.add_paragraph("michaelbeebe1031@gmail.com")
    skip_line(docx)
    docx.add_paragraph(format_date())
    skip_line(docx)

    if hiring_manager != "Hiring Manager":
        docx.add_paragraph(hiring_manager)
        docx.add_paragraph("Hiring Manager")
        docx.add_paragraph(company)
        skip_line(docx)

    docx.add_paragraph(f"Dear {hiring_manager},")
    skip_line(docx)

    docx.add_paragraph(
        INTRO.replace("[COMPANY]", company)
        .replace("[ROLE]", role)
        .replace("[LANGUAGES]", languages["required"])
        .replace("[COMPANY_ATTRIBUTE]", COMPANY_ATTRIBUTES[attribute])
        .replace("[PERSONAL_ATTRIBUTE]", PERSONAL_ATTRIBUTES[attribute])
    )
    skip_line(docx)
    docx.add_paragraph(BODY1)
    skip_line(docx)
    docx.add_paragraph(
        BODY2.replace("[LANGUAGES]", languages["combined"])
        .replace("[COMPANY]", company)
        .replace("[TECHNOLOGIES]", technologies["required"])
    )
    skip_line(docx)
    docx.add_paragraph(CONCLUSION.replace("[COMPANY]", company).replace("[ROLE]", role))
    skip_line(docx)

    docx.add_paragraph(f"Sincerely,")
    skip_line(docx)
    docx.add_paragraph("Michael Beebe")
    return docx


# MARK: SAVE .DOCX
def save_docx(docx: Document, company):
    file_path = f"{DOCX_FILE["path"]}{DOCX_FILE["name"]}_{company}.docx"

    if os.path.exists(file_path):
        os.remove(file_path)

    docx.core_properties.created = datetime.now()
    docx.save(file_path)
