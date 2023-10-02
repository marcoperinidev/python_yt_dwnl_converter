from pytube import YouTube
import os

while True:
    url = input("Inserisci l'URL di YouTube: ")

    try:
        video = YouTube(url)
        break
    except Exception as e:
        print("URL non valido, riprova.")

print('Title:', video.title)
print('Downloading...')
out_path = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(out_path)
os.rename(out_path, new_name[0] + '.mp3')
print('Done!')

