# GRPA
Classification de la parole et de la musique par réseau de neurones

## Environnement

**Installez Anaconda**
   
**IDE :** Spyder
   
**Pour éxecuter un code sur Spyder :** sélectionnez le code puis, CTRL + Enter 

**Ajouter une bibliothèque dans Anaconda :** dans le prompt conda, saisissez : `conda install name_package`

## Utiliser le découpeur de fichier audio
**Dans le dossier Decoupage fichier audio, vous trouverez :**
  
 - **ffmpeg.exe**
   l'executable de la librairie ffmpeg utilisée dans le script bash, à laisser dans le même dossier que le script bash lors de son exécution
   
 - **cmd_cut.bat**
   le script bash permettant la découpe des fichiers audio

## Utiliser le CNN (approche par spectrogramme)
**Dans le dossier CNN, vous trouverez trois dossiers contenant des spectrogrammes :**

 - **training_set et test_set** :
   spectrogrammes des fichiers audios de la base de données permettant l'apprentissage du réseau
   
 - **prediction**
   spectrogrammes de la base de test pour évaluer les performances de l'algorithme

**Vous disposez également de trois Python** :
 
 - **AudioFiles_to_Spectrogram.py** 
   traitement des fichiers audio permettant la creation des spectrogrammes
   
 - **Spectrogram_Neurones.py**
   ce fichier python contient toute la structure du reséau de neurones CNN avec les différents paramètres définis ainsi que la partie permettant les tests de performance
   
 - **Application.py**
   une application graphique permettant de tester l'aglorithme de deep learning en y mettant un entrée un fichier audio coupé
   
 **Et enfin un dossier avec l'enregistrement d'un apprentissage pour pouvoir réaliser les tests :**
 
 - **Training**
 
## Utiliser le ANN (approche par features)
**Dans le dossier ANN, vous trouverez 2 fichiers MATLAB :**

 - **features_extraction_dataset.m** : 
   extraire le dataset - changer le PATH en constante et d'exécuter le code
   
 - **features_extraction_predictions.m** : 
   extraire les données à prédire - changer le PATH en constante et d'exécuter le code
   
**Vous trouverez 2 matrices (de dataset et  de prediction) au formal `.csv` :**

  Automatiquement générées par les scripts MATLAB 
  
 - **base_features.csv**
 
- **base_test_prediction_features.csv**

**Vous trouverez 1 fichier `.py` :**

 - **Features_Neurones.py** :
   Ce fichier contient les phases d'initialisation des données, d'architecture du réseau de neurones, d'apprentissage, de    sauvegarde d'apprentissage et de predictions.

**Et enfin un dossier avec l'enregistrement d'un apprentissage pour pouvoir réaliser les tests :**
 
 - **Training**
