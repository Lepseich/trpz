import time

class MacroRecorder:
    def __init__(self):
        self.actions = []

    def record_action(self, action_type, details):
        self.actions.append({"action": action_type, "details": details, "time": time.time()})

    def save_macro(self, filename):
        with open(filename, 'w') as f:
            for action in self.actions:
                f.write(f"{action}\n")
