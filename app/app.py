from flask import Flask
from blueprints.main.views import main_blueprint

app = Flask(__name__, template_folder="/templates")

app.register_blueprint(main_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return f"<h1>{e}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
