from abc import ABC, abstractmethod

class TaskScheduler(ABC):
    """Абстрактний клас для планувальника завдань."""

    @abstractmethod
    def schedule_task(self):
        pass

class TorrentSchedulerAction(TaskScheduler):
    """Клас для планування торрент-завдань."""

    def schedule_task(self):
        print("Роздача торрентів запланована на 5 ранку.")

class TaskSchedulerFactory:
    """Фабрика для створення планувальника завдань."""

    def create_task_scheduler(self):
        return TorrentSchedulerAction()