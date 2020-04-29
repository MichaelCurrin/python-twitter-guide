"""
Streaming demo - Tweepy docs example.

Based on tutorial: http://docs.tweepy.org/en/latest/streaming_how_to.html
"""
import tweepy


CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_error disconnects the stream on rate limiting.
            # This is recommended.
            return False

        # Returning non-False reconnects the stream, with backoff.


auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=auth, listener=myStreamListener)

# Follow tweets with the word "python".
# Note that is the command is blocking, so any lines after this will not execute.
myStream.filter(track=["python"])

# Use async flag so that a separate thread is used.
# myStream.filter(track=['python'], is_async=True)

# Follow user ID "2211149702"
# myStream.filter(follow=["2211149702"])
