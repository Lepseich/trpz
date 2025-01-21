import unittest
from factory import WinFactory, MacFactory
from button import WinButton, MacButton
from checkbox import WinCheckbox, MacCheckbox
from application import Application


class TestAbstractFactory(unittest.TestCase):
    
    def test_win_factory(self):
        factory = WinFactory()
        app = Application(factory)
        app.create_ui()
        
        # Перевіряємо, чи створена кнопка є WinButton
        self.assertIsInstance(app.button, WinButton)
        self.assertEqual(app.button.paint(), "Windows Button Painted")
        
        # Перевіряємо, чи створений чекбокс є WinCheckbox
        self.assertIsInstance(app.checkbox, WinCheckbox)
        self.assertEqual(app.checkbox.paint(), "Windows Checkbox Painted")
    
    def test_mac_factory(self):
        factory = MacFactory()
        app = Application(factory)
        app.create_ui()
        
        # Перевіряємо, чи створена кнопка є MacButton
        self.assertIsInstance(app.button, MacButton)
        self.assertEqual(app.button.paint(), "Mac Button Painted")
        
        # Перевіряємо, чи створений чекбокс є MacCheckbox
        self.assertIsInstance(app.checkbox, MacCheckbox)
        self.assertEqual(app.checkbox.paint(), "Mac Checkbox Painted")

    def test_factory_integration(self):
        # Тестуємо обидві фабрики разом для порівняння
        win_factory = WinFactory()
        mac_factory = MacFactory()

        # Створюємо застосунок для Windows
        app_win = Application(win_factory)
        app_win.create_ui()
        self.assertIsInstance(app_win.button, WinButton)
        self.assertEqual(app_win.button.paint(), "Windows Button Painted")
        self.assertIsInstance(app_win.checkbox, WinCheckbox)
        self.assertEqual(app_win.checkbox.paint(), "Windows Checkbox Painted")

        # Створюємо застосунок для Mac
        app_mac = Application(mac_factory)
        app_mac.create_ui()
        self.assertIsInstance(app_mac.button, MacButton)
        self.assertEqual(app_mac.button.paint(), "Mac Button Painted")
        self.assertIsInstance(app_mac.checkbox, MacCheckbox)
        self.assertEqual(app_mac.checkbox.paint(), "Mac Checkbox Painted")


if __name__ == "__main__":
    unittest.main()
