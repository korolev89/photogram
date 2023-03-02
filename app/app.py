from flask import Flask
from blueprints.main.views import main_blueprint

app = Flask(__name__, template_folder="/templates")

app.register_blueprint(main_blueprint)

app.run(debug=True)
