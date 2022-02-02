import cv2 as cv
import os 
import glob 
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cropped = gray[x:x+w, y:y+h]
    return cropped

img_dir = "data" 
# Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path)
data = []

for f1 in files: 
    img = cv.imread(f1)
    crop= face_detect(img)
    data.append(crop)

os.chdir('data_process') # data save directory
for i, name in enumerate(data):
    filename = 'image' + str(i) +'.jpg'