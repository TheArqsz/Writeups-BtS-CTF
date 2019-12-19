import qrcode
import numpy as np
import tensorflow as tf
from PIL import Image
from skimage.transform import resize
import cv2
from matplotlib import pyplot as plt
import os

#Opis:
'''
Aby odczytać zawartość przekonwertuj dane binarne do obrazka
'''
#Pobieranie danych testowych i treningowych
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

ZEROS = []
ONES = []

#Wrzucanie randomowych obrazków jedynek i zer
for i in range(len(x_train)):
    if y_train[i] == 0:
        ZEROS.append(x_train[i])
    if y_train[i] == 1:
        ONES.append(x_train[i])
    else:
        pass



#Tworzenie QrCode
img = qrcode.make('bts-ctf{SKYNET_WILL__TAKE_CONTROL_OVER_THE_WORLD__SOON}')

#Pomniejszenie obrazka
width, height = img.size
img = img.resize((int(width/4), int(height/4)))

#Zapis
img.save('qrcode.png')
img = np.array(img)

HEIGHT, WIDTH = img.shape[0], img.shape[1]

imgName = 0
test = []

#Tworzenie folderu na obrazki
os.makedirs('pliki')

#Zamiana pixela [0,1] na obrazek i zapis
for i in range(HEIGHT):
    for j in range(WIDTH):
        imgName += 1
        #print(img[i][j])
        img[i][j] = int(img[i][j])
        if img[i][j] == 0:
            temp = ZEROS[np.random.randint(len(ZEROS))]
            temp = Image.fromarray(temp)
            temp.save('pliki/{}.jpeg'.format(imgName))
        elif img[i][j] == 1:
            temp = ONES[np.random.randint(len(ONES))]
            temp = Image.fromarray(temp)
            temp.save('pliki/{}.jpeg'.format(imgName))
        test.append(bool(img[i][j]))
    