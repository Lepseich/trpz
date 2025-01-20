from components.file_downloader import FileDownloader
from components.status_updater import StatusUpdater
from components.script_executor import ScriptExecutor
from strategy.file_download_strategy import FileDownloadStrategy
from strategy.status_update_strategy import StatusUpdateStrategy
from strategy.script_execution_strategy import ScriptExecutionStrategy
from action import Action

if __name__ == "__main__":
    # Створення об'єктів компонентів
    file_downloader = FileDownloader()
    status_updater = StatusUpdater()
    script_executor = ScriptExecutor()

    # Створення стратегії
    file_download_strategy = FileDownloadStrategy(file_downloader)
    status_update_strategy = StatusUpdateStrategy(status_updater)
    script_execution_strategy = ScriptExecutionStrategy(script_executor)

    # Виконання дій
    file_download_action = Action(file_download_strategy)
    file_download_action.execute_action()

    status_update_action = Action(status_update_strategy)
    status_update_action.execute_action()

    script_execution_action = Action(script_execution_strategy)
    script_execution_action.execute_action()










