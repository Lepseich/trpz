from download_service import download_file, get_uploaded_files, delete_file
from status_service import update_status
from task_service import schedule_task
from macros import record_macro, execute_macro

class MainController:
    def __init__(self):
       
        self.download_service = download_file
        self.status_service = update_status
        self.task_service = schedule_task
        self.macro_service = (record_macro, execute_macro)

    def handle_file_upload(self, file_path):
        """Обробка завантаження файлів"""
        self.download_service(file_path)
        print(f"File {file_path} uploaded successfully.")
        
    def show_uploaded_files(self):
        """Отримання списку завантажених файлів"""
        files = get_uploaded_files()
        print("Uploaded files:", files)
        
    def remove_file(self, filename):
        """Видалення файлів"""
        delete_file(filename)
        print(f"File {filename} deleted successfully.")
        
    def update_user_status(self, status):
        """Оновлення статусу"""
        self.status_service(status)
        print(f"Status updated to {status}.")
        
    def schedule_new_task(self, task_time):
        """Запланувати нове завдання"""
        self.task_service(task_time)
        print(f"Task scheduled at {task_time}.")
        
    def record_new_macro(self, macro_actions):
        """Запис макроса"""
        self.macro_service[0](macro_actions)
        print(f"Macro recorded with actions: {macro_actions}.")
        
    def execute_macro(self, macro_name):
        """Виконання макроса"""
        self.macro_service[1](macro_name)
        print(f"Macro {macro_name} executed.")
    
if __name__ == "__main__":

    controller = MainController()


    controller.handle_file_upload("example_file.txt")
    controller.show_uploaded_files()
    controller.remove_file("example_file.txt")
    controller.update_user_status("Available")
    controller.schedule_new_task("2025-01-20 09:00:00")
    controller.record_new_macro(["Ctrl+S", "Ctrl+P"])
    controller.execute_macro("auto_save_macro")
