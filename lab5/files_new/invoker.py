from command import Command
class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command) -> None:
        self._commands.append(command)

    def execute_commands(self) -> None:
        for command in self._commands:
            command.execute()
