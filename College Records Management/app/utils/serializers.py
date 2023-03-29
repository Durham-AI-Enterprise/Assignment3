# utils/serializers.py

def student_serializer(student):
    return {
        'student_id': student.student_id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'date_of_birth': student.date_of_birth,
        'amount_due': student.amount_due
    }