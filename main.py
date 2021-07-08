from pytube import YouTube

link = input("Inserta el link del video: ")
yt = YouTube(f'{link}')

videos = yt.streams
video = list(enumerate(videos))
for i in video:
    print(i)
dn_option = int(input("En qué formato? (nº lista arriba) "))

print(" ")
print(f"Video: {yt.title}")

print("Es este tu vídeo? (y or n) ")
answer = input().lower

if answer() == "y":
    print("De acuerdo") 
    dn_video = videos[dn_option]
    dn_video.download()
    print(f"{yt.title} descargado correctamente!")

if answer() == "n":
    print("Pues pon el link bien -_-")