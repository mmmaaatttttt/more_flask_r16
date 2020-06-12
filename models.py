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
    instructors = db.relationship("Instructor", secondary="teaching_assignments")

    def instructors_str(self):
        """ Get string representation of all instructors."""

        return ", ".join([instructor.get_full_name() for instructor in self.instructors])


class Review(db.Model):
    """ Review model """

    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    course = db.relationship("Course")


class Instructor(db.Model):
    """ Instructor model """

    __tablename__ = "instructors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    courses = db.relationship("Course", secondary="teaching_assignments")

    def get_full_name(self):
        """ Get instructor's full name"""

        return f"{self.first_name} {self.last_name}"


class TeachingAssignment(db.Model):
    """ Join table for Instructor and Course. """

    __tablename__ = "teaching_assignments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey("instructors.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
