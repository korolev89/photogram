from flask import Blueprint, render_template, request
from .dao.post_dao import PostDAO
from .dao.comment_dao import CommentDAO
from .functions import load_data_from_json

POSTS_PATH = "data/posts.json"
COMMENTS_PATH = "data/comments.json"

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

posts_json = load_data_from_json(POSTS_PATH)
comments_json = load_data_from_json(COMMENTS_PATH)

post_dao = PostDAO(posts_json)
post_dao.json_posts_to_posts()

comment_dao = CommentDAO(comments_json)
comment_dao.json_comments_to_comments()


@main_blueprint.route("/")
def main_page():
    return render_template("index.html", posts=post_dao.posts)


@main_blueprint.route("/post/<int:pk>")
def get_post_by_pk(pk):
    post = post_dao.get_post_by_pk(pk)
    comments = comment_dao.get_post_comments(pk)
    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route("/search")
def search_for_posts():
    query = request.args["query"]
    posts = post_dao.search_for_post(query)
    return render_template("search.html", posts=posts, posts_count=len(posts))


@main_blueprint.route("/user/<user_name>")
def get_posts_by_user(user_name):
    posts = post_dao.get_posts_by_user(user_name)
    return render_template("user_feed.html", posts=posts)

