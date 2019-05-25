import unittest
from unittest import mock

from module.diode.manager import DiodeManager

class TestDiodeModule(unittest.TestCase):

    def test_turn_on_diode(self):
        diode_interface = mock.Mock()
        expected_pin = 1

        diode_manager = DiodeManager(
            interface=diode_interface,
            pin=expected_pin,
        )

        diode_manager.turn_on()

        diode_interface.output.assert_called_once_with(
            expected_pin,
            diode_interface.HIGH
        )

    def test_turn_on_diode(self):
        diode_interface = mock.Mock()
        expected_pin = 1

        diode_manager = DiodeManager(
            interface=diode_interface,
            pin=expected_pin,
        )

        diode_manager.turn_off()

        diode_interface.output.assert_called_once_with(
            expected_pin,
            diode_interface.LOW,
        )
