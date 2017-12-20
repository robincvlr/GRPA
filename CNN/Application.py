# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:25:25 2017

@author: chag2818
"""

##############Import librairie
import wave
import pylab as pb
import numpy as np
import time


#############Constante
#Fréquence d'échantillonage = 2 * fc Shanon
FE = 22050
#NFFT echantillonnage - length of the windowing segments
NFFT = 1024

#############Fonction get_Info du fichier audio
#Return les info de l'audio et sa duree
def get_wav_info(wav_file):
    #Ouverture du fichier en lecture
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = np.fromstring(frames, 'Int16')
    wav.close()
    #Return
    return sound_info

#############Fonction enregistrement du spectrogramme
def graph_spectrogram(wav_file, name):
    #Recupere les infos de  audio
    sound_info = get_wav_info(wav_file)
    pb.figure(num=None, figsize=(19, 12))
    pb.subplot(111)

    #Suppression des axes pour supprimer les parasites
    pb.axis('off')
    
    #Suppresion de la légende
    #pb.legend().set_visible(False)
    
    #Desine le spectrogramme d une partie de l audio
    pb.specgram(sound_info, NFFT=NFFT, Fs=FE, noverlap=1000, cmap='binary') #Noir et blanc
    
    #Enregistrement du spectrogramme
    #pb.savefig('training_set/Base_spect_parole/' +name + '.png')
    #pb.savefig('training_set/Base_spect_musique/' +name + '.png')
    pb.savefig(name)

#############Fonction main
if __name__ == '__main__':
    
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        
        T = tk.Text(root, height=10, width=80)
        T.pack()
        T.insert(tk.END,"Classification parole/musique \n")
        
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("wav files","*.wav"),("all files","*.*")))
        
        wav_file_parole = root.filename 
       
        #name_png = 'spectrogram_parole_' + str(i)
        name_png = 'spectrogram.png'
        graph_spectrogram(wav_file_parole, name_png)
        
        time.sleep(5) 
        
        ############################ Making a prediction ##################

        from keras.preprocessing import image
        from keras.models import model_from_json
        
        # Load json and create model
        json_file = open('Training/model_voice_music.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        
        #load weights into new model
        loaded_model.load_weights('Training/model_voice_music.h5')
        print("Loaded model from disk")

        prediction_image = image.load_img(name_png, target_size=(64, 64))
    
    
        # passer l'image en tableau
        prediction_image = image.img_to_array(prediction_image)
        
        #test method
        #mauvais format, il faut ajouter une dimension au test 
        prediction_image = np.expand_dims(prediction_image, axis = 0)
        loaded_model.predict(prediction_image)
        
        #Correspondance 
        result  = loaded_model.predict(prediction_image)
        
        # 1 est une voix
        #t = train_generator.class_indices
        
        if result[0][0] > 0: 
            prediction='voice'
        else:
            prediction='music'
        
        #champ_label = tk.Label(root, text= "Resultats de la prediction :" + prediction)
        T.insert(tk.END,"Resultats de la prediction :\n" + prediction + "\n")
        root.mainloop()
        
        
        
        
        
        
        
        
        