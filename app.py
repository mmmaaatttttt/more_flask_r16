from flask import Flask, request, redirect, render_template
from models import db, connect_db, Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def course_index():
    """ Show all courses """

    courses = Course.query.all()
    return render_template("course_index.html", courses=courses)