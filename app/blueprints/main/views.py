from flask import Blueprint, redirect

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return redirect("/posts/", 302)
