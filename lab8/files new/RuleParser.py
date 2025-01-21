class RuleParser:
    def parse(self, rule_text):
        print(f"Parsing rule: {rule_text}")

        try:
            if "IF" in rule_text and "THEN" in rule_text:
                condition, action = rule_text.split(" THEN ")
                condition = condition.replace("IF ", "").strip()
                action = action.strip()
                return {"condition": condition, "action": action}
            else:
                raise ValueError("Invalid rule format. Use 'IF condition THEN action'.")
        except Exception as e:
            print(f"Error parsing rule: {e}")
            return {}

    def parse_condition(self, condition_text):
        print(f"Parsing condition: {condition_text}")

        return condition_text