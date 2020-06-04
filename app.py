from flask import Flask, request, redirect, render_template
from models import db, connect_db, Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def course_redirect():
    """redirect to course_index"""
    return redirect("/courses")

@app.route("/courses")
def course_index():
    """ Show all courses """

    courses = Course.query.all()
    return render_template("course_index.html", courses=courses)


@app.route("/courses", methods=["POST"])
def course_create():
    """ Handle form submit """

    title = request.form.get("title")
    description = request.form.get("description")
    new_course = Course(title=title, description=description)
    db.session.add(new_course)
    db.session.commit()

    return redirect("/courses")


@app.route("/courses/new")
def course_new():
    """ Show form for adding a course. """

    return render_template("course_new.html")
