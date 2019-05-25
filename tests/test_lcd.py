import unittest
from unittest import mock

from module.lcd.display import LCDDisplayManager 

class TestLCDModule(unittest.TestCase):

    def test_display_frame_has_been_flush_before_display_message(self):
        lcd_interface = mock.Mock()
        message = 'Hello Gary!'
        display_manager = LCDDisplayManager(
            lcd_interface,
            message,
        )

        display_manager.display_frame()

        lcd_interface.clear.assert_called_once()
        lcd_interface.write_string.assert_called_once_with(message)
