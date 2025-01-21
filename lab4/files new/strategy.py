from abc import ABC, abstractmethod

# Загальний інтерфейс стратегій
class Strategy(ABC):
    @abstractmethod
    def execute(self, task_details):
        pass

# Конкретні стратегії для завдань автоматизації
class ConcreteStrategyDownload(Strategy):
    def execute(self, task_details):
        return f"Завантаження файлів за планом: {task_details['url']}"

class ConcreteStrategySetStatus(Strategy):
    def execute(self, task_details):
        return f"Встановлення статусу: {task_details['status']} в {task_details['messenger']}"

class ConcreteStrategySchedule(Strategy):
    def execute(self, task_details):
        return f"Запуск завдання за розкладом: {task_details['time']}"

# Контекст для виконання завдань
class TaskContext:
    def __init__(self, strategy: Strategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, task_details):
        if not self.strategy:
            raise ValueError("Стратегія не встановлена")
        return self.strategy.execute(task_details)

# Приклад роботи програми
class AutomationApp:
    def main(self):
        # 1. Створити контекст для завдання
        context = TaskContext(None)
        
        # 2. Вибір стратегії та передача деталей завдання
        task_details = {
            'url': 'https://example.com/video.mp4',
            'status': 'Офлайн',
            'messenger': 'Skype',
            'time': '05:00'
        }
        
        # Вибір стратегії
        action = input("Виберіть тип завдання (download/status/schedule): ").lower()
        
        if action == 'download':
            context.set_strategy(ConcreteStrategyDownload())
        elif action == 'status':
            context.set_strategy(ConcreteStrategySetStatus())
        elif action == 'schedule':
            context.set_strategy(ConcreteStrategySchedule())
        else:
            print("Невідома операція.")
            return
        
        # 3. Виконати завдання за допомогою стратегії
        return context.execute_strategy(task_details)
