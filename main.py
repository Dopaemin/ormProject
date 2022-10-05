from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy()


class Teammember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)
    email = db.Column(db.String)


def connect_create_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return db

connect_create_db(app)

with app.app_context():
    me = Teammember(username='me', email='me@e.de')
    db.session.add(me)
    db.session.commit()

    # User me suchen
    user = Teammember.query.filter_by(username='me').first()
    # User ändern
    user.name = 'Mertens'
    db.session.delete(user)
    db.session.commit()

