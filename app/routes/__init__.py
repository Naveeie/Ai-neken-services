from flask import Blueprint, request, jsonify
from face_recogize import FaceRecognition
from text_to_speech import TextToSpeech
from database import mycursor
from .response import success
from face_encoding import FaceEncoding

import sqlite3
routes = Blueprint('routes', __name__)

sqliteconnection = sqlite3.connect('aineken')

@routes.get('/face')
def faceRecognition():
    name = FaceRecognition()
    print(name)
    return success(name)

@routes.get('/encode')
def faceEncoding():
    FaceEncoding()

@routes.post('/text-speech')
def textSpeech():
    body = request.get_json()
    return TextToSpeech(body)

@routes.get('/health-check')
def index():
    return success('Server is running')

@routes.get('/allUserEvents')
def allUserEvents():
    mycursor.execute('select * from user_events')
    result = mycursor.fetchall()
    return jsonify({"data":result})

@routes.get('/allUsers')
def allUsers():
    mycursor.execute('select * from user')
    result = mycursor.fetchall()
    return jsonify({"data":result})

@routes.get('/getSingleUser/<int:Number>')
def getSingleUser(Number):
    mycursor.execute("SELECT * FROM user WHERE user_uuid = '%d'" % Number)
    result = mycursor.fetchone()
    return jsonify({"data":result})

@routes.get('/getSingleUserEvent/<int:Number>')
def getSingleUserEvent(Number):
    mycursor.execute("SELECT * FROM user_events WHERE user_event_uuid = '%d'" % Number)
    result = mycursor.fetchone()
    return jsonify({"data":result})
