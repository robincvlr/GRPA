::L'objectif de ce script est de découper les échantillons afin qu'ils
::aient une durée de 3s chacun - OBJ : apprentisage plus précis - limiter les erreurs 

::::::::::::::::::::::::::::::::::::::::Decoupe de la base d entrainement ::::::::::::::::::::::::::::::
::découpage des fichiers musicaux
::set i=0
::for %%X in (sons_musique/*.wav) do (
::echo Traitement de %%X... 
::echo valeur de i %i%...
::ffmpeg -ss 00:00:00.001 -i "sons_musique/%%X" -t 00:00:03.001 "sons_musique/Split_music/%%X"
::set /a i+=1)

::découpage des fichiers vocaux
::set /A i=0
::for %%Y in (sons_parole/*.wav) do (
::echo Traitement de %%Y...
::ffmpeg -ss 00:00:01.001 -t 00:00:04.001 -i "sons_parole/%%Y" -t 00:00:03.001 "sons_parole/Split_parole/%%Y"
::set /a i+=1)

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::::::Decoupe base de test:::::::::::::::::::::::::::::::::::::::::::::::
::Parcours les fichiers wav du dossier audio
set /A i=0
for %%X in (audio/*.wav) do (
::Affichage
echo Traitement de %%X...
::Decoupe du fichier X entre 50,001 et 53,001 et le place dans le sous dossier Split
ffmpeg -ss 00:00:50.001 -t 00:00:53.001 -i "audio/%%X" -t 00:00:03.001 "audio/Split/%%X"
set /a i+=1)


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::