import json
from json import JSONDecodeError
# import logging
from ..models.Post import Post


class PostDAO:
    def __init__(self, post_path):
        self.post_path = post_path

    def load_data_from_json(self):
        try:
            posts = []
            with open(self.post_path, "r", encoding="utf-8") as file:
                posts_raw = json.load(file)

                for post in posts_raw:
                    posts.append(Post(
                        post["poster_name"],
                        post["poster_avatar"],
                        post["pic"],
                        post["content"],
                        post["views_count"],
                        post["likes_count"],
                        post["pk"]
                    ))

                return posts

        except FileNotFoundError:
            # logging.basicConfig(filename="../logs/logs.text", level=logging.exception("File not found"))
            return "<h1>File not found</h1>"

        except JSONDecodeError:
            # logging.exception(filename="../logs/logs.text", level=logging.exception("JSON is corrupted"))
            return "<h1>File is corrupted</h1>"

    def get_all_posts(self):
        posts = self.load_data_from_json()
        return posts
