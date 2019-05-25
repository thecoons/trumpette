from .exceptions import EmptyTimeline

class TweeterManager:

    def __init__(self, api):
        self.api = api

    def get_last_tweet(self, user_id):
        user_timeline = self.api.GetUserTimeline(
            user_id=user_id,
        )

        try:
            return user_timeline[0]
        except IndexError:
            raise EmptyTimeline('The user timeline is empty ...')