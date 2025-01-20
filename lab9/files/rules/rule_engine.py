class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self):
        for rule in self.rules:
            if rule["condition"]:
                rule["action"]()
