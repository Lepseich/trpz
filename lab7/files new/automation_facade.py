from youtube_downloader import YouTubeDownloader
from macro_recorder import MacroRecorder
from task_scheduler import TaskScheduler

class AutomationFacade:
    def __init__(self):
        self.youtube_downloader = YouTubeDownloader()
        self.macro_recorder = MacroRecorder()
        self.task_scheduler = TaskScheduler()

    def download_and_schedule_video(self, channel_url, video_format, time):
        video_file = self.youtube_downloader.download_video(channel_url, video_format)
        self.task_scheduler.schedule_task(f"Роздача {video_file}", time)

    def record_and_execute_macro(self, macro_name):
        macro_file = self.macro_recorder.record_macro(macro_name)
        self.macro_recorder.execute_macro(macro_file)
