from models import db, connect_db, Course, Review, Instructor, TeachingAssignment
from app import app

db.create_all()

matt = Instructor(first_name="Matt", last_name="Lane")
nate = Instructor(first_name="Nate", last_name="Lipp")
tim = Instructor(first_name="Tim", last_name="Garcia")

db.session.add_all([matt, nate, tim])
db.session.commit()