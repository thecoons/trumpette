#!/usr/bin/env python
import twitter
import time
import RPi.GPIO as GPIO
from unittest import mock

from module.tweeter.manager import TweeterManager
from module.diode.manager import DiodeManager

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
diode_manager = DiodeManager(interface=GPIO, pin=7)



api = twitter.Api(
    consumer_key='eaBcw0YCEnfVEu2pPuDPgJ161',
    consumer_secret='0QW3zLsLjqMMth5Rvfjc7RkFbgFBFO4T3LQTp36qj3jwcV9pNI',
    access_token_key='823823410350477313-4Fud2SRmY5J62sDkL8guCSFn8E8x7vU',
    access_token_secret='rI18QbDBN8j18MsFZTRf7eRPXoQQk4iufvCZVsD5vBYSI',
)
tweeter_manager = TweeterManager(api=api)

last_tweet_id = -1

while True:
    tweet = tweeter_manager.get_last_tweet(user_id=25073877)

    if last_tweet_id != tweet.id:
        last_tweet_text = tweet.text
        last_tweet_id = tweet.id
        print(last_tweet_text)
        print(last_tweet_id)
        for tick in range(10):
            diode_manager.turn_on()
            time.sleep(1)
            diode_manager.turn_off()
            time.sleep(1)

    time.sleep(300)
