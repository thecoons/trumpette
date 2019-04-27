#!/usr/bin/env python
import twitter
import time
import RPi.GPIO as GPIO
from unittest import mock 

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)



api = twitter.Api(
    consumer_key='eaBcw0YCEnfVEu2pPuDPgJ161',
    consumer_secret='0QW3zLsLjqMMth5Rvfjc7RkFbgFBFO4T3LQTp36qj3jwcV9pNI',
    access_token_key='823823410350477313-4Fud2SRmY5J62sDkL8guCSFn8E8x7vU',
    access_token_secret='rI18QbDBN8j18MsFZTRf7eRPXoQQk4iufvCZVsD5vBYSI',
)
last_tweet_id = -1

while True:
    trump_timeline = api.GetUserTimeline(user_id=25073877)
    tweet = trump_timeline[0]

    if last_tweet_id != tweet.id:
        last_tweet_text = tweet.text
        last_tweet_id = tweet.id
        print(last_tweet_text)
        print(last_tweet_id)
        for tick in range(10):
            GPIO.output(7, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(7, GPIO.LOW)
            time.sleep(1)

    time.sleep(300)
