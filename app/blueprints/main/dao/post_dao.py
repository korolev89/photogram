from ..models.Post import Post


class PostDAO:
    def __init__(self, posts_json):
        self.posts_json = posts_json
        self.posts = []

    def json_posts_to_posts(self):
        posts = []
        for post in self.posts_json:
            posts.append(Post(
                post["poster_name"],
                post["poster_avatar"],
                post["pic"],
                post["content"],
                post["views_count"],
                post["likes_count"],
                post["pk"]
            ))

        self.posts = posts

    def get_all_posts(self):
        return self.posts

    def get_posts_by_user(self, user_name):
        posts = []
        for post in self.posts:
            if post.poster_name.lower() == user_name.lower():
                posts.append(post)
        return posts

    def search_for_post(self, query):
        posts = []
        for post in self.posts:
            if query.lower() in post.content.lower():
                posts.append(post)
        return posts

    def get_post_by_pk(self, pk):
        for post in self.posts:
            if post.pk == pk:
                return post
