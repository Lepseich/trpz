from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WinCheckbox(Checkbox):
    def paint(self):
        return "Windows Checkbox Painted"

class MacCheckbox(Checkbox):
    def paint(self):
        return "Mac Checkbox Painted"
