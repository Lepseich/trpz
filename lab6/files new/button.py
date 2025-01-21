from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinButton(Button):
    def paint(self):
        return "Windows Button Painted"

class MacButton(Button):
    def paint(self):
        return "Mac Button Painted"
