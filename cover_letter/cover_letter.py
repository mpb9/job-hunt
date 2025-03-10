import getopt
import sys

import docx

from constants.skills_const import LANGS, TECH
from cover_letter.os_control import save_docx, save_docx_as_pdf
from cover_letter.to_docx import init_docx, write_docx
from cover_letter.utils import convert_list_to_str, parse_arg, parse_arg_list

input_args = {
    "short": "c:r:l:t:a:h:o:d:",
    "long": [
        "company=",
        "role=",
        "languages=",
        "technologies=",
        "attribute=",
        "hiring-manager=",
        "organization=",
        "company-different=",
    ],
}
company = None
role = None
languages = {
    "known": LANGS["known"],
    "required": None,
    "combined": None,
}
technologies = {
    "known": TECH["known"],
    "required": None,
    "combined": None,
}
attribute = 10
hiring_manager = "Hiring Team"
organization = None
company_different = None

if __name__ == "__main__":
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, input_args["short"], input_args["long"])
    except:
        print("Error: Invalid arguments")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-c", "--company"):
            company = parse_arg(arg)
        elif opt in ("-r", "--role"):
            role = parse_arg(arg)
        elif opt in ("-l", "--languages"):
            required_lang_list = parse_arg_list(arg)
            languages["required"] = convert_list_to_str(required_lang_list.copy())
            languages["combined"] = convert_list_to_str(
                required_lang_list, languages["known"]
            )
        elif opt in ("-t", "--technologies"):
            required_tech_list = parse_arg_list(arg)
            technologies["required"] = convert_list_to_str(required_tech_list.copy())
            technologies["combined"] = convert_list_to_str(
                required_tech_list, technologies["known"], 3
            )
        elif opt in ("-a", "--attribute"):
            attribute = int(parse_arg(arg))
        elif opt in ("-h", "--hiring-manager"):
            hiring_manager = parse_arg(arg)
        elif opt in ("-o", "--organization"):
            organization = parse_arg(arg)
        elif opt in ("-d", "--company-alternate"):
            company_different = parse_arg(arg)

    docx = init_docx()
    docx = write_docx(
        docx,
        company,
        role,
        languages,
        technologies,
        attribute,
        hiring_manager,
        organization,
        company_different,
    )
    save_docx(docx, company)
    save_docx_as_pdf(company)
