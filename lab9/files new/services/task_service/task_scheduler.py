import time
from datetime import datetime

class Scheduler:
    def __init__(self, task_time, task_action):
        self.task_time = task_time
        self.task_action = task_action

    def schedule_task(self):
        while True:
            if datetime.now().hour == self.task_time:
                self.task_action()
                time.sleep(3600)  # Sleep for 1 hour
