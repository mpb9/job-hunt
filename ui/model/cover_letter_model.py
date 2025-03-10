import cover_letter.cover_letter as cover_letter
from constants.skills_const import LANGS, TECH


class CoverLetterModel:
    company: str = cover_letter.company
    role: str = cover_letter.role
    languages: dict = cover_letter.languages
    technologies: dict = cover_letter.technologies
    attribute: int = cover_letter.attribute
    hiring_manager: str = cover_letter.hiring_manager
    organization: str = cover_letter.organization
    company_different: str = cover_letter.company_different

    language_key: dict = LANGS["key"]
    technology_key: dict = TECH
