from command import DownloadContentCommand, SetStatusCommand
from invoker import Invoker


if __name__ == "__main__":
    invoker = Invoker()
    
    # Додавання команд для автоматизації завдань
    download_command = DownloadContentCommand("фільм", "https://example.com/movie.mp4")
    set_status_command = SetStatusCommand("Skype", "Away")
    
    invoker.add_command(download_command)
    invoker.add_command(set_status_command)
    
    # Виконання всіх команд
    invoker.execute_commands()
