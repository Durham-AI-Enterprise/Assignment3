# utils/response_utils.py

from flask import jsonify

def error_response(error=None):
    message = {
        'status': 404,
        'message': error if error else "Something went wrong, Please try again later",
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

def success_response(message, data=None):
    message = {
        'status': 200,
        'message': message,
    }
    if data is not None:
        message['data'] = data

    response = jsonify(message)
    response.status_code = 200
    return response
