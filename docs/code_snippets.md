# Code snippets
> Common use-cases for Tweepy


This section aims at making at easier by doing that work for you and suggesting a good path, by providing recommended code snippets and samples of the data or returned. This guide is not meant to be complete, but rather to cover typical situations in a way that is easy for beginners to follow.

This based on Tweepy docs, Tweepy code and the Twitter API docs.

## Snippet use

You may copy and paste the code here into your own project and modify it as you need.

Pasting into a script is easy, but note that if you paste into the interactive Python terminal you may get a syntax error because of the empty lines in functions.


## Authorize

### Setup credentials

Dummy values:

```python
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
```

Make sure to **never** includes these in version control (commits). They can be stored in an unversioned config file or environment variables.


### Basic usage

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.verify_credentials()
```

### Advanced usage

```python
def get_api_connection(consumer_key, consumer_secret, access_key=None,
                       access_secret=None):
    """
    Authorize with Twitter and return API connection object.
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    if access_key and access_secret:
        auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api


api = get_api_connection(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)
```

Notes:

- If Access credentials are provided, create an App Access Token. Otherwise, create an Application-only Access Token, which has limited context (it can't access a current user), it but different API rate limit restrictions which can be more favorable for certain requests.
- Then set up an API instance which will automatically wait and print a notification if a rate
limit is reached, to avoid getting blocked by the API.
- See [application-only](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only) doc.


## Users

### Get profile for authenticated user

```python
api.me()
```

### Get author of tweet

```python
tweet.author
```

### Get profile for a username

```python
user = api.get_user(username)

user.screen_name
user.followers_count
```


## Post tweet

### Message only

```python
msg = 'Hello, world!'

tweet = api.update_status(msg)
```

### Message with media

Upload an image or animated GIF on disk.

```python
media_path = 'foo.gif'
msg = 'Hello, world!'

tweet = api.update_with_media(media_path, status=msg)
```


## Handle time values

Parse a datetime string as returned from Twitter API. Tweepy does not do any logic here, so we convert it into a datetime object to make it more useful.

```python
import datetime


TIME_FORMAT_IN = r"%Y-%m-%dT%H:%M%z"


def parse_datetime(value):
    """
    Convert from Twitter datetime string to a datetime object.

    >>> parse_datetime('2020-01-24T08:37:37+00:00')
    datetime.datetime(2020, 1, 24, 8, 37, tzinfo=datetime.timezone.utc)
    """
    dt = ":".join(value.split(":", 2)[:2])
    tz = value[-6:]
    clean_value = f"{dt}{tz}"

    return datetime.datetime.strptime(clean_value, TIME_FORMAT_IN)
```

Notes:

- When splitting, we don't need seconds and any decimals (which have changed style before between API versions). So ignore after the 2nd colon.
- The value from Twitter will be in GMT zone, regardless of your location or profile settings.

Example usage:

```python
>>> dt = parse_datetime(tweet.created_at())
>>> print(dt.year)
2020
```


## Search

```python
def search_api_for_tweets(query, result_type="popular"):
    # Result type: 'recent' 'popular' 'mixed'
    api = twitter.get_api_connection(**CONF["twitter_credentials"])

    tweets = api.search(
        query, count=100, tweet_mode="extended", result_type=result_type
    )

    return tweets
```
