import sys
import webbrowser

import tweepy


CONSUMER_KEY = ""
CONSUMER_SECRET = ""


def generate_user_access_token():
    """
    Generate a Twitter API connection with access for a specific user.

    Requires the user to view the browser URI that is automatically opened,
    then manually enter the pin in the command-line in order to generate
    the access token.

    :return: tweepy.OAuthHandler instance, with User Access Token set.
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    print("You need to authorize the application. Opening page in browser...\n")
    auth_url = auth.get_authorization_url()
    webbrowser.open(auth_url)

    user_pin = input("Generate a pin and enter it here, or type `quit`. /> ")
    if not user_pin or user_pin.lower() in ("q", "quit", "exit"):
        print("Exiting.")
        sys.exit(0)

    print("Authenticating...")
    auth.get_access_token(user_pin)

    return auth


auth = generate_user_access_token()
tweepy.API(auth)
