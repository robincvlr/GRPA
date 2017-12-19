###################################################################################################
# Artificial Neural Network
# Par Robin Cavalieri et Guillaume Chantrel
# Groupe de recherche sur la parole et l'audio 
# Automne 2017 
# Classifier la parole et la musique par extraction de features
###################################################################################################

###################################################################################################
# LIBRAIRIES UTILES
###################################################################################################
import numpy as np
import pandas as pd
import time
import csv
# Modelisation
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
# Réseau de neurones 
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
###################################################################################################

##########################################################################################
#TRAVAIL PRELIMINAIRE DE TRAITEMENT DES DONNEES D'APPRENTISSAGE
##########################################################################################
# Import du dataset : Features des différentes musiques 
# Dans le fichier 'features_extraction.m' création d'une matrice faisant office de données d'apprentissage
# Traitment de tous les fichiers et génération d'histogrammes pour chacun. 
# Obtention des différents pics spectraux
# Moyennage du nombre d'apparition de ces pics selon un certain nombre de BINS -» voir modifier nBins sous 'features_extraction.m'
# Ouverture de la base d'apprentissage
dataset = pd.read_csv('base_features.csv');
#récupération de la taille de la matrice dataset - l'indice de la classe est en derniere colonne
[nSizeX, nSizeY] = np.shape(dataset);
# Données d'entrée 
data = dataset.iloc[:, 0:nSizeY-1].values;
# Sortie associée 
target = dataset.iloc[:, nSizeY - 1].values;
# Splitting the dataset into the Training set and Test set
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.2, random_state = 0);
# Normalisation des données pré-apprentissage
sc = StandardScaler();
data_train = sc.fit_transform(data_train);
data_test = sc.transform(data_test);
##########################################################################################

##########################################################################################
#ARCHITECTURE DU RESEAU DE NEURONES par le biais de la librairie KERAS
#A N N 
##########################################################################################
#Initialising the ANN
classifier = Sequential();
#Adding the input layer and the first hidden layer
# output_dim = nb_entree + nb_sortie /2
# input_dim = 11 --> 11 variables independantes
# uniform --> initialise le poids des connections
# use the rectifier fonction en entrée et entre les differentes couches de neurones 
# (0 ou plusieurs valeurs possibles)

classifier.add(Dense(output_dim = nSizeY-1, init = 'uniform', activation = 'sigmoid', input_dim = nSizeY-1));

# Adding the second hidden layer
# output_dim = nb_entree + nb_sortie /2
# uniform --> initialise le poids des connections
# use the rectifier fonction en entrée et entre les differentes couches de neurones 
# (0 ou plusieurs valeurs possibles)
# Nombres input a initialisé que sur la premeiere couche

classifier.add(Dense(output_dim = nSizeY-1, init = 'uniform', activation = 'sigmoid'));
#classifier.add(Dense(output_dim = 30, init = 'uniform', activation = 'sigmoid'));

# Test avec ajout d'une seconde couche cachee
# Mauvais sur tests car propagation de l'erreur, alorithme plus long a execter, perte du gradient et risque de divergence 
# classifier.add(Dense(output_dim = nSizeY-1, init = 'uniform', activation = 'sigmoid'));

# Adding the output layer
# output layer --> 1 etat bianire
# Signal de sortie --> sigmoid activation (1 ou 0)
# Si plusieurs categories a plusieurs valeurs en sortie : output = nb valeurs 
# et activation = 'softmax'
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'));
##########################################################################################

##########################################################################################
#COMPILATION
##########################################################################################
# optimizer : algorithme choisi pour trouver le model (le plus puissant)
# adam --> Stochastic Gradient Descent
# loss : Si deux valeurs en sortie (binairie outcome) : binary_crossentropy
#        Si plus de deux valeurs : categorical_crossentropy
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']);
##########################################################################################

##########################################################################################
#TRAINING
##########################################################################################
# Fitting the ANN to the Training set
# data : matrice d'entrée d'apprentissage
# target : matrice de sortie d'apprentissage
# update the weights after each observation (Reinforcement Learning)
# update the weights after a batch of observations (Batch Learning) 
# In general: Larger batch sizes result in faster progress in training, 
# but don't always converge as fast. Smaller batch sizes train slower, 
# but can converge faster. It's definitely problem dependent.
tmps1=time.time()
classifier.fit(data_train, target_train, batch_size =1, epochs=1000);
tmps2=time.time()-tmps1

##########################################################################################

##########################################################################################
#TAUX DE REUSSITE A PARTIR DES DONNEES DE TEST
##########################################################################################
# Making the prediction and evaluating the model 
# Predicting the Test set results (En pourcentage)
data_pred = classifier.predict(data_test);
# Conversion en True ou False les predictions
# Si y_pred > 0.5 : True 
data_pred_binary = (data_pred > 0.5);
# Matrice de cout
cm = confusion_matrix(target_test, data_pred_binary);
good_prediction = cm[0, 0] + cm[1, 1]; #dire qu'une musique est musique et qu'un enregistrement vocal est un enreg. vocal
bad_prediction = cm[1, 0] + cm[0, 1]; #dire qu'une musique est enreg. vocal et qu'un enregistrement vocal est une musique
taux_succes = good_prediction * 100 / (good_prediction + bad_prediction);
##########################################################################################

##########################################################################################
#SAUVEGARDE DU TRAINING SET
##########################################################################################
#Le modèle est mis au format JSON 
classifier_json = classifier.to_json();
with open('Training/training_features.json',"w") as json_file : 
    json_file.write(classifier_json);
#Les poids sont mis en HDF5
classifier.save_weights("Training/training_features.h5");
##########################################################################################

##########################################################################################
##########################################################################################
#VOUS POUVEZ EXECUTER UNIQUEMENT CE CODE
########################################################################################## 
##########################################################################################
#LOAD DU TRAINING SET
##########################################################################################
json_file=open('Training/training_features.json','r');
loaded_model_json=json_file.read();
json_file.close();
loaded_model=model_from_json(loaded_model_json);
loaded_model.load_weights('Training/training_features.h5');
##########################################################################################

##########################################################################################
#REALISER DES PREDICTIONS
##########################################################################################
dataset_to_pred = pd.read_csv('base_test_prediction.csv', quoting=csv.QUOTE_NONE);
[xSizePred, ySizePred] = np.shape(dataset_to_pred);
data_to_pred = dataset_to_pred.iloc[:, 0: ySizePred].values;
predictions = classifier.predict(data_to_pred);

predictions_named = [];

for x in range(0, xSizePred-1):
    if predictions[x] > 0.5:
        predictions_named.append("Musique")
    else:
        predictions_named.append("Parole")
##########################################################################################