from automation_facade import AutomationFacade

if __name__ == "__main__":
    # Ініціалізація фасаду
    automation_tool = AutomationFacade()

    # Тест 1: Завантаження відео та планування його роздачі
    print("=== Тест 1: Завантаження відео та планування ===")
    automation_tool.download_and_schedule_video(
        channel_url="https://youtube.com/examplechannel",
        video_format="mp4",
        time="6:00 AM"
    )

    # Тест 2: Запис та виконання макросу
    print("\n=== Тест 2: Запис та виконання макросу ===")
    automation_tool.record_and_execute_macro("TestMacro")

    print("\nПеревірка завершена. Патерн Facade працює коректно.")
