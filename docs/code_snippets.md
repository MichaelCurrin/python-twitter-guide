# Code snippets
> Common use-cases for Tweepy


This section aims at making at easier by doing that work for you and suggesting a good path, by providing recommended code snippets and samples of the data or returned. This guide is not meant to be complete, but rather to cover typical situations in a way that is easy for beginners to follow.

This based on Tweepy docs, Tweepy code and the Twitter API docs.

## Snippet use

You may copy and paste the code here into your own project and modify it as you need.

Pasting into a script is easy, but note that if you paste into the interactive Python terminal you may get a syntax error because of the empty lines in functions.


## Authorization
> Authenticating with Twitter API using dev account credentials

### Setup credentials

Dummy values:

```python
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
```

Make sure to **never** includes these in version control (repo commits). They can be stored in an unversioned config file (ignored by `.gitignore`) or using environment variables.

A typical config setup would be one of these:

- `.env` - Shell script of properties. Readable from the shell or a Python package (e.g. `dotenv`).
- `config_local.yaml` - A YAML config file. Readable using PyYAML.

### Simple usage

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.verify_credentials()
```

### Use a function

Put the logic above in a function. This makes keeps the values out of the global scope and it means it is easy to import and use the function in multiple scripts.

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


# Example use:
api = get_api_connection(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)
```

?> If Access credentials are provided, create an App Access Token. Otherwise, create an Application-only Access Token, which has limited context (it can't access a current user), it but different API rate limit restrictions which can be more favorable for certain requests.

?> Then set up an API instance which will automatically wait and print a notification if a rate
limit is reached, to avoid getting blocked by the API.

?> See [application-only](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only) doc.


## Users

### Fetch the profile for the authenticated user

```python
api.me()
```

### Get author of a tweet

```python
tweet.author
```

### Fetch profile for a given username

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

?> When splitting, we don't need seconds and any decimals (which have changed style before between API versions). So ignore after the 2nd colon.

?> The value from Twitter will be in GMT zone, regardless of your location or profile settings.

Example usage:

```python
>>> dt = parse_datetime(tweet.created_at())
>>> print(dt.year)
2020
```


## Search API

The Twitter Search API lets you get tweets made in the past 7 to 10 days.

### Query syntax

You can test a search query out in the Twitter search bar before trying it in the API.

Here we choose a high volume term for testing but you can choose anything.

e.g.

```python
query = "python"
```

### Tweepy search method

#### Basic

Return tweets for a search query. Only gives 20 tweets.

```python
tweets = api.search(query)
```

```python
def process_tweet(tweet):
    print(tweet.id)
    print(tweet.text)
    print(tweet.author)
    print()


for tweet in tweets:
    process_tweet(tweet)
```

#### Get more tweets

With search API, you can specify a max of up to `100` items (tweets) per page. The other endpoints like user timelines seem to mostly allow up to `200` items on a page.

```python
tweets = api.search(
    query,
    count=100
)
```

If you want to get the _next_ 100 tweets after that, you could get the ID of the last tweet and use that to start the search at the next page, modified with `since_id=last_tweet_id-1`. You'd also have to check when there are no Tweets left and then stop searching.

However, it is much more practical to use Tweepy's **cursor** approach to do paging.

```python
cursor = tweepy.Cursor(api.search, count=100)
```

In both examples below, we process 500 tweets (assuming there are actually 500 tweets out there matching the search).

```python
for tweet in cursor.items(500):
    process_status(tweet)
```

```python
for page in cursor.pages(5):
    for tweet in page:
        process_status(tweet)
```

Both approaches will get 5 pages from the API and so take the same number of API requests and will give the same tweet results. The difference is that the `.items` approach will add a logic layer so that you only care about tweets and not pages.

?> See [Cursor tutorial](http://docs.tweepy.org/en/latest/cursor_tutorial.html) on Tweepy docs.


#### Extended message

Set `tweet_mode` to `extended`.

- This will give messages that are not truncated (with an ellipsis at the end).
- Note that retweets messages might still be truncated even with this option.
- When using this option, make sure to use the `tweet.full_text` attribute and not `tweet.text`, to avoid an error.

```python
tweets = api.search(
    query,
    tweet_mode="extended"
)
```

#### Result type

Set `result_type` to one of the following, according to Twitter API:

- `recent` - The tweets that are most recent.
- `popular`- The tweets with the highest engagements. Note that this list might be very short - just a few tweets - compared with running the `recent` query query.
- `mixed` - A balance of the other two. Default option.


```python
result_type = "popular"

tweets = api.search(
    query,
    count=100,
    result_type=result_type
)
```
