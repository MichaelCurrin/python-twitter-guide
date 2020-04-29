"""
Stream watcher - from Tweepy example repo.

Based on PY 2 script here: https://github.com/tweepy/examples/blob/master/streamwatcher.py
"""
import time
from getpass import getpass
from textwrap import TextWrapper

import tweepy


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''


class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print(self.status_wrapper.fill(status.text))
            print('\n %s  %s  via %s\n'
                % (status.author.screen_name, status.created_at, status.source))
        except Exception:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print('An error has occurred! Status code = %s' % status_code)

        # Keep stream alive.

        return True

    def on_timeout(self):
        print('Snoozing Zzzzzz')


auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

stream = tweepy.Stream(
    auth,
    StreamWatcherListener(),
    timeout=None
)
