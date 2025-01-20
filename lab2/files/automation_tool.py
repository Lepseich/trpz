class AutomationTool:
    def __init__(self):
        self.rules = []
        self.macros = []
        self.task_scheduler = TaskScheduler()

    def executeRule(self, rule):
        rule.execute()

    def scheduleTask(self, task):
        self.task_scheduler.scheduleAt(task)

    def addMacro(self, macro):
        self.macros.append(macro)

class Rule:
    def __init__(self):
        self.conditions = []
        self.tasks = []

    def execute(self):
        if all(condition.checkCondition() for condition in self.conditions):
            for task in self.tasks:
                task.execute()

    def addCondition(self, condition):
        self.conditions.append(condition)

    def addTask(self, task):
        self.tasks.append(task)

class Condition:
    def checkCondition(self):
        # Logic to check the condition
        return True

class Task:
    def schedule(self):
        pass

    def execute(self):
        pass

class FileDownloader(Task):
    def execute(self):
        print("Downloading file...")

class StatusUpdater(Task):
    def execute(self):
        print("Updating status...")

class ScriptExecutor(Task):
    def execute(self):
        print("Executing script...")

class Macro:
    def __init__(self):
        self.actions = []

    def recordAction(self, action):
        self.actions.append(action)

    def playback(self):
        for action in self.actions:
            action.execute()

class Action:
    def __init__(self, action_type):
        self.action_type = action_type

    def execute(self):
        print(f"Executing action: {self.action_type}")

class TaskScheduler:
    def scheduleAt(self, time):
        print(f"Scheduling task at {time}")

class IRepository:
    def save(self, item):
        pass

    def load(self, id):
        pass

class Repository(IRepository):
    def __init__(self):
        self.rules = []
        self.macros = []

    def save(self, item):
        if isinstance(item, Rule):
            self.rules.append(item)
        elif isinstance(item, Macro):
            self.macros.append(item)

    def load(self, id):
        if id < len(self.rules):
            return self.rules[id]
        elif id < len(self.macros):
            return self.macros[id]

class AbstractFactory:
    def createRule(self):
        raise NotImplementedError()

    def createTask(self):
        raise NotImplementedError()

class ConcreteFactory(AbstractFactory):
    def createRule(self):
        return Rule()

    def createTask(self):
        return Task()
