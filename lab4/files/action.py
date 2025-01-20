class Action:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_action(self):
        self.strategy.execute()