import pytest


@pytest.fixture()
def prepare_posts():
    return '[{"poster_name":"user-1","poster_avatar":"ava-1","pic":"pic-1","content":"content-1","views_count":111,"likes_count":110,"pk":1},{"poster_name":"user-2","poster_avatar":"ava-2","pic":"pic-2","content":"content-2","views_count":222,"likes_count":220,"pk":2},{"poster_name":"user-3","poster_avatar":"ava-3","pic":"pic-3","content":"content-3","views_count":333,"likes_count":330,"pk":3}]'


@pytest.fixture()
def prepare_comments():
    return '[{"post_id":1,"commenter_name":"user_1","comment":"Cool!","pk":1},{"post_id":2,"commenter_name":"user_2","comment":":)","pk":2},{"post_id":3,"commenter_name":"user_3","comment":"Wow!","pk":3},{"post_id":1,"commenter_name":"user_2","comment":"I like it!","pk":1},{"post_id":2,"commenter_name":"user_2","comment":":)","pk":2}]'
