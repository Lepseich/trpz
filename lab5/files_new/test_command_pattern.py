from command import DownloadContentCommand, SetStatusCommand
from invoker import Invoker

def test_command_pattern():
    # Ініціалізація Invoker
    invoker = Invoker()

    # Створення команд
    download_command = DownloadContentCommand("фільм", "https://example.com/movie.mp4")
    set_status_command = SetStatusCommand("Skype", "Away")

    # Додавання команд до Invoker
    invoker.add_command(download_command)
    invoker.add_command(set_status_command)

    # Виконання команд
    print("Виконання всіх команд:")
    invoker.execute_commands()

if __name__ == "__main__":
    test_command_pattern()
