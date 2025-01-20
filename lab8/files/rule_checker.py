class RuleContext:
    def __init__(self):
        self.variables = {}

    def set_variable(self, key, value):
        self.variables[key] = value

    def get_variable(self, key):
        return self.variables.get(key, None)


class RuleParser:
    def parse(self, rule: str):
        """Парсить правило на дію і умову (якщо є)"""
        if "download" in rule:
            return "download"
        elif "status" in rule:
            return "status"
        return None


class RuleInterpreter:
    def __init__(self, context: RuleContext, parser: RuleParser):
        self.context = context
        self.parser = parser

    def interpret(self, rule: str):
        action = self.parser.parse(rule)
        if action == "download":
            self.execute_action("Downloading file...")
        elif action == "status":
            self.execute_action("Changing status...")
        else:
            print("Unknown rule")

    def execute_action(self, action: str):
        """Виконує дію на основі інтерпретованого правила"""
        print(action)


# Створюємо контекст і інтерпретатор
context = RuleContext()
parser = RuleParser()
interpreter = RuleInterpreter(context, parser)

# Встановлюємо змінні в контексті
context.set_variable("download_path", "/path/to/download")

# Інтерпретуємо правила
interpreter.interpret("download new movies")
interpreter.interpret("status update in skype")
