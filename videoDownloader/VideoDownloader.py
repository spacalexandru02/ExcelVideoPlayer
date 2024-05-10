from pytube import YouTube
import os
import ssl
class VideoDownloader:
    def __init__(self):
        pass

    def downloader(self, url, resolution, folder):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            yt = YouTube(url)
            print(url, resolution, folder)
            video = yt.streams.filter(res=resolution).first()
            if video:
                video_path = os.path.join(folder, "youtube" + ".mp4")
                print("video_path")
                if os.path.exists(video_path):
                    os.remove(video_path)

                video.download(output_path=folder, filename="youtube" + ".mp4")
                print("Video downloaded successfully!")
                print("Saved at:", video_path)
            else:
                print("Video with specified resolution not found.")
        except Exception as e:
            print("Error:", str(e))
