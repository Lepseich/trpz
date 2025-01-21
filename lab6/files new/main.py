from factory import WinFactory, MacFactory
from application import Application

def main():
    os_type = input("Enter the OS (Windows/Mac): ").strip().lower()

    if os_type == "windows":
        factory = WinFactory()
    elif os_type == "mac":
        factory = MacFactory()
    else:
        print("Error: Unknown operating system.")
        return

    app = Application(factory)
    app.create_ui()
    app.paint()

if __name__ == "__main__":
    main()
