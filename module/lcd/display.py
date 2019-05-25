import time

class LCDDisplayManager:
    def __init__(self, lcd_interface, message=''):
        self.lcd_interface = lcd_interface
        self.message = message

    def display_frame(self):
        self.lcd_interface.clear()
        self.lcd_interface.write_string(
            self.message,
        )
