class RuleManager:
    def create_rule(self, trigger, action):
        print(f"Rule created: WHEN '{trigger}' THEN '{action}'")

    def execute_rules(self):
        print("Executing all rules...")


class MacroRecorder:
    def record_macro(self, name, actions):
        print(f"Macro '{name}' recorded with actions: {actions}")

    def play_macro(self, name):
        print(f"Playing macro '{name}'")


class TasksScheduler:
    def schedule_task(self, task_name, time):
        print(f"Task '{task_name}' scheduled for {time}")

    def execute_tasks(self):
        print("Executing all scheduled tasks...")


class MainFacade:
    def __init__(self):
        self.rule_manager = RuleManager()
        self.macro_recorder = MacroRecorder()
        self.task_scheduler = TasksScheduler()

    def add_rule(self, trigger, action):
        self.rule_manager.create_rule(trigger, action)

    def record_macro(self, name, actions):
        self.macro_recorder.record_macro(name, actions)

    def schedule_task(self, task_name, time):
        self.task_scheduler.schedule_task(task_name, time)

    def execute_all(self):
        print("\n--- Executing All Automated Actions ---")
        self.rule_manager.execute_rules()
        self.task_scheduler.execute_tasks()


if __name__ == "__main__":
    app = MainFacade()

    app.add_rule("New episode released", "Download the episode")

    app.record_macro("LoginWorkflow", ["Open browser", "Navigate to login page", "Enter credentials"])

    app.schedule_task("Share torrents", "05:00 AM")

    app.execute_all()
