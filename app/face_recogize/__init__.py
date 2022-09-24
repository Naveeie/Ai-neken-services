import face_recognition
import cv2
import numpy as np
import csv
import pickle
from datetime import datetime 

def FaceRecognition():
    video_capture = cv2.VideoCapture(0)
    data = pickle.loads(open('face_enc', "rb").read())
    face_location = []
    facce_encodings = []
    s=True
    while True:
        _,frame = video_capture.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.50,fy=0.50)
        rgb_small_frame = small_frame[:,:,::-1]
        if s:
            face_location = face_recognition.face_locations(rgb_small_frame)
            facce_encodings = face_recognition.face_encodings(rgb_small_frame,face_location)
            for face_encodinds in facce_encodings:
                matches = face_recognition.compare_faces(data["encodings"],face_encodinds)
                name = 'Unknown'
                face_distance = face_recognition.face_distance(data["encodings"],face_encodinds)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = data["names"][best_match_index]
                    return name
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
