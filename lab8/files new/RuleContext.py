class RuleContext:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        print(f"Setting variable: {name} = {value}")
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name, None)