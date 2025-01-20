from services.download_service.downloader import Downloader
from services.macros_service.macro_executor import MacroExecutor
from services.status_service.status_updater import StatusUpdater
from services.task_service.task_scheduler import Scheduler

def main():
    # Example task: Download a file
    downloader = Downloader("http://example.com/testfile", "/path/to/save")
    downloader.download()

    # Example task: Execute macro
    macro_executor = MacroExecutor("path/to/macro_file")
    macro_executor.execute_macro()

    # Example task: Update status
    status_updater = StatusUpdater("AA")
    status_updater.update_status()

    # Example task: Schedule task
    scheduler = Scheduler(5, lambda: print("Task executed"))
    scheduler.schedule_task()

if __name__ == "__main__":
    main()
