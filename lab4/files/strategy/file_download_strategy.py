from strategy.action_strategy import ActionStrategy
from components.file_downloader import FileDownloader

class FileDownloadStrategy(ActionStrategy):
    def __init__(self, file_downloader: FileDownloader):
        self.file_downloader = file_downloader
    
    def execute(self):
        self.file_downloader.download_file("http://example.com/file")