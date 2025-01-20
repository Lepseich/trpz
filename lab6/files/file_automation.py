from abc import ABC, abstractmethod

class FileAutomation(ABC):
    """Абстрактний клас для автоматизації завантаження файлів."""

    @abstractmethod
    def download(self):
        pass

class DownloadMovieAction(FileAutomation):
    """Клас для завантаження фільмів або серій."""

    def download(self):
        print("Завантаження нових серій фільму розпочато.")

class FileAutomationFactory:
    """Фабрика для створення автоматизації завантаження файлів."""

    def create_file_automation(self):
        return DownloadMovieAction()
