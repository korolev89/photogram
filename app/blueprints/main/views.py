import json
from flask import Blueprint, render_template, request, abort
from .dao.post_dao import PostDAO
from .dao.comment_dao import CommentDAO
from .functions import load_data_from_json

POSTS_PATH = "data/posts.json"
COMMENTS_PATH = "data/comments.json"

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    posts_json = load_data_from_json(POSTS_PATH)
    if posts_json is None:
        abort(500)
    post_dao = PostDAO(posts_json)
    post_dao.json_posts_to_posts()
    return render_template("index.html", posts=post_dao.posts)


@main_blueprint.route("/post/<int:pk>")
def get_post_by_pk(pk):
    posts_json = load_data_from_json(POSTS_PATH)
    comments_json = load_data_from_json(COMMENTS_PATH)
    if posts_json is None or comments_json is None:
        abort(500)

    post_dao = PostDAO(posts_json)
    post_dao.json_posts_to_posts()
    post = post_dao.get_post_by_pk(pk)

    comment_dao = CommentDAO(comments_json)
    comment_dao.json_comments_to_comments()
    comments = comment_dao.get_post_comments(pk)

    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route("/search")
def search_for_posts():
    posts_json = load_data_from_json(POSTS_PATH)
    if posts_json is None:
        abort(500)
    post_dao = PostDAO(posts_json)
    post_dao.json_posts_to_posts()
    query = request.args["query"]
    if query:
        posts = post_dao.search_for_post(query)
        return render_template("search.html", posts=posts, posts_count=len(posts))
    else:
        abort(500)


@main_blueprint.route("/user/<user_name>")
def get_posts_by_user(user_name):
    posts_json = load_data_from_json(POSTS_PATH)
    if posts_json is None:
        abort(500)
    post_dao = PostDAO(posts_json)
    post_dao.json_posts_to_posts()
    posts = post_dao.get_posts_by_user(user_name)
    return render_template("user_feed.html", posts=posts)


@main_blueprint.errorhandler(500)
def error_handler(e):
    return f"<h1>{e}</h1>"
