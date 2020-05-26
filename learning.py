import os
import face_recognition as fd
from PIL import Image

#Return the encodings of her face
def Known_Pics():

    #Move to the location of the pictures
    os.chdir("F:\Best Bud\Sad\memories")

    #Load the face to be recognized
    image=fd.load_image_file("Screenshot_1.png")
    knowm_face_encodings=fd.face_encodings(image)
    img=Image.fromarray(image)
    img.show()
    print(len(knowm_face_encodings))
    return knowm_face_encodings[1]

known_pic_encodings=Known_Pics()

l=[]
#Search her face with the dataset
def Unknown_Pics():
    os.chdir("F:\Best Bud\pics")
    for pic in os.listdir():
        print(pic)
        image=fd.load_image_file(pic)
        unknown_face_encodings=fd.face_encodings(image)
        for i in unknown_face_encodings:
            results=fd.compare_faces([known_pic_encodings],i)
            if results[0]==True:
                img=Image.fromarray(image)
                img.show()
                break
        #        break
Unknown_Pics()
