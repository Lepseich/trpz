import unittest
from strategy import ConcreteStrategyDownload, ConcreteStrategySetStatus, ConcreteStrategySchedule, TaskContext

class TestStrategyPattern(unittest.TestCase):

    def setUp(self):
        """Ініціалізація перед кожним тестом"""
        self.download_strategy = ConcreteStrategyDownload()
        self.set_status_strategy = ConcreteStrategySetStatus()
        self.schedule_strategy = ConcreteStrategySchedule()
        
        self.task_details = {
            'url': 'https://example.com/video.mp4',
            'status': 'Офлайн',
            'messenger': 'Skype',
            'time': '05:00'
        }
        
        # Створюємо контекст
        self.context = TaskContext()

    def test_download_strategy(self):
        """Тестуємо стратегію завантаження"""
        self.context.set_strategy(self.download_strategy)
        result = self.context.execute_strategy(self.task_details)
        self.assertEqual(result, "Завантаження файлів за планом: https://example.com/video.mp4")

    def test_set_status_strategy(self):
        """Тестуємо стратегію встановлення статусу"""
        self.context.set_strategy(self.set_status_strategy)
        result = self.context.execute_strategy(self.task_details)
        self.assertEqual(result, "Встановлення статусу: Офлайн в Skype")

    def test_schedule_strategy(self):
        """Тестуємо стратегію запуску завдання за розкладом"""
        self.context.set_strategy(self.schedule_strategy)
        result = self.context.execute_strategy(self.task_details)
        self.assertEqual(result, "Запуск завдання за розкладом: 05:00")

    def test_strategy_change(self):
        """Тестуємо зміну стратегії"""
        self.context.set_strategy(self.download_strategy)
        download_result = self.context.execute_strategy(self.task_details)
        
        self.context.set_strategy(self.set_status_strategy)
        status_result = self.context.execute_strategy(self.task_details)
        
        self.assertNotEqual(download_result, status_result)
        self.assertEqual(download_result, "Завантаження файлів за планом: https://example.com/video.mp4")
        self.assertEqual(status_result, "Встановлення статусу: Офлайн в Skype")

    def test_no_strategy_set(self):
        """Тестуємо, що станеться, якщо не встановлено стратегію"""
        with self.assertRaises(ValueError):
            self.context.execute_strategy(self.task_details)

if __name__ == '__main__':
    unittest.main()
