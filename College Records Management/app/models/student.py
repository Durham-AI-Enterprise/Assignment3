# models/student.py
from app.utils.database import db
class Student(db.Model):
    __tablename__ = 'student_info'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    amount_due = db.Column(db.DECIMAL(10, 2), nullable=False, default=0.0)

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth.isoformat(),
            'amount_due': str(self.amount_due),
        }