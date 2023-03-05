import json
from app.blueprints.main.dao.post_dao import PostDAO


class TestPostDAO:
    def test_get_all_posts_test(self, prepare_posts):
        post_dao = PostDAO(json.loads(prepare_posts))
        post_dao.json_posts_to_posts()
        assert 3 == len(post_dao.get_all_posts())

    def test_get_posts_by_user(self, prepare_posts):
        post_dao = PostDAO(json.loads(prepare_posts))
        post_dao.json_posts_to_posts()
        posts = post_dao.get_posts_by_user("user-1")
        assert 1 == len(posts)
        assert "content-1" == posts[0].content

    def test_search_for_post(self, prepare_posts):
        post_dao = PostDAO(json.loads(prepare_posts))
        post_dao.json_posts_to_posts()
        posts = post_dao.search_for_post("content")
        assert 3 == len(posts)

    def test_get_post_by_pk(self, prepare_posts):
        post_dao = PostDAO(json.loads(prepare_posts))
        post_dao.json_posts_to_posts()
        post = post_dao.get_post_by_pk(2)
        assert "content-2" == post.content
