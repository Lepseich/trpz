from command import UpdateStatusCommand, DownloadFileCommand, ExecuteScriptCommand
from invoker import Invoker
from receiver import FileDownloader, StatusUpdater, ScriptExecutor

# Створюємо об'єкти отримувачів
file_downloader = FileDownloader()
status_updater = StatusUpdater()
script_executor = ScriptExecutor()

# Створюємо конкретні команди
update_status_command = UpdateStatusCommand(status_updater, "Away")
download_file_command = DownloadFileCommand(file_downloader, "http://example.com/file")
execute_script_command = ExecuteScriptCommand(script_executor, "run_task.sh")

# Створюємо інвокера та додаємо команди
invoker = Invoker()
invoker.add_command(update_status_command)
invoker.add_command(download_file_command)
invoker.add_command(execute_script_command)

# Виконуємо всі команди
invoker.execute_commands()
