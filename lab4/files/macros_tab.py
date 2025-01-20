import tkinter as tk
from tkinter import ttk
import threading
import time
import keyboard
import pyautogui
import json
import os
import mouse


class MacrosTab:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.create_widgets()
        self.recording = False
        self.macro = []
        self.stop_event = threading.Event()


        self.mouse_state = {
            "left": False,
            "right": False
        }

    def create_widgets(self):
        ttk.Label(self.frame, text="Запис і виконання макросів", font=("Arial", 14)).pack(pady=10)
        ttk.Button(self.frame, text="Записати макрос", command=self.record_macro).pack(pady=5)
        ttk.Button(self.frame, text="Зупинити запис", command=self.stop_recording).pack(pady=5)
        ttk.Button(self.frame, text="Відтворити макрос", command=self.play_macro).pack(pady=5)

    def record_macro(self):
        print("Функція запису викликана!")
        if self.recording:
            print("Запис вже триває!")
            return

        self.macro = []
        self.recording = True
        self.stop_event.clear()
        self.record_thread = threading.Thread(target=self.record_actions)
        self.record_thread.daemon = True
        self.record_thread.start()

    def stop_recording(self):
        if self.recording:
            print("Запис зупинено!")
            self.recording = False
            self.stop_event.set()
            self.save_macro()
        else:
            print("Запис не активний.")

    def record_keyboard_actions(self):
        while self.recording:
            try:

                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    print(f"Захоплено натискання клавіші: {event.name}")
                    self.macro.append({"type": "keyboard", "key": event.name, "time": time.time()})
            except Exception as e:
                print(f"Неочікувана помилка з клавіатурою: {e}")

    def record_mouse_actions(self):
        previous_position = None
        while self.recording:
            try:

                if mouse.is_pressed(button="left"):
                    if not self.mouse_state["left"]:
                        print("Натискання лівої кнопки миші")
                        self.macro.append(
                            {"type": "mouse_click", "button": "left", "action": "down", "time": time.time()})
                        self.mouse_state["left"] = True


                if mouse.is_pressed(button="right"):
                    if not self.mouse_state["right"]:
                        print("Натискання правої кнопки миші")
                        self.macro.append(
                            {"type": "mouse_click", "button": "right", "action": "down", "time": time.time()})
                        self.mouse_state["right"] = True


                if not mouse.is_pressed(button="left") and self.mouse_state["left"]:
                    self.macro.append({"type": "mouse_click", "button": "left", "action": "up", "time": time.time()})
                    print("Відпускання лівої кнопки миші")
                    self.mouse_state["left"] = False


                if not mouse.is_pressed(button="right") and self.mouse_state["right"]:
                    self.macro.append({"type": "mouse_click", "button": "right", "action": "up", "time": time.time()})
                    print("Відпускання правої кнопки миші")
                    self.mouse_state["right"] = False


                x, y = pyautogui.position()
                if previous_position != (x, y):
                    print(f"Запис миші на координатах x: {x}, y: {y}")
                    self.macro.append({"type": "mouse_move", "x": x, "y": y, "time": time.time()})
                    previous_position = (x, y)

                time.sleep(0.1)
            except Exception as e:
                print(f"Неочікувана помилка з мишою: {e}")

    def record_actions(self):

        keyboard_thread = threading.Thread(target=self.record_keyboard_actions)
        mouse_thread = threading.Thread(target=self.record_mouse_actions)

        keyboard_thread.daemon = True
        mouse_thread.daemon = True

        keyboard_thread.start()
        mouse_thread.start()


        while self.recording:
            time.sleep(0.1)


        print(f"Запис завершено. Кількість подій: {len(self.macro)}")
        self.save_macro()

    def save_macro(self):
        if not self.macro:
            print("Немає подій для збереження.")
            return

        file_path = "macro.json"
        try:
            with open(file_path, "w") as f:
                json.dump(self.macro, f)
            print(f"Макрос успішно збережено в {file_path}")
        except Exception as e:
            print(f"Помилка при збереженні макросу: {e}")

    def play_macro(self):
        file_path = "macro.json"
        if not os.path.exists(file_path):
            print("Немає записаного макросу!")
            return

        try:
            with open(file_path, "r") as f:
                macro = json.load(f)
            print(f"Макрос завантажено. Кількість подій: {len(macro)}")

            if len(macro) == 0:
                print("Макрос порожній!")
                return

            previous_time = time.time()
            for action in macro:
                event_time = action["time"]
                delay = event_time - previous_time

                if delay > 0:
                    print(f"Затримка перед виконанням: {delay}")
                    time.sleep(delay)

                print(f"Обробка події: {action}")
                if action["type"] == "keyboard":
                    print(f"Натискання клавіші: {action['key']}")
                    keyboard.press(action["key"])
                    keyboard.release(action["key"])
                elif action["type"] == "mouse_move":
                    print(f"Переміщення миші до x: {action['x']}, y: {action['y']}")
                    pyautogui.moveTo(action["x"], action["y"])
                elif action["type"] == "mouse_click":
                    if action["action"] == "down":
                        print(f"Натискання кнопки миші {action['button']}")
                        mouse.press(button=action['button'])
                    elif action["action"] == "up":
                        print(f"Відпускання кнопки миші {action['button']}")
                        mouse.release(button=action['button'])

                previous_time = event_time

        except Exception as e:
            print(f"Помилка при відтворенні макросу: {e}")
