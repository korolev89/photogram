from ..models.Comment import Comment


class CommentDAO:
    def __init__(self, comments_json):
        self.comments_json = comments_json
        self.comments = []

    def json_comments_to_comments(self):
        comments = []
        for comment in self.comments_json:
            comments.append(Comment(
                comment["post_id"],
                comment["commenter_name"],
                comment["comment"],
                comment["pk"]
            ))

        self.comments = comments

    def get_post_comments(self, post_id):
        comments = []
        for comment in self.comments:
            if comment.post_id == post_id:
                comments.append(comment)
        return comments
