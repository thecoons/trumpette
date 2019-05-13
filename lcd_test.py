from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time


lcd = CharLCD(
    cols=16,
    rows=2,
    pin_rs=37,
    pin_rw=35,
    pin_e=33,
    pins_data=[16, 11, 12, 15],
    numbering_mode=GPIO.BOARD,
)


lcd.write_string('Salut gros chat :3')
time.sleep(5)
lcd.close(clear=False)
