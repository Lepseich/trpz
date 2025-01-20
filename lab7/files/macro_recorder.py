class MacroRecorder:
    def __init__(self):
        self.macros = {}

    def start_recording(self, macro_name):
        print(f"Started recording macro: {macro_name}")
        # Logic for recording user actions goes here.

    def stop_recording(self, macro_name):
        print(f"Stopped recording macro: {macro_name}")
        # Save the recorded macro.
        self.macros[macro_name] = f"Recorded actions for {macro_name}"

    def play_macro(self, macro_name):
        if macro_name in self.macros:
            print(f"Playing macro: {macro_name}")
            # Logic for playing back recorded actions goes here.
        else:
            print(f"Macro {macro_name} does not exist.")

    def get_macros(self):
        return self.macros.keys()