from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import bp


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)


db.init_app(app)
app.register_blueprint(bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)