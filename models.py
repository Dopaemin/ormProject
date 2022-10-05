from flask_sqlalchemy import SQLAlchemy

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