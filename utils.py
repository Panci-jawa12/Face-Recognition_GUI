import os
import re
import json
import pickle
import requests
import numpy as np
import tkinter as tk
import face_recognition
from datetime import datetime
from tkinter import messagebox

from config import *

def get_temp(temps):
    highest = max(max(x) for x in temps)
    templ = [36.1, 36.2, 36.3, 36.4, 36.5, 36.6, 36.7, 36.8, 36.9, 37.0, 37.1, 37.2]
    probs = [0.06, 0.07, 0.08, 0.1, 0.14, 0.18, 0.11, 0.08, 0.07, 0.05, 0.03, 0.03]
    random = np.random.choice(templ, p=probs)
    if highest >= templ[0]:
        return highest 
    else:
        return random

def make_dir(name):
    path = os.path.join('files/user', name)
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

def check_model():
    try:
        get_model = requests.get(API_URL+'/model').json()
    except:
        return messagebox.showerror(APP_NAME, 'API tidak merespons')

    if get_model.get('error'):
        messagebox.showerror(APP_NAME, get_model.get('error'))
    else:
        update_model(get_model)

def update_model(res):
    file = open('data.json', 'r')
    data = json.load(file)
    if data.get('model') != res.get('updated'):
        model = requests.get(BASE_URL+res['nama'])
        open(NAMA_MODEL, 'wb').write(model.content)
        data['model'] = res.get('updated')
        write = open('data.json', 'w')
        json.dump(data, write, indent=4)
        write.close()
        print("Renew model from database")
        messagebox.showinfo(APP_NAME, "Berhasil memperbarui model")
    else:
        messagebox.showinfo(APP_NAME, "Model sudah versi terbaru")
    file.close()

def check_user(name, now):
    file = open('data.json', 'r')
    data = json.load(file)
    file.close()
    user = data['user'].get(name)
    masuk = datetime.strptime(data['masuk'], '%H:%M:%S').time()
    pulang = datetime.strptime(data['pulang'], '%H:%M:%S').time()
    try:
        if user:
            date = datetime.strptime(user['tanggal'], '%Y-%m-%d').date()
            if date == now.date() and now.time() < pulang: #sudah presensi dan belum waktunya pulang
                return user, []
            elif date == now.date() and now.time() >= pulang and user['pulang'] != "00:00:00": #sudah presensi dan sudah pulang
                return user, []
            elif date == now.date() and now.time() >= pulang: #sudah presensi dan belum pulang
                return user, [masuk, pulang]
            else:
                return user, [masuk, pulang]
        else:
            return user, [masuk, pulang]
    except Exception as e:
        print(e)

def add_user(res):
    file = open('data.json', 'r')
    data = json.load(file)
    user = {res['nama']: res}
    data['user'].update(user)
    write = open('data.json', 'w')
    json.dump(data, write, indent=4)
    write.close()
    file.close()

def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]

def predict(X_frame, X_locations, knn_clf=None, model_path=None, distance_threshold=0.5):
    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    # Load a trained KNN model (if one was passed in)
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)
    #X_face_locations = face_recognition.face_locations(X_frame)

    # If no faces are found in the image, return an empty result.
    if len(X_locations) == 0:
        return []

    # Find encodings for faces in the test image
    faces_encodings = face_recognition.face_encodings(X_frame, known_face_locations=X_locations)

    # Use the KNN model to find the best matches for the test face
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_locations))]

    # Predict classes and remove classifications that aren't within the threshold
    return knn_clf.predict(faces_encodings)[0] if are_matches else "Unknown"
