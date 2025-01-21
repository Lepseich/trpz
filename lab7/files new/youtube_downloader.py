class YouTubeDownloader:
    def download_video(self, channel_url, video_format="mp4"):
        print(f"Завантаження відео з каналу {channel_url} у форматі {video_format}...")
        return f"video.{video_format}"
