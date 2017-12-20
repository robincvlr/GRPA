# Convolutional Neural Network 

# Part 1 - Building the CNN 

from keras.models import Sequential # Initialiser les couches du réseau de neurones 
from keras.layers import Convolution2D # Convolution 
from keras.layers import MaxPooling2D # Pooling step 
from keras.layers import Flatten # Convert Pool into vectors (connexions) 
from keras.layers import Dense # Add the fully connected layers 


# initialising the CNN 
classifier = Sequential()

# Step 1  - convolution 
# Paramètres de la matrice de détection, couleurs, taille, etc 
# 1 chanel for B&W 3 RGB
# 32 filters differents utiliser pour la convolution mettre plus si travail sur GPU
# 3x3 taille du filtre de convolution
# input_shape=(64, 64, 3) --» 3 arrays : RGB / 2 arrays BW, 64*64 RGB --» jusqu a 256 
classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2))) 

# Step 1  - convolution 
# Paramètres de la matrice de détection, couleurs, taille, etc 
classifier.add(Convolution2D(32, 3, 3, activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2))) 
 
# Step 3 - Flattening 
# Mettre en un seul vecteur a une dimension pour l entree dans les couches cachees 
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu')) 

# Output layer
classifier.add(Dense(output_dim = 1, activation = 'sigmoid')) 

# Compilation of the CNN 
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images 
from keras.preprocessing.image import ImageDataGenerator

# creation base plus grande avec rotation, ...
# ici pas de rotation ni de zoom autrement perte de donnees importante pour la classification 
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0,
        zoom_range=0,
        horizontal_flip=False)

test_datagen = ImageDataGenerator(rescale=1./255)

# 20/100 test_set  = 187/936
train_generator = train_datagen.flow_from_directory(
        'training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        'test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        train_generator,
        steps_per_epoch=500,
        epochs=2,
        validation_data=validation_generator,
        validation_steps=200)

#Save the learning 
#classifier.save('sauvegarde.tfl')

#serialise model to json
classifier_json = classifier.to_json()
with open('model_voice_music.json', "w") as json_file :
    json_file.write(classifier_json)
    
# serialize weights to HDF5
classifier.save_weights("model_voice_music.h5")
print("Classifier save on disk")



################## Test avec Load du model #######################


# Load json and create model
from keras.models import model_from_json
json_file = open('model_voice_music.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

#load weights into new model
loaded_model.load_weights('model_voice_music.h5')
print("Loaded model from disk")



############################ Making a prediction ##################

import numpy as np
from keras.preprocessing import image
import math as m

#################################prediction#########################
# Load the image with keras 
# arg : path / target_size same as the test_set

pre = np.zeros([118,2])
array = []

i = 1
while i < 119 :
    test_image = image.load_img('prediction/spectrogram ('+ str(i) +').png', target_size=(64, 64))
    
    
    # passer l'image en tableau
    test_image = image.img_to_array(test_image)
    
    #test method
    #mauvais format, il faut ajouter une dimension au test 
    test_image = np.expand_dims(test_image, axis = 0)
    loaded_model.predict(test_image)
    
    #Correspondance 
    result  = loaded_model.predict(test_image)
    
    result = result
    
    
    # 1 est une voix
    #t = train_generator.class_indices
    
    if result[0][0] > 0: 
        prediction='voice'
    else:
        prediction='music'
    
    print(i)
    pre[i - 1,0] = i
    pre[i - 1,1] = float(result)
    
    array.append(prediction)
    
    i = i + 1
    
nombre_music = array.count("music")
nombre_voix = array.count("voice")

erreur = (118 - (m.fabs(nombre_music-50) + m.fabs(nombre_voix-68))) *100 / 118

