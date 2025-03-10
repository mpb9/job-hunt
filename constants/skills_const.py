SKILLS__MASTER_REF: dict = {
    "LANG_CATEGORIES": {
        # info: LISTED IN ORDER OF PROFICIENCY/EXPERIENCE
        "frontend": ["JavaScript", "TypeScript", "HTML", "CSS"],
        "backend": ["Java", "SQL", "Python", "PHP", "C++"],
    },
    "TECH_CATEGORIES": {
        # info: LISTED IN ORDER OF PROFICIENCY/EXPERIENCE
        "backend": [
            "nodejs",
            "express",
            "django",
            "flask",
            "spring",
            "spring_boot",
            "graphql",
            "rest",
        ],
        "deployment": ["aws", "gcp", "azure", "docker", "kubernetes"],
        "database": ["postgres", "mongo", "oracle", "snowflake"],
        "frontend": ["react", "angular", "tailwindcss"],
        "management": ["git", "git_actions", "jenkins", "maven", "gradle"],
        "testing": ["junit", "jest", "pytest"],
    },
}

# MARK: LANGUAGES
LANGS = {
    "known": [
        "JavaScript",
        "Java",
        "SQL",
        "TypeScript",
        "Python",
        "HTML",
        "CSS",
        "PHP",
        "C++",
    ],
    "ranked": {
        1: "JavaScript",
        2: "Java",
        3: "SQL",
        4: "TypeScript",
        5: "Python",
        6: "HTML",
        7: "CSS",
        8: "PHP",
        9: "C++",
    },
    "key": {
        # info: ORDER MATTERS
        "javascript": "JavaScript",
        "java": "Java",
        "sql": "SQL",
        "typescript": "TypeScript",
        "python": "Python",
        "html": "HTML",
        "css": "CSS",
        "php": "PHP",
        "cpp": "C++",
    },
}

# MARK: TECHNOLOGIES
TECH = {
    "known": [
        "React",
        "Spring Boot",
        "Node.js",
        "Angular",
        "AWS",
        "Azure",
        "Flask",
        "Git",
        "MongoDB",
        "Oracle",
        "Snowflake",
        "Tailwind",
    ],
    "key": {
        # info: ORDER MATTERS
        "react": "React",  # JavaScript
        "spring_boot": "Spring Boot",  # Java
        "nodejs": "Node.js",  # JavaScript
        "angular": "Angular",  # JavaScript
        "aws": "AWS",
        "azure": "Azure",
        "flask": "Flask",  # Python
        "git": "Git",
        "mongo": "MongoDB",
        "oracle": "Oracle",
        "gcp": "GCP",
        "snowflake": "Snowflake",
        "tailwind": "Tailwind",  # CSS
        "docker": "Docker",
        "kubernetes": "Kubernetes",
        "rest": "REST",
        "spring": "Spring Framework",  # Java
        "postgres": "PostgreSQL",
        "mysql": "MySQL",
        "vue": "Vue.js",  # JavaScript
        "linux": "Linux",
        "jenkins": "Jenkins",  # Java
        "git_actions": "GitHub Actions",
        "express": "Express",  # JavaScript
        "django": "Django",  # Python
        "maven": "Maven",  # Java
        "vite": "Vite",  # JavaScript
        "gradle": "Gradle",  # Java
        "graphql": "GraphQL",
        "junit": "JUnit",  # Java
        "jest": "Jest",  # JavaScript
        "pytest": "Pytest",  # Python
    },
    "react": {"name": "React", "label": "React", "category": "frontend", "default": 1},
    "spring_boot": {
        "name": "Spring Boot",
        "label": "Spring 👢",
        "category": "backend",
        "default": 1,
    },
    "nodejs": {"name": "Node.js", "label": "Node", "category": "backend", "default": 1},
    "angular": {
        "name": "Angular",
        "label": "Angular",
        "category": "frontend",
        "default": 0,
    },
    "aws": {"name": "AWS", "label": "AWS", "category": "deployment", "default": 1},
    "azure": {
        "name": "Azure",
        "label": "Azure",
        "category": "deployment",
        "default": 0,
    },
    "flask": {"name": "Flask", "label": "Flask", "category": "backend", "default": 0},
    "git": {"name": "Git", "label": "Git", "category": "management", "default": 0},
    "mongo": {"name": "MongoDB", "label": "🥭", "category": "database", "default": 1},
    "oracle": {
        "name": "Oracle",
        "label": "Oracle",
        "category": "database",
        "default": 0,
    },
    "gcp": {"name": "GCP", "label": "GCP", "category": "deployment", "default": 0},
    "snowflake": {
        "name": "Snowflake",
        "label": "❄️",
        "category": "database",
        "default": 0,
    },
    "tailwind": {
        "name": "Tailwind",
        "label": "💨",
        "category": "frontend",
        "default": 0,
    },
    "docker": {"name": "Docker", "label": "🐳", "category": "deployment", "default": 0},
    "kubernetes": {
        "name": "Kubernetes",
        "label": "Kuber",
        "category": "deployment",
        "default": 0,
    },
    "rest": {"name": "REST", "label": "REST", "category": "backend", "default": 0},
    "spring": {
        "name": "Spring Framework",
        "label": "Spring 🖼️",
        "category": "backend",
        "default": 0,
    },
    "postgres": {
        "name": "Postgres",
        "label": "Postgres",
        "category": "database",
        "default": 0,
    },
    "mysql": {"name": "MySQL", "label": "MySQL", "category": "database", "default": 0},
    "vue": {"name": "Vue.js", "label": "Vue", "category": "frontend", "default": 0},
    "linux": {
        "name": "Linux",
        "label": "Linux",
        "category": "management",
        "default": 0,
    },
    "jenkins": {
        "name": "Jenkins",
        "label": "Jenkins",
        "category": "management",
        "default": 0,
    },
    "git_actions": {
        "name": "Actions",
        "label": "Actions",
        "category": "management",
        "default": 0,
    },
    "express": {
        "name": "Express",
        "label": "Express",
        "category": "backend",
        "default": 0,
    },
    "django": {
        "name": "Django",
        "label": "Django",
        "category": "backend",
        "default": 0,
    },
    "maven": {
        "name": "Maven",
        "label": "Maven",
        "category": "management",
        "default": 0,
    },
    "vite": {"name": "Vite", "label": "Vite", "category": "frontend", "default": 0},
    "gradle": {
        "name": "Gradle",
        "label": "Gradle",
        "category": "management",
        "default": 0,
    },
    "graphql": {
        "name": "GraphQL",
        "label": "GraphQL",
        "category": "backend",
        "default": 0,
    },
    "junit": {"name": "JUnit", "label": "JUnit", "category": "testing", "default": 0},
    "jest": {"name": "Jest", "label": "Jest", "category": "testing", "default": 0},
    "pytest": {
        "name": "Pytest",
        "label": "Pytest",
        "category": "testing",
        "default": 0,
    },
}
