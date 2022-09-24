from database import mycursor
from flask import jsonify
def FetchAllUserEvents():
    mycursor.execute('select * from user_events')
    result = mycursor.fetchall()
    return jsonify({"data":result})

def FetchAllUsers():
    mycursor.execute('select * from user')
    result = mycursor.fetchall()
    return jsonify({"data":result})