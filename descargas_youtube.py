import yt_dlp as youtube_dl  # Usamos yt-dlp en lugar de youtube_dl

def descargar_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Función de descarga correcta

# aqui se agrega la URL del video
url = "https://hd.m0vie.org/es/loading?id=1252309&amp;title=P%C3%ADdeme%20lo%20que%20quieras"

# aqui hago la Llamada a la función
descargar_video(url)
