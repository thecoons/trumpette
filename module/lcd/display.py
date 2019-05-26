import time
from .exceptions import FrameTooLong

class LCDDisplayManager:
    def __init__(self, lcd_interface, frame):
        self.lcd_interface = lcd_interface
        self.set_frame(frame)

    def set_frame(self, frame):
        if self._frame_validation(frame):
            self.frame = frame
        else:
            raise FrameTooLong('The frame you are tryng to set is not valid.')

    def display_frame(self):
        self.lcd_interface.clear()
        self.lcd_interface.write_string(
            self.frame,
        )

    def _lcd_char_size(self):
        return self.lcd_interface.cols * self.lcd_interface.rows

    def _frame_validation(self, frame):
        return len(frame) <= self._lcd_char_size()
