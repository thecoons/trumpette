import unittest
from unittest.mock import Mock

from module.tweeter.manager import TweeterManager
from module.tweeter.exceptions import EmptyTimeline


class TestTweetManager(unittest.TestCase):

    def test_get_last_tweet(self):
        first_tweet = Mock(id=1)
        last_tweet = Mock(id=2)
        user_timeline = [last_tweet, first_tweet]

        tweet_interface = Mock()
        tweet_interface.GetUserTimeline.return_value = user_timeline

        tweeter_manager = TweeterManager(api=tweet_interface)
        last_tweet = tweeter_manager.get_last_tweet(user_id=999)

        tweet_interface.GetUserTimeline.assert_called_once_with(user_id=999)
        self.assertEqual(
            2,
            last_tweet.id,
        )

    def test_get_last_tweet_with_empty_timeline(self):
        user_timeline = []

        tweet_interface = Mock()
        tweet_interface.GetUserTimeline.return_value = user_timeline

        tweeter_manager = TweeterManager(api=tweet_interface)
        with self.assertRaises(EmptyTimeline):
            tweeter_manager.get_last_tweet(user_id=999)

