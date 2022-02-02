# import cv2 as cv
# import face_recognition
# import numpy as np

# face_locations=[]
# chanhyuk_image = face_recognition.load_image_file("data/img13.jpg")
# small_frame = cv.resize(chanhyuk_image, (0,0),fx=0.25, fy= 0.25)
# #convert image from BGR color to RGB color
# rgb_frame = small_frame[:,:, ::-1]

# face_locations = face_recognition.face_locations(rgb_frame)

# for (top, right, bottom, left) in face_locations:
#     top *=4
#     right *=4
#     bottom *=4
#     left *=4

#     cv.rectangle(chanhyuk_image, (left, top), (right, bottom), (0, 0, 255), 2)\

# cv.imshow('after', chanhyuk_image)
# cv.waitKey(0)

from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("data/chanhyuk.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()