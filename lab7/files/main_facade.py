from rule_manager import RuleManager
from macro_recorder import MacroRecorder
from task_scheduler import TaskScheduler

class MainFacade:
    def __init__(self):
        self.rule_manager = RuleManager()
        self.macro_recorder = MacroRecorder()
        self.task_scheduler = TaskScheduler()

    def add_rule(self, trigger, action):
        self.rule_manager.create_rule(trigger, action)

    def record_macro(self, macro_name):
        self.macro_recorder.start_recording(macro_name)
        input("Press Enter to stop recording...")
        self.macro_recorder.stop_recording(macro_name)

    def schedule_task(self, task_name, time):
        self.task_scheduler.schedule_task(task_name, time)

    def execute_all(self):
        print("Executing all automation tasks...")
        self.rule_manager.execute_rules()
        self.task_scheduler.execute_scheduled_tasks()