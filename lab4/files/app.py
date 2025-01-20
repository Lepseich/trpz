import tkinter as tk
from tkinter import ttk
from youtube_tab import YouTubeMonitorTab
from macros_tab import MacrosTab
from task_scheduler_tab import TaskSchedulerTab


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Automation Tool")
        self.root.geometry("800x600")
        self.create_tabs()

    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)


        youtube_tab = YouTubeMonitorTab(tab_control)
        tab_control.add(youtube_tab.frame, text="YouTube Monitor")

        macros_tab = MacrosTab(tab_control)
        tab_control.add(macros_tab.frame, text="Macros")

        scheduler_tab = TaskSchedulerTab(tab_control)
        tab_control.add(scheduler_tab.frame, text="Task Scheduler")

        tab_control.pack(expand=1, fill="both")

    def run(self):
        self.root.mainloop()
