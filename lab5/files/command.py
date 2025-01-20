class Command:
    """Інтерфейс команди."""
    def execute(self):
        pass

class RecordMacroCommand(Command):
    """Команда для запису макросу."""
    def execute(self):
        print("Запис макросу розпочато.")

class StopRecordingCommand(Command):
    """Команда для зупинки запису макросу."""
    def execute(self):
        print("Запис макросу зупинено.")

class PlayMacroCommand(Command):
    """Команда для відтворення макросу."""
    def execute(self):
        print("Відтворення макросу.")

class MacroController:
    """Клас, що управляє командами."""
    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

if __name__ == "__main__":
    controller = MacroController()

    controller.add_command(RecordMacroCommand())
    controller.add_command(StopRecordingCommand())
    controller.add_command(PlayMacroCommand())

    controller.execute_commands()
