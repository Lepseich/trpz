from strategy.action_strategy import ActionStrategy
from components.script_executor import ScriptExecutor

class ScriptExecutionStrategy(ActionStrategy):
    def __init__(self, script_executor: ScriptExecutor):
        self.script_executor = script_executor
    
    def execute(self):
        self.script_executor.execute_script("runBackup.sh")