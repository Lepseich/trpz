class RuleManager:
    def __init__(self):
        self.rules = []

    def create_rule(self, trigger, action):
        rule = {"trigger": trigger, "action": action}
        self.rules.append(rule)
        print(f"Rule added: IF {trigger} THEN {action}")

    def delete_rule(self, rule_id):
        if 0 <= rule_id < len(self.rules):
            removed_rule = self.rules.pop(rule_id)
            print(f"Deleted rule: IF {removed_rule['trigger']} THEN {removed_rule['action']}")
        else:
            print("Invalid rule ID.")

    def get_rules(self):
        return self.rules

    def execute_rules(self):
        for rule in self.rules:
            print(f"Executing rule: IF {rule['trigger']} THEN {rule['action']}")