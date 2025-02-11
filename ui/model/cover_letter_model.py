import cover_letter.cover_letter as cover_letter


class CoverLetterModel:
    company: str = cover_letter.company
    role: str = cover_letter.role
    languages: dict = cover_letter.languages
    technologies: dict = cover_letter.technologies
    attribute: int = cover_letter.attribute
    hiring_manager: str = cover_letter.hiring_manager
    organization: str = cover_letter.organization
    company_different: str = cover_letter.company_different

    # rename
    language_key: dict = {
        "javascript": "JavaScript",
        "python": "Python",
        "java": "Java",
        "sql": "SQL",
        "typescript": "TypeScript",
        "html": "HTML",
        "css": "CSS",
        "php": "PHP",
    }

    technology_key: dict = {
        "angular": "Angular",
        "react": "React",
        "spring_boot": "Spring Boot",
        "flask": "Flask",
        "aws": "AWS",
        "gcp": "GCP",
        "oracle": "Oracle",
        "tailwindcss": "TailwindCSS",
    }
