from abc import ABC, abstractmethod

class StatusAutomation(ABC):
    """Абстрактний клас для автоматизації статусів."""

    @abstractmethod
    def set_status(self):
        pass

class SetSkypeStatusAction(StatusAutomation):
    """Клас для встановлення статусу в Skype."""

    def set_status(self):
        print("Статус у Skype змінено на 'Відсутній'.")

class StatusAutomationFactory:
    """Фабрика для створення автоматизації статусів."""

    def create_status_automation(self):
        return SetSkypeStatusAction()