from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class DownloadContentCommand(Command):
    def __init__(self, content_type: str, content_url: str) -> None:
        self._content_type = content_type
        self._content_url = content_url

    def execute(self) -> None:
        print(f"Завантаження {self._content_type} з {self._content_url}...")

class SetStatusCommand(Command):
    def __init__(self, messenger: str, status: str) -> None:
        self._messenger = messenger
        self._status = status

    def execute(self) -> None:
        print(f"Встановлення статусу в {self._messenger} на {self._status}...")
