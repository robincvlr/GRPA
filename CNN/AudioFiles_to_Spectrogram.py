##############Import librairie
import wave
import pylab as pb
import numpy as np


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
    pb.savefig('spect/' +name + '.png')

#############Fonction main
if __name__ == '__main__':
    #Boucle de traitement des audios
    i = 1
    while i < 11 :
        
       # Filename of the wav file
       # wav_file_parole = 'sons_parole/Split_parole/Parole (' + str(i) + ').wav' 
       
       # Filename of the wav file
        #wav_file_parole = 'sons_musique\Split_music\Musique (' + str(i) + ').wav' 
        wav_file_parole = 'audio/Split/audio (' + str(i) + ').wav' 
       
       # Filename of the wav file
       #wav_file_parole = 'prediction_music/prediction (' + str(i) + ').wav'
      
        #name_png = 'spectrogram_parole_' + str(i)
        name_png = 'spectrogram_1' + str(i)
        
        graph_spectrogram(wav_file_parole, name_png)
        
        i = i+1
        