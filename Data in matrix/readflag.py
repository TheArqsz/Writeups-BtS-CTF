import os
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import cv2
import random
import numpy as np
from PIL import Image

#W razie problemów z błędem:
#Activation function not found: softmax_v2
#Odkomentować

##_TF_ACTIVATIONS_V2 = {
##    'softmax_v2': 'softmax',
##}

def sortKeyFunc(s):
    return int(os.path.basename(s)[:-5])



#Jeśli QR code będzie nieczytelny zmienić na >5
N_EPOCHS = 3

#pobieranie zbioru testowego i treningowego
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#Ładowanie jsona z formatem sieci
try:
    json_file = open('model.json', 'r')
except:
    print('\n======================')
    print('NO PREVIOUSLY SAVED MODEL! \n CREATING NEW ONE!')
    print('======================')

    #Kod zajebany

    # Reshaping the array to 4-dims so that it can work with the Keras API
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
    # Making sure that the values are float so that we can get decimal points after division
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # Normalizing the RGB codes by dividing it to the max RGB value.
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print('Number of images in x_train', x_train.shape[0])
    print('Number of images in x_test', x_test.shape[0])

    # Creating a Sequential Model and adding the layers
    model = Sequential()
    model.add(Conv2D(28, kernel_size=(3,3), input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten()) # Flattening the 2D arrays for fully connected layers
    model.add(Dense(128, activation=tf.nn.relu))
    model.add(Dropout(0.2))
    model.add(Dense(128, activation=tf.nn.sigmoid))
    model.add(Dropout(0.2))
    model.add(Dense(10,activation=tf.nn.sigmoid)) #Był tf.nn.softmax ale powodował problemy

    model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])
    
    model.fit(x=x_train,y=y_train, epochs=N_EPOCHS, shuffle=True)
    #model.evaluate(x_test, y_test)

    #Zapisywanie modelu sieci jako json
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
        
    #Zapisywanie wag w pliku '.h5'
    model.save_weights("model.h5")
    print("Saved model to disk")

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

#Kompilowanie modelu i wag wczytanych z pliku
loaded_model.compile(optimizer='adam', 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])

finalimage = []
counter = 0

#TA KOMENDA NIE PRZEKAZUJE PLIKOW W KOLEJNOSCI ALFABETYCZNEJ
#WYMAGA SORTOWANIA
folder = sorted(os.listdir('pliki'), key=sortKeyFunc)

for filename in folder:
    file = cv2.imread('pliki/{}'.format(filename), 0)
    prediction = loaded_model.predict(file.reshape(1, 28,28, 1))
    prediction = int(prediction.argmax())
    
    #w razie przekłamania w rozpoznaniu strzelamy:
    #Niepoprawnych rozpoznań jest na tyle mało, że nie wpływają w żadnym stopniu na kod
    # (pojedyncze pixele, gdzie jeden kwadracik kodu QR to co najmniej 10x10 (przynajmniej
    # w tym formacie flagi)
    if prediction > 1:
        prediction = int(random.randint(0,1))

    #print(prediction)
    finalimage.append(prediction)
    counter += 1
    if counter%10000 == 0:
        print('+10 000')


print(len(finalimage))
finalimage = np.array(finalimage)


finalimage = np.reshape(finalimage, (102,102)).astype('bool')
finalimage = Image.fromarray(finalimage)
plt.imshow(finalimage)
plt.show()
finalimage.show()
