from main_facade import MainFacade

class AutomationClient:
    def __init__(self):
        self.facade = MainFacade()

    def run(self):
        print("Welcome to the Automation Tool!")
        while True:
            print("\nOptions:")
            print("1. Add Rule")
            print("2. Record Macro")
            print("3. Schedule Task")
            print("4. Execute All")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                trigger = input("Enter trigger: ")
                action = input("Enter action: ")
                self.facade.add_rule(trigger, action)
            elif choice == "2":
                macro_name = input("Enter macro name: ")
                self.facade.record_macro(macro_name)
            elif choice == "3":
                task_name = input("Enter task name: ")
                time = input("Enter time (HH:MM): ")
                self.facade.schedule_task(task_name, time)
            elif choice == "4":
                self.facade.execute_all()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    client = AutomationClient()
    client.run()





















