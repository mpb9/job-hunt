from ensurepip import bootstrap  # ! not sure if this is needed

from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from constants.cover_letter_const import ATTRIBUTES
from constants.skills_const import TECH

render_tech: dict[str, str] = {"class": "tech"}
render_lang: dict[str, str] = {"class": "lang"}


class CoverLetterForm(FlaskForm):
    # MARK: COMPANY
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
        render_kw={"placeholder": "ORGANIZATION", "autocomplete": "off"},
    )
    hiring_manager = StringField(
        label="hiring_manager",
        default="Hiring Team",
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={"placeholder": "HIRING TEAM", "autocomplete": "off"},
    )
    company_different = StringField(
        label="company_different",
        render_kw={"placeholder": "COMPANY ALT", "autocomplete": "off"},
    )

    # MARK: LANG
    javascript = BooleanField(label="JS", default=1, render_kw=render_lang)
    java = BooleanField(label="☕", default=1, render_kw=render_lang)
    sql = BooleanField(label="SQL", default=1, render_kw=render_lang)
    typescript = BooleanField(label="TS", render_kw=render_lang)
    python = BooleanField(label="🐍", render_kw=render_lang)
    html = BooleanField(label="HTML", render_kw=render_lang)
    css = BooleanField(label="CSS", render_kw=render_lang)
    php = BooleanField(label="PHP", render_kw=render_lang)
    cpp = BooleanField(label="C++", render_kw=render_lang)  # not in form
    custom_lang_0 = StringField(
        label="Custom Lang 0",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "lang"},
    )

    # MARK: TECH
    # info: Frontend
    react = BooleanField(
        label=TECH["react"]["label"],
        default=TECH["react"]["default"],
        render_kw=render_tech,
    )
    angular = BooleanField(
        label=TECH["angular"]["label"],
        default=TECH["angular"]["default"],
        render_kw=render_tech,
    )
    vue = BooleanField(
        label=TECH["vue"]["label"],
        default=TECH["vue"]["default"],
        render_kw=render_tech,
    )
    vite = BooleanField(
        label=TECH["vite"]["label"],
        default=TECH["vite"]["default"],
        render_kw=render_tech,
    )
    tailwind = BooleanField(
        label=TECH["tailwind"]["label"],
        default=TECH["tailwind"]["default"],
        render_kw=render_tech,
    )

    # info: Backend
    spring_boot = BooleanField(
        label=TECH["spring_boot"]["label"],
        default=TECH["spring_boot"]["default"],
        render_kw=render_tech,
    )
    spring = BooleanField(
        label=TECH["spring"]["label"],
        default=TECH["spring"]["default"],
        render_kw=render_tech,
    )
    nodejs = BooleanField(
        label=TECH["nodejs"]["label"],
        default=TECH["nodejs"]["default"],
        render_kw=render_tech,
    )
    express = BooleanField(
        label=TECH["express"]["label"],
        default=TECH["express"]["default"],
        render_kw=render_tech,
    )
    rest = BooleanField(
        label=TECH["rest"]["label"],
        default=TECH["rest"]["default"],
        render_kw=render_tech,
    )
    flask = BooleanField(
        label=TECH["flask"]["label"],
        default=TECH["flask"]["default"],
        render_kw=render_tech,
    )
    django = BooleanField(
        # ! not in form
        label=TECH["django"]["label"],
        default=TECH["django"]["default"],
        render_kw=render_tech,
    )
    graphql = BooleanField(
        # ! not in form
        label=TECH["graphql"]["label"],
        default=TECH["graphql"]["default"],
        render_kw=render_tech,
    )

    # info: Databases
    mongo = BooleanField(
        label=TECH["mongo"]["label"],
        default=TECH["mongo"]["default"],
        render_kw=render_tech,
    )
    postgres = BooleanField(
        label=TECH["postgres"]["label"],
        default=TECH["postgres"]["default"],
        render_kw=render_tech,
    )
    mysql = BooleanField(
        label=TECH["mysql"]["label"],
        default=TECH["mysql"]["default"],
        render_kw=render_tech,
    )
    oracle = BooleanField(
        label=TECH["oracle"]["label"],
        default=TECH["oracle"]["default"],
        render_kw=render_tech,
    )
    snowflake = BooleanField(
        label=TECH["snowflake"]["label"],
        default=TECH["snowflake"]["default"],
        render_kw=render_tech,
    )

    # info: Deployment
    aws = BooleanField(
        label=TECH["aws"]["label"],
        default=TECH["aws"]["default"],
        render_kw=render_tech,
    )
    azure = BooleanField(
        label=TECH["azure"]["label"],
        default=TECH["azure"]["default"],
        render_kw=render_tech,
    )
    gcp = BooleanField(
        label=TECH["gcp"]["label"],
        default=TECH["gcp"]["default"],
        render_kw=render_tech,
    )
    kubernetes = BooleanField(
        label=TECH["kubernetes"]["label"],
        default=TECH["kubernetes"]["default"],
        render_kw=render_tech,
    )
    docker = BooleanField(
        label=TECH["docker"]["label"],
        default=TECH["docker"]["default"],
        render_kw=render_tech,
    )

    # info: Management
    git = BooleanField(label=TECH["git"]["label"], default=TECH["git"]["default"])
    git_actions = BooleanField(
        label=TECH["git_actions"]["label"], default=TECH["git_actions"]["default"]
    )
    linux = BooleanField(label=TECH["linux"]["label"], default=TECH["linux"]["default"])
    maven = BooleanField(label=TECH["maven"]["label"], default=TECH["maven"]["default"])
    gradle = BooleanField(
        label=TECH["gradle"]["label"], default=TECH["gradle"]["default"]
    )
    jenkins = BooleanField(
        # ! not in form
        label=TECH["jenkins"]["label"],
        default=TECH["jenkins"]["default"],
    )
    # info: Testing
    junit = BooleanField(label=TECH["junit"]["label"], default=TECH["junit"]["default"])
    jest = BooleanField(label=TECH["jest"]["label"], default=TECH["jest"]["default"])
    pytest = BooleanField(
        # ! not in form
        label=TECH["pytest"]["label"],
        default=TECH["pytest"]["default"],
    )

    # info: Custom
    custom_tech_0 = StringField(
        label="Custom Tech 0",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )
    custom_tech_1 = StringField(
        label="Custom Tech 1",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )
    custom_tech_2 = StringField(
        label="Custom Tech 2",
        render_kw={"placeholder": "CUSTOM", "autocomplete": "on", "class": "tech"},
    )

    # MARK: ATTR
    attribute = SelectField(
        label="Attributes",
        default=3,
        choices=[
            (1, f"{ATTRIBUTES[1]['label'].upper()} - {ATTRIBUTES[1]['personal']}"),
            (2, f"{ATTRIBUTES[2]['label'].upper()} - {ATTRIBUTES[2]['personal']}"),
            (3, f"{ATTRIBUTES[3]['label'].upper()} - {ATTRIBUTES[3]['personal']}"),
            (4, f"{ATTRIBUTES[4]['label'].upper()} - {ATTRIBUTES[4]['personal']}"),
            (5, f"{ATTRIBUTES[5]['label'].upper()} - {ATTRIBUTES[5]['personal']}"),
            (6, f"{ATTRIBUTES[6]['label'].upper()} - {ATTRIBUTES[6]['personal']}"),
            (7, f"{ATTRIBUTES[7]['label'].upper()} - {ATTRIBUTES[7]['personal']}"),
            (8, f"{ATTRIBUTES[8]['label'].upper()} - {ATTRIBUTES[8]['personal']}"),
            (9, f"{ATTRIBUTES[9]['label'].upper()} - {ATTRIBUTES[9]['personal']}"),
            (10, f"{ATTRIBUTES[10]['label'].upper()} - {ATTRIBUTES[10]['personal']}"),
        ],
        validators=[DataRequired()],
    )

    # MARK: SUBMIT
    submit = SubmitField(name="submit", id="submit", render_kw={"value": "execute"})
    keep_docx = BooleanField(label=".docx", default=0)
