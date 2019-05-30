import unittest
from unittest import mock

from module.lcd.display import LCDDisplayManager 
from module.lcd.exceptions import FrameTooLong

class TestLCDModule(unittest.TestCase):

    def test_display_frame_has_been_flush_before_display_message(self):
        lcd_interface = mock.Mock()
        lcd_interface.lcd = mock.Mock(rows=16, cols=16)
        frame = 'Hello Gary!'
        display_manager = LCDDisplayManager(
            lcd_interface,
            frame,
        )

        display_manager.display_frame()

        lcd_interface.clear.assert_called_once()
        lcd_interface.write_string.assert_called_once_with(frame)

    def test_frame_cant_have_more_char_than_display(self):
        lcd_interface = mock.Mock()
        lcd_interface.lcd = mock.Mock(rows=2, cols=16)
        
        frame = 'X' * ((16 * 2) + 1)

        with self.assertRaises(FrameTooLong):
            LCDDisplayManager(
                lcd_interface,
                frame,
            )
