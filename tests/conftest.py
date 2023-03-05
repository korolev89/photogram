import pytest


@pytest.fixture()
def prepare_posts():
    return '[{"poster_name":"user-1","poster_avatar":"ava-1","pic":"pic-1","content":"content-1","views_count":111,"likes_count":110,"pk":1},{"poster_name":"user-2","poster_avatar":"ava-2","pic":"pic-2","content":"content-2","views_count":222,"likes_count":220,"pk":2},{"poster_name":"user-3","poster_avatar":"ava-3","pic":"pic-3","content":"content-3","views_count":333,"likes_count":330,"pk":3}]'
