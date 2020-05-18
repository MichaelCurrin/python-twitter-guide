def get_message(tweet):
    """
    Robustly get a message on a tweet, even if truncated or a retweet (always truncated).
    """
    try:
        return tweet.full_text
    except AttributeError:
        return tweet.text


query = "-filter:retweets -filter:replies python"
lang = "en"

cursor = tweepy.Cursor(
    api,
    q=query,
    count=100,
    tweet_mode="extended",
    lang=lang,
)

results = []

for tweet in cursor.items():
    parsed_tweet = {
        "id": tweet.id,
        "screen_name": tweet.author.screen_name,
        "message": get_message(tweet),
    }
    print(parsed_tweet)
    results.append(parsed_tweet)

print(len(results)
