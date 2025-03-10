from cover_letter.os_control import delete_docx, save_docx, save_docx_as_pdf
from cover_letter.to_docx import init_docx, write_docx
from cover_letter.utils import convert_list_to_str
from ui.model.cover_letter_model import CoverLetterModel


# MARK: VIEW TO MODEL
def view_to_model(data):
    cl_model = CoverLetterModel()

    cl_model.company = data["company"]
    cl_model.role = data["role"]
    cl_model.organization = data["organization"] if data["organization"] != "" else None
    cl_model.attribute = int(data["attribute"])
    cl_model.hiring_manager = (
        data["hiring_manager"] if data["hiring_manager"] != "" else "Hiring Team"
    )
    cl_model.company_different = (
        data["company_different"] if data["company_different"] != "" else None
    )

    # info: LANGUAGES
    required_lang_list = []
    for key in cl_model.language_key:
        if data[key]:
            required_lang_list.append(cl_model.language_key[key])

    if data["custom_lang_0"] != "":
        required_lang_list.append(data["custom_lang_0"])

    cl_model.languages["required"] = convert_list_to_str(required_lang_list.copy())
    cl_model.languages["combined"] = convert_list_to_str(
        required_lang_list, cl_model.languages["known"]
    )

    if cl_model.languages["required"] == None:
        cl_model.languages["required"] = convert_list_to_str(
            [], cl_model.languages["known"], 3
        )

    # info: TECHNOLOGIES
    required_tech_list = []
    for id in cl_model.technology_key:
        if data[id]:
            required_tech_list.append(cl_model.technology_key[id]["name"])

    if data["custom_tech_0"] != "":
        required_tech_list.append(data["custom_tech_0"])
    if data["custom_tech_1"] != "":
        required_tech_list.append(data["custom_tech_1"])
    if data["custom_tech_2"] != "":
        required_tech_list.append(data["custom_tech_2"])

    # cl_model.technologies["required"] = convert_list_to_str(required_tech_list.copy())
    cl_model.technologies["combined"] = convert_list_to_str(
        required_tech_list, cl_model.technologies["known"], 4
    )

    # if cl_model.technologies["required"] == None:
    #     cl_model.technologies["required"] = convert_list_to_str(
    #         [], cl_model.technologies["known"], 4
    #     )

    return cl_model


# MARK: CREATE
def create_cover_letter(data):
    docx = None

    try:
        cl_model = view_to_model(data)

        docx = init_docx()
        docx = write_docx(
            docx,
            cl_model.company,
            cl_model.role,
            cl_model.languages,
            cl_model.technologies,
            cl_model.attribute,
            cl_model.hiring_manager,
            cl_model.organization,
            cl_model.company_different,
        )
        save_docx(docx, cl_model.company)
        save_docx_as_pdf(cl_model.company)

        if not data["keep_docx"]:
            delete_docx(cl_model.company)

    except Exception as e:
        print(f"Error: {e}")

    else:
        return docx
