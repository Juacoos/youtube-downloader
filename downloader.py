import pytube

print("SISTEMA DE DESCARGA DE YOUTUBE")
print("------------------------------")

url = input("Inserte URL de YouTube: ")
yt = pytube.YouTube(url)

def descarga():
  print("Elija la opción: ")
  print("Opción 1: resolución más alta")
  print("Opción 2: resolución más baja")
  print("Opción 3: solo audio MP3")
  opt = input("Opción: ")
  if(opt == "1"):
    print("Descargando")
    video1 = yt.streams.get_highest_resolution()
    video1.download(filename="Video.mp4")
  elif(opt == "2"):
    print("Descargando")
    video2 = yt.streams.get_lowest_resolution()
    video2.download(filename="Video.mp4")
  elif(opt == "3"):
    print("Descargando")
    video3 = yt.streams.get_audio_only()
    video3.download(filename="Video.mp3")
  else:
    print("Opción incorrecta")
    print("-----------------")
    descarga()

descarga()
print("Descarga finalizada")

