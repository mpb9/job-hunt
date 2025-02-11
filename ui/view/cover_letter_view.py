from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length


class CoverLetterForm(FlaskForm):
    company = StringField(
        label="company",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "COMPANY", "autofocus": True, "autocomplete": "on"},
    )
    role = StringField(
        label="role",
        default="Software Engineer",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "ROLE", "autocomplete": "on"},
    )
    organization = StringField(
        label="organization",
        render_kw={"placeholder": "ORGANIZATION", "autocomplete": "on"},
    )
    hiring_manager = StringField(
        label="hiring_manager",
        default="Hiring Team",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "HIRING TEAM", "autocomplete": "on"},
    )
    company_different = StringField(
        label="company_different",
        render_kw={"placeholder": "COMPANY ALT", "autocomplete": "on"},
    )

    # Languages
    javascript = BooleanField(
        label="JavaScript", default=1, render_kw={"class": "lang"}
    )
    python = BooleanField(label="Python", default=0, render_kw={"class": "lang"})
    java = BooleanField(label="Java", default=0, render_kw={"class": "lang"})
    sql = BooleanField(label="SQL", default=1, render_kw={"class": "lang"})
    typescript = BooleanField(
        label="TypeScript", default=0, render_kw={"class": "lang"}
    )
    html = BooleanField(label="HTML", default=0, render_kw={"class": "lang"})
    css = BooleanField(label="CSS", default=0, render_kw={"class": "lang"})
    php = BooleanField(label="PHP", default=0, render_kw={"class": "lang"})
    custom_lang_0 = StringField(
        label="Custom Language 0",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "lang"},
    )
    custom_lang_1 = StringField(
        label="Custom Language 1",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "lang"},
    )

    # Technologies
    angular = BooleanField(label="Angular", default=0, render_kw={"class": "tech"})
    react = BooleanField(label="React", default=1, render_kw={"class": "tech"})
    spring_boot = BooleanField(label="Spring", default=0, render_kw={"class": "tech"})
    flask = BooleanField(label="Flask", default=0, render_kw={"class": "tech"})
    aws = BooleanField(label="AWS", default=1, render_kw={"class": "tech"})
    gcp = BooleanField(label="GCP", default=0, render_kw={"class": "tech"})
    oracle = BooleanField(label="Oracle", default=0, render_kw={"class": "tech"})
    tailwindcss = BooleanField(label="Tailwind", default=0, render_kw={"class": "tech"})
    custom_tech_0 = StringField(
        label="Custom Technology 0",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )
    custom_tech_1 = StringField(
        label="Custom Technology 1",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )
    custom_tech_2 = StringField(
        label="Custom Technology 2",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )
    custom_tech_3 = StringField(
        label="Custom Technology 3",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )

    # Attribute
    attribute = SelectField(
        label="Attributes",
        default=3,
        choices=[
            (
                1,
                "innovative CULTURE - passion for creativity and forward-thinking solutions",
            ),
            (
                2,
                "COLLABORATION - ability to thrive in team-oriented environments",
            ),
            (
                3,
                "LEARNING and growth - dedication to personal and professional development",
            ),
            (
                4,
                "USER-CENTRIC solutions - strong drive to create impactful, user-friendly systems",
            ),
            (
                5,
                "technical EXCELLENCE - passion for delivering high-quality, scalable solutions",
            ),
            (
                6,
                "MISSION-DRIVEN approach - enthusiasm for tackling meaningful challenges",
            ),
            (
                7,
                "FAST-PACED environment - ability to adapt quickly and stay focused under pressure",
            ),
            (
                8,
                "fostering INNOVATION - excitement for leveraging technology to create change",
            ),
            (
                9,
                "DIVERSITY and inclusion - belief in creating equitable and inclusive solutions",
            ),
            (
                10,
                "COMMUNITY and purpose - commitment to contributing to meaningful, mission-driven work",
            ),
        ],
        validators=[DataRequired()],
    )

    # Submit
    submit = SubmitField(name="submit", id="submit", render_kw={"value": "execute"})
    keep_docx = BooleanField(label=".docx", default=0)
