from flask import Blueprint, jsonify, render_template

from ui.controller.cover_letter_controller import create_cover_letter
from ui.view.cover_letter_view import CoverLetterForm
from ui.utils import copy_to_clipboard
from ui.view.result_view import Result

bp = Blueprint(name="routes", import_name=__name__)


@bp.route(rule="/", methods=["GET", "POST"])
def cover_letter():
    form = CoverLetterForm()
    result = Result()

    if form.validate_on_submit():
        try:
            cover_letter_content = create_cover_letter(data=form.data)
            result.content = cover_letter_content
        except Exception as e:
            result.content = f"{e}"
            result.status = f"error: {e}"
            return render_template("pages/cover_letter.html", form=form, result=result)
        else:
            result.status = "success"
            result.content = cover_letter_content
            print(result.content)
            return render_template(
                template_name_or_list="pages/cover_letter.html",
                form=form,
                result=result,
            )

    # ! clipboard not working
    # if result.is_submitted():
    #     copy_to_clipboard(result.content)
    #     print(result.content)
    #     return result.content

    return render_template(
        template_name_or_list="pages/cover_letter.html", form=form, result=result
    )


@bp.route(rule="/json")
def json(data):
    return jsonify(data)
