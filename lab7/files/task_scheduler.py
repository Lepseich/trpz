from datetime import datetime

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def schedule_task(self, task_name, time):
        task = {"name": task_name, "time": time}
        self.tasks.append(task)
        print(f"Task scheduled: {task_name} at {time}")

    def cancel_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Cancelled task: {removed_task['name']} scheduled at {removed_task['time']}")
        else:
            print("Invalid task ID.")

    def get_scheduled_tasks(self):
        return self.tasks

    def execute_scheduled_tasks(self):
        current_time = datetime.now().strftime("%H:%M")
        for task in self.tasks:
            if task["time"] == current_time:
                print(f"Executing task: {task['name']} scheduled at {task['time']}")