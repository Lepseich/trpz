import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import schedule
from telegram import Bot
import threading
import time
import asyncio

class TaskSchedulerTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()


        self.token = '7910813623:AAFoh7qg8-0L4QtW1yheGOfIVZp2z2g68Sk'
        self.chat_id = '549924354'

    def create_widgets(self):
        ttk.Label(self.frame, text="Планувальник задач", font=("Arial", 14)).pack(pady=10)

        # Поле для вибору файлу
        ttk.Label(self.frame, text="Виберіть файл для відправки:").pack(pady=5)
        self.entry_file_path = ttk.Entry(self.frame, width=50)
        self.entry_file_path.pack(pady=5)
        ttk.Button(self.frame, text="Обрати файл", command=self.select_file).pack(pady=5)


        ttk.Label(self.frame, text="Введіть дату й час у форматі YYYY-MM-DD HH:MM:SS:").pack(pady=5)
        self.entry_datetime = ttk.Entry(self.frame, width=50)
        self.entry_datetime.pack(pady=5)


        ttk.Button(self.frame, text="Додати задачу", command=self.schedule_file_sending).pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Виберіть файл для відправки")
        if file_path:
            self.entry_file_path.delete(0, tk.END)
            self.entry_file_path.insert(0, file_path)

    async def send_file_to_telegram(self, file_path):
        try:
            print(f"Намагаємося відправити файл {file_path}")  # Логування
            bot = Bot(token=self.token)
            with open(file_path, 'rb') as file:
                await bot.send_document(chat_id=self.chat_id, document=file)
            messagebox.showinfo("Успіх", f"Файл {file_path} відправлено в Telegram!")
        except Exception as e:
            print(f"Помилка при відправці файлу: {e}")  # Логування помилок
            messagebox.showerror("Помилка", f"Не вдалося відправити файл: {e}")

    def schedule_file_sending(self):
        file_path = self.entry_file_path.get()
        date_time_str = self.entry_datetime.get()


        if not file_path or not date_time_str:
            messagebox.showerror("Помилка", "Заповніть усі поля!")
            return


        try:
            scheduled_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Помилка", "Неправильний формат дати й часу! Використовуйте YYYY-MM-DD HH:MM:SS.")
            return


        schedule.every().day.at(scheduled_time.strftime("%H:%M:%S")).do(
            self.schedule_task, file_path
        )
        messagebox.showinfo("Успіх", f"Задачу заплановано на {date_time_str}!")


        threading.Thread(target=self.run_scheduler, daemon=True).start()

    def schedule_task(self, file_path):

        asyncio.run(self.send_file_to_telegram(file_path))

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            print("Перевірка задач...")
            time.sleep(1)
