# app/routes/student.py
from flask import Blueprint, request, jsonify
from app.models.student import Student
from app.utils.database import db
from app.utils.response_utils import success_response, error_response

student_bp = Blueprint('student', __name__, url_prefix='/api/student')

# CREATE a new student
@student_bp.route('/', methods=['POST'])
def create_student():
    try:
        data = request.get_json()
        new_student = Student(
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            amount_due=data.get('amount_due'),
        )
        db.session.add(new_student)
        db.session.commit()
        return success_response(message='New student created successfully', data=new_student.to_dict())
    except Exception as e:
        print(e)
        return error_response(str(e))

# READ all students
@student_bp.route('/', methods=['GET'])
def read_students():
    try:
        students = Student.query.all()
        return success_response(message='All students fetched successfully', data=[student.to_dict() for student in students])
    except Exception as e:
        print(e)
        return error_response(str(e))

# READ a single student by ID
@student_bp.route('/<student_id>', methods=['GET'])
def read_student(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return error_response('Student not found')
        return success_response(message='Student fetched successfully', data=student.to_dict())
    except Exception as e:
        print(e)
        return error_response(str(e))

# UPDATE a student by ID
@student_bp.route('/<student_id>', methods=['PUT'])
def update_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        data = request.get_json()
        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.date_of_birth = data.get('date_of_birth', student.date_of_birth)
        student.amount_due = data.get('amount_due', student.amount_due)
        db.session.commit()
        return success_response(message='Student updated successfully', data=student.to_dict())
    except Exception as e:
        print(e)
        return error_response(str(e))

# DELETE a student by ID
@student_bp.route('/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return success_response(message='Student deleted successfully')
    except Exception as e:
        print(e)
        return error_response(str(e))