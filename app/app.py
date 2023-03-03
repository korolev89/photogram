from flask import Flask
from blueprints.main.views import main_blueprint
from blueprints.posts.views import post_blueprint

app = Flask(__name__, template_folder="/templates")

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint, url_prefix="/posts/")

if __name__ == "__main__":
    app.run(debug=True)
