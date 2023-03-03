from flask import Blueprint, render_template
from .dao.post_dao import PostDAO

POST_PATH = "data/posts.json"

post_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
post_dao = PostDAO(POST_PATH)


@post_blueprint.route("/")
def all_posts_page():
    posts = post_dao.get_all_posts()
    return render_template("index.html", posts=posts)
