from abc import ABC, abstractmethod

class AutomationFactory(ABC):


    @abstractmethod
    def create_automation(self):
        pass

class FileAutomationFactory(AutomationFactory):


    def create_automation(self):
        return DownloadMovieAction()

class Automation(ABC):


    @abstractmethod
    def execute(self):
        pass

class DownloadMovieAction(Automation):

    def execute(self):
        return 

def run_automation(factory: AutomationFactory):

    automation = factory.create_automation()
    print(automation.execute())


factory = FileAutomationFactory()
run_automation(factory)
