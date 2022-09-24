from flask import jsonify

def success(data = [], message = ''):
    return jsonify(
        data = data,
        status = 200,
        success = True,
        message = message
    )

def error(status = '500', message = ''):
    return jsonify(
        status = status,
        success = False,
        message = message
    )