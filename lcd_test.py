from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

from module.lcd.display import LCDDisplayManager


lcd = CharLCD(
    cols=16,
    rows=2,
    pin_rs=37,
    pin_rw=35,
    pin_e=33,
    pins_data=[16, 11, 12, 15],
    numbering_mode=GPIO.BOARD,
)

display_manager = LCDDisplayManager(lcd, 'Hello Toi !!!!!')
display_manager.display_frame()
time.sleep(1)
display_manager.message = 'Et toi aussi !!!'
display_manager.display_frame()
for i in range(20):
    display_manager.message = str(i)
    display_manager.display_frame()



lcd.close(clear=False)

