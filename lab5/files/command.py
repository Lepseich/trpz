from abc import ABC, abstractmethod

# Базовий клас команди
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретна команда для оновлення статусу
class UpdateStatusCommand(Command):
    def __init__(self, status_updater, status):
        self.status_updater = status_updater
        self.status = status

    def execute(self):
        self.status_updater.updateStatus(self.status)

# Конкретна команда для завантаження файлів
class DownloadFileCommand(Command):
    def __init__(self, file_downloader, url):
        self.file_downloader = file_downloader
        self.url = url

    def execute(self):
        self.file_downloader.downloadFile(self.url)

# Конкретна команда для виконання скриптів
class ExecuteScriptCommand(Command):
    def __init__(self, script_executor, script):
        self.script_executor = script_executor
        self.script = script

    def execute(self):
        self.script_executor.executeScript(self.script)
