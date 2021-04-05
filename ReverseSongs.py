from pydub import AudioSegment
import pathlib
import os
import errno

#ReverseAudio
#ListadoArchivos
directorioactual = pathlib.Path()
#Filtrado de canciones y generacion ver.reverse
for archivo in directorioactual.iterdir():
    if archivo.is_file() and archivo.name.endswith('.mp3'):
        song = AudioSegment.from_mp3(archivo.name)
        backwards = song.reverse()
        audio = (archivo.name[:-4])
        backwards.export(audio+"backwards.mp3", format="mp3")