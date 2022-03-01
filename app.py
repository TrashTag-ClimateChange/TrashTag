# Flask utils
import os

import re

import cv2

import time

import shutil

import zipfile

import urllib.request

import numpy as np

from PIL import Image

from os import listdir

from os.path import isfile, join

from random import randrange

import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template

from werkzeug.utils import secure_filename

#from flask_ngrok import run_with_ngrok

#from gevent import WSGIServer



model = load_model('model/debris.h5',compile=False)

print('Model loaded')

 

# Define a flask app

app = Flask(__name__)

#run_with_ngrok(app) 



def make_prediction(image_fp,model):

    im = cv2.imread(image_fp) # load image

    plt.imshow(im[:,:,[2,1,0]])

    img = image.load_img(image_fp, target_size = (180,180))

    img = image.img_to_array(img)



    image_array = img / 180. # scale the image

    img_batch = np.expand_dims(image_array, axis = 0)



    class_ = [ 'cardboard','glass', 'metal','paper','plastic', 'plasticbags', 'trash'] # possible output values

    predicted_value = class_[model.predict(img_batch).argmax()]

    true_value = re.search(r'(cardboard)|(glass)|(metal)|(paper)|(plastic)|(plasticbags)|(trash)', image_fp)[0]

    

    out = f"""Predicted debris Type: {predicted_value}\n

    True Debris Type: {true_value}\n

    Correct?: {predicted_value == true_value}"""

    return out

def classify_percentage(image_fp, model):
    start = time.time()
    out = classify_images(image_fp=image_fp, model=model)
    print(out)
    finish = str(round(time.time() - start, 5))
    
    im = cv2.imread(image_fp) # load image
    plt.imshow(im[:,:,[2, 1, 0]])

    percentage = f'''---
            Percent cardboard: {round(out[0] * 100, 2)}%)\n
            Percent glass: {round(out[1] * 100, 2)}%)\n
            Percent metal: {round(out[2] * 100, 2)}%)\n
            Percent paper: {round(out[0] * 100, 2)}%)\n
            Percent plastic: {round(out[1] * 100, 2)}%)\n
            Percent plastic bags: {round(out[1] * 100, 2)}%)\n
            Percent trash: {round(out[2] * 100, 2)}%)\n
            Time to Classify: {finish} seconds\n
            ---'''
    return percentage

def classify_images(image_fp, model):

    classes = [ 'cardboard','glass', 'metal','paper','plastic', 'plasticbags', 'trash']

    cardboard_count = 0

    glass_count = 0

    metal_count = 0

    paper_count = 0

    plastic_count = 0

    plasticbags_count = 0

    trash_count = 0

    img = cv2.imread(image_fp)

    img = cv2.resize(img,(1024,1024))

    im_dim = 180

    for r in range(0, img.shape[0], im_dim):

        for c in range(0, img.shape[1], im_dim):

            cropped_img = img[r:r + im_dim, c:c + im_dim, :]

            h, w, c = cropped_img.shape

            if h == im_dim and w == im_dim:

                classification = model_classify(cropped_img, model)

                if classification == classes[0]:

                    cardboard_count += 1

                elif classification == classes[1]:

                    glass_count += 1

                elif classification == classes[2]:

                    metal_count += 1

                elif classification == classes[3]:

                    paper_count += 1

                elif classification == classes[4]:

                    plastic_count += 1

                elif classification == classes[5]:

                    plasticbags_count += 1

                elif classification == classes[6]:

                    trash_count += 1

            else:

                continue

    total_count = cardboard_count + glass_count + metal_count + paper_count + plastic_count + plasticbags_count + trash_count

    proportion_array = [cardboard_count / total_count, glass_count / total_count, metal_count / total_count, paper_count / total_count, plastic_count / total_count, plasticbags_count / total_count, trash_count / total_count]
    print(proportion_array)
    return proportion_array



def model_classify(cropped_img, model):

    classes = [ 'cardboard','glass', 'metal','paper','plastic', 'plasticbags', 'trash']

    image_array = cropped_img / 255

    img_batch = np.expand_dims(image_array, axis=0)

    prediction_array = model.predict(img_batch)[0]

    first_idx = np.argmax(prediction_array)

    first_class = classes[first_idx]

    return first_class


@app.route('/')

def index():

    # Main page

    print('index root')

    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])

def upload():

    if request.method == 'POST':  

        # Get the file from post request

        f = request.files['file']

        # Save the file to ./uploads

        basepath = os.path.dirname(__file__)

        file_path = os.path.join(

            basepath, 'uploads', secure_filename(f.filename))

        f.save(file_path)

        # Make prediction

        preds = make_prediction(file_path, model)

        print(make_prediction(file_path, model))

        return preds

    return 'Please try with an image'

@app.route('/classify', methods=['GET','POST'])

def uploadfile():

    if request.method == 'POST':  

        # Get the file from post request

        f = request.files['file']

        # Save the file to ./uploads

        basepath = os.path.dirname(__file__)

        file_path = os.path.join(

            basepath, 'uploads', secure_filename(f.filename))

        f.save(file_path)

        # Make prediction

        start = time.time()

        preds = classify_percentage(file_path, model)

        return preds

    return 'Please try with an image'


if __name__ == '__main__':

    app.run(host='0.0.0.0',port='8080')


