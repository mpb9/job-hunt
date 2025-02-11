from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
)


# ! clipboard not woorking
class Result(FlaskForm):
    copy = SubmitField(name="copy", id="copy", label="Copy to Clipboard")
    status = None
    content = None
