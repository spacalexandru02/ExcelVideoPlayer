from videoDownloader import VideoDownloader
from videoDecoder import VideoDecoder


class VideoPlayer:
    def __init__(self, url, resolution, folder):
        vd = VideoDownloader.VideoDownloader()
        vd.downloader(url, resolution, folder)
        videoDecoder = VideoDecoder.VideoDecoder()
        videoDecoder.analyze(folder + "youtube.mp4")
