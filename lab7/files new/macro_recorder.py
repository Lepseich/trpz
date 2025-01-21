class MacroRecorder:
    def record_macro(self, macro_name):
        print(f"Запис макросу: {macro_name}...")
        return f"{macro_name}.macro"

    def execute_macro(self, macro_file):
        print(f"Виконання макросу з файлу: {macro_file}...")
