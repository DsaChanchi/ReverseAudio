from pydub import AudioSegment

# Keyboard Audio
print("Give Song to reverse:")
audio = input()

song = AudioSegment.from_mp3(audio+".mp3")

# song is not modified
backwards = song.reverse()

backwards.export(audio+"backwards.mp3", format="mp3")