from strategy.action_strategy import ActionStrategy
from components.status_updater import StatusUpdater

class StatusUpdateStrategy(ActionStrategy):
    def __init__(self, status_updater: StatusUpdater):
        self.status_updater = status_updater
    
    def execute(self):
        self.status_updater.update_status("away")