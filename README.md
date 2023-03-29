## CRUD Operations for Student Records
This project implements a basic CRUD (Create, Read, Update, Delete) API for managing student data. The API is built using Flask, a popular Python web framework, and SQLAlchemy, a powerful ORM (Object Relational Mapper) library.

### Getting Started
- Clone the repository to your local machine.
- Start the Flask application.

### Endpoints

#### Create a new student
- Endpoint: POST /students
- Request Body: JSON object containing the student's information (first name, last name, date of birth, and amount due)
- Response: JSON object containing the new student's information (including an automatically generated ID)

#### Read all students
- Endpoint: GET /students
- Response: JSON array containing all student objects

#### Read a single student by ID
- Endpoint: GET /students/{id}
- Response: JSON object containing the student's information

#### Update a student by ID
- Endpoint: PUT /students/{id}
- Request Body: JSON object containing the updated student information
- Response: JSON object containing the updated student's information

#### Delete a student by ID
- Endpoint: DELETE /students/{id}
- Response: JSON object confirming that the student has been deleted

### Conclusion
This API provides a basic implementation for managing student data using Flask and SQLAlchemy. It can be extended to add more features and functionality as required.