import json
from app.blueprints.main.dao.comment_dao import CommentDAO


class TestCommentDAO:

    def test_get_post_comments(self, prepare_comments):
        comments_dao = CommentDAO(json.loads(prepare_comments))
        comments_dao.json_comments_to_comments()
        comments = comments_dao.get_post_comments(1)
        assert 2 == len(comments)
