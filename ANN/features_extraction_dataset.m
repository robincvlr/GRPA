%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Extraction des features audio par Robin CAVALIERI et Guillaume CHANTREL 
%Automne 2017
%Classification parole / musique
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%CONSTANTES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc;
%Changez votre chemin pour appliquer de nouveaux changements
folder_parole = 'C:\Users\cavr2302\Documents\GitHub\FormationIA\Split_parole';
dirParole = dir(folder_parole);
%Changez votre chemin pour appliquer de nouveaux changements 
folder_musique = 'C:\Users\cavr2302\Documents\GitHub\FormationIA\Split_music';
dirMusique = dir(folder_musique);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%VARIABLES
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nBins = 99;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%TRAITEMENT DE LA PAROLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%pour la parole la classe est notée 0
base_parole = [];
for i=3:length(dirParole)
    filename= fullfile(folder_parole,dirParole(i).name);
    disp(filename);
    [signal,fs] = audioread(filename);
    tt = signal(:,1);
    X = hist(tt,nBins);
    Y = horzcat(X, 0); %ajout de l'emprunte de la classe
    base_parole = vertcat(base_parole, Y);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%TRAITEMENT DE LA MUSIQUE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%pour la musique la classe est notée 1
base_musique = [];
for i=3:length(dirMusique)
    filename= fullfile(folder_musique,dirMusique(i).name);
    disp(filename);
    [signal,fs] = audioread(filename);
    tt = signal(:,1);
    X = hist(tt,nBins);
    Y = horzcat(X, 1); %ajout de l'emprunte de la classe
    base_musique = vertcat(base_musique, Y);
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%EXPORTATION DES BASES VERS UN FICHIER D'APPRENTISSAGE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
base_complete = vertcat(base_parole, base_musique);
base_complete = base_complete(randperm(size(base_complete,1)),:);
csvwrite('base_features.csv',base_complete);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%AFFICHAGE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
hold on
figure(1)
plot(signal);
histogram(signal);
title("appartenance des amplitudes : Enregistrement vocal")
xlabel("Amplitude (V)")
ylabel("nombre d'occurencs")
%figure(2)
%plot(signal2);
%histogram(signal2);
%title("appartenance des amplitudes : Enregistrement vocal")
%xlabel("Amplitude (V)")
%ylabel("nombre d'occurencs")
%hold off
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
