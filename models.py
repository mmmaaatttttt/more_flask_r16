from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Course(db.Model):
    """ Course model """

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)

    reviews = db.relationship("Review")


class Review(db.Model):
    """ Review model """

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    course = db.relationship("Course")
