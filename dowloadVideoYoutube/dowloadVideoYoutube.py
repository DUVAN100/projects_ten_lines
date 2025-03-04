import yt_dlp

def download_video(video_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s' 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

download_video('https://youtu.be/5hlW5RKYxQk?si=0Dn6otLuUhiMZTQ3')
