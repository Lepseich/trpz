from abc import ABC, abstractmethod

class AutomationFactory(ABC):
    """Інтерфейс фабрики автоматизації."""

    @abstractmethod
    def create_file_automation(self):
        pass

    @abstractmethod
    def create_status_automation(self):
        pass

    @abstractmethod
    def create_task_scheduler(self):
        pass