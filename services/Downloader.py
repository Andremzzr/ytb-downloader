from yt_dlp import YoutubeDL
import os

class Downloader():

    def __init__(self, download_path=None):
        self.download_path = os.path.join(os.getcwd(), download_path or 'downloads' )

        os.makedirs(self.download_path, exist_ok=True)

        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [
                {  
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3', 
                    'preferredquality': '0',  
                },
                {
                    'key': 'FFmpegMetadata'  
                }
            ],
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
        }
    
    def download_video_as_mp3(self, url, download_path = None):
        if download_path:
            self.ydl_opts['outtmpl'] = os.path.join(download_path, '%(title)s.%(ext)s')
            self.download_path = download_path

        info = ydl.extract_info(url, download=False)
        file_path = os.path.join(download_path or self.download_path, f"{info['title']}.mp3")
        
        with YoutubeDL(self.ydl_opts) as ydl:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"Deleted existing file: {file_path}")
                except PermissionError:
                    print(f"Error: Unable to delete {file_path}. File may be in use.")
                    return

            ydl.download([url])

