from flask import Blueprint, render_template
from .dao.post_dao import PostDAO
from .functions import load_data_from_json

POSTS_PATH = "data/posts.json"
COMMENTS_PATH = "data/comments.json"

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

posts_json = load_data_from_json(POSTS_PATH)
comments_json = load_data_from_json(COMMENTS_PATH)

post_dao = PostDAO(posts_json)
post_dao.json_posts_to_posts()


@main_blueprint.route("/")
def main_page():
    return render_template("index.html", posts=post_dao.posts)


@main_blueprint.route("/post/<int:pk>")
def get_post_by_pk(pk):
    post = post_dao.get_post_by_pk(pk)
    return render_template("post.html", post=post)

# def get_posts_by_user(user_name):
#     pass
#
#
# def get_comments_by_post_id(post_id):
#     pass
#
#
# def search_for_posts(query):
#     pass
