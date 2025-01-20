from RuleContext import RuleContext
from RuleParser import RuleParser

class RuleInterpreter:
    def __init__(self):
        self.context = RuleContext()
        self.parser = RuleParser()

    def interpret(self, rule_text):
        print(f"Interpreting rule: {rule_text}")
        parsed_rule = self.parser.parse(rule_text)
        condition = parsed_rule.get("condition")
        action = parsed_rule.get("action")

        if self.evaluate_condition(condition):
            self.execute_action(action)
        else:
            print("Condition not met. Rule will not execute.")

    def evaluate_condition(self, condition):
        print(f"Evaluating condition: {condition}")

        try:
            result = eval(condition, {}, self.context.variables)
            print(f"Condition result: {result}")
            return result
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return False

    def execute_action(self, action):
        print(f"Executing action: {action}")

        if action.startswith("download "):
            file_name = action.replace("download ", "")
            print(f"Downloading file: {file_name}")
        elif action.startswith("set_status "):
            status = action.replace("set_status ", "")
            print(f"Setting status to: {status}")
        else:
            print(f"Unknown action: {action}")