import unittest
from unittest.mock import Mock, call, patch
from module.scene.models import MessageScene

class TestMessageScene(unittest.TestCase):

    def test_play_message_scene(self):
        elapse_time = 1
        mock_lcd_manager = Mock()
        mock_lcd_manager.lcd_char_size.return_value = 32
        message_scene = MessageScene(
            lcd_manager=mock_lcd_manager,
            elapse_time=elapse_time,
        )
        
        message_scene.set_message('Hello world !')
        with patch('time.sleep'):        
            message_scene.play()

        mock_lcd_manager.set_frame.assert_called_once_with(
            frame='Hello world !'
        )
        mock_lcd_manager.display_frame.assert_called_once()

    def test_play_message_scene_with_long_message(self):
        expected_elapsed_time = 5
        mock_lcd_manager = Mock()
        mock_lcd_manager.lcd_char_size.return_value = 32
        message_scene = MessageScene(
            lcd_manager=mock_lcd_manager,
            elapse_time=expected_elapsed_time,
        )
        
        message_scene.set_message('X' * (16 * 2) + 'Y' * (16 * 2))
        with patch('time.sleep') as mocked_time:
            message_scene.play()

        mock_lcd_manager.set_frame.assert_has_calls(
            [
                call(frame='X' * (16 * 2)),
                call(frame='Y' * (16 * 2)),
            ],
        )
        mock_lcd_manager.display_frame.assert_has_calls(
            [
                call(),
                call(),
            ],
        )
        mocked_time.assert_has_calls(
            [
                call(expected_elapsed_time),
                call(expected_elapsed_time),
            ]
        )