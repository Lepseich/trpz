from automation_factory import AutomationFactory
from file_automation import FileAutomationFactory
from status_automation import StatusAutomationFactory
from task_scheduler import TaskSchedulerFactory

class FullAutomationFactory(AutomationFactory):


    def create_file_automation(self):
        return FileAutomationFactory().create_file_automation()

    def create_status_automation(self):
        return StatusAutomationFactory().create_status_automation()

    def create_task_scheduler(self):
        return TaskSchedulerFactory().create_task_scheduler()

if __name__ == "__main__":
    factory = FullAutomationFactory()

    # Завантаження файлів
    file_automation = factory.create_file_automation()
    file_automation.download()

    # Встановлення статусу
    status_automation = factory.create_status_automation()
    status_automation.set_status()

    # Планувальник завдань
    task_scheduler = factory.create_task_scheduler()
    task_scheduler.schedule_task()