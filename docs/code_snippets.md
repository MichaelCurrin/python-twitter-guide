# Code snippets
> Common use-cases for Tweepy


This section aims at making at easier by doing that work for you and suggesting a good path, by providing recommended code snippets and samples of the data or returned. This guide is not meant to be complete, but rather to cover typical situations in a way that is easy for beginners to follow.

This based on Tweepy docs, Tweepy code and the Twitter API docs.

?> **Snippet use:**<br>You may copy and paste the code here into your own project and modify it as you need.<br><br>Pasting into a *script* and running is straightforward. But, note that if you paste into the *interactive* Python terminal you may get a syntax error because of the empty lines in functions.

## Naming conventions

- A tweet is called a status in the API and Tweepy.
- A profile is called a user.
- A username is called in a screen name.

These terms will be used interchangeably in this guide.


## Installation

### Install Tweepy for your own projects

If you are new to Python or virtual environments, read through this guide for more background on the instructions below.

- [Setup a Python 3 virtual environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7)


#### Install system dependencies

<!-- TODO: Link to Learn to Code project when links are updated -->

Install [Python 3](python.org/).


#### Install Python packages

```bash
cd my-project
```

Create a virtual environment. Here we use the `venv` tool which built-in for Python 3, but you can use something else.

```bash
python3 -m venv venv
```

Activate the virtual environment.

```bash
# Linux and macOS
source venv/bin/activate
# Windows
source venv\Scripts\activate
```

Install Tweepy into the virtual environment.

```bash
pip install tweepy
```

Now you can import Tweepy within the context of your project's virtual environment. A one-liner to test `tweepy`:

```sh
python -c 'import tweepy; print("It works!")
```

?> Use `deactivate` command to revert to the global environment. Make sure you use the activate command above whenever you need to use `tweepy` in your project.


## Authentication
> Authenticating with the Twitter API using a dev app's credentials

See also the [Authentication](http://docs.tweepy.org/en/latest/auth_tutorial.html) tutorial in the Tweepy docs.

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

If Access credentials are provided, the function will create an App Access Token. Otherwise, the access token step will be left out and the function will return an Application-only Access Token. Which has limited context (it can't access a current user) and has different API rate limit restrictions which can be more favorable for certain requests. 

?> Not covered here is the User access token, which requires a user to sign into Twitter and then enter a short code into your application. So that your app can perform actions on their behalf - this flow is unnecessary if you want to make a bot, do bulk retweets as your own bot account or do searches. Rate limiting is on each user. This use flow would require you to setup your own API to handle this complex flow. Or you can enter the code on the command-line and capture using `input()` if you want to try that out locally without the extra setup. 

Then set up an API instance which will automatically wait and print a notification if a rate limit is reached, to avoid getting blocked by the API.

If you are doing automation for a task like search, which doesn't need a concept of "me" as a Twitter account, you can use the "application-only" flow above which does **not** use access details, only consumer details. The drawback is that some methods around `.me` or `.home_timeline` will no longer work, but the advantage is that certain endpoints like `.search` have a higher threshold for rate limiting.

You can start using the application-only approach without hassle, but if you are interested to learn you can read the  [application-only](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only) doc.

> As this method is specific to the application, it does not involve any users. This method is typically for developers that need read-only access to public information. 
>
> API calls using app-only authentication are rate limited per API method at the app level. [source](https://developer.twitter.com/en/docs/basics/authentication/oauth-2-0)


#### Application-only flow

There are two way to do an application-only flow and get a App Access Token.

- One approach is using `OAuthHandler` - this is similar to the flow above but leaves out the `.set_access_token` step.
    ```python
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth)
    ```
- The other approach uses `AppAuthHandler` and is covered in the [OAuth 2](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-2-authentication) part of Tweepy docs.
    ```python
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth)
    ```

#### User flow

You can let a user sign in on the browser side of a web app, or in the command-line for a local terminal-based application. This is not necessary for doing searches or making a bot but is necessary if you want to perform actions on behalf of the user with their permission (such as a liking a Tweet in a mobile app you made).

The user will sign into Twitter and then will get a number to enter. The flow here is more complex. Read more [here](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-1a-authentication)

## Tweepy API overview

The `api` object returned in the auth section above will cover most of your needs for requesting the Twitter API, whether fetching or sending data.

The `api` object is an instance of `tweepy.API` class and is covered in the docs here and is useful to see the allowed parameters, how they are used and what is returned.

The methods on `tweepy.API`  also include some useful links in their docstrings, pointing to the Twitter API endpoints docs. These do not appear in the Tweepy docs. Therefore you might want to look at the [api.py](https://github.com/tweepy/tweepy/blob/master/tweepy/api.py) script in the Tweepy repo to see these links.


## Users

### Fetch the profile for the authenticated user

```python
api.me()
```

### Get author of a tweet

Whenever you have a tweet object you can find the profile that authored the tweet, without a doing a further API call.

```python
tweet.author
```

See [models](models.md) page for in this guide for attributes on a User instance.

### Fetch profile by ID

#### Lookup a single profile

By screen name.

```python
screen_name = "foo"
user = api.get_user(screen_name=screen_name)
```

By ID.

```python
user_id = "foo"
user = api.get_user(user_id=user_id)
```

?> Tweepy docs: [API.get_user](http://docs.tweepy.org/en/v3.8.0/api.html#API.get_user) 


Then you can inspect the user object or do actions on it. See the [User](models.md#user) section of the models page.

Example:

```python
user.screen_name
# => "foo"

user.id
# => 1234567

user.followers_count
# => 99
```

#### Lookup many profiles

By screen name.

```python
screen_names = ["foo", "bar", "baz"]
users = api.lookup_users(screen_names=screen_names)
```

By ID.

```python
user_ids = [123, 456, 789]
users = api.lookup_users(user_ids=user_ids)
```

?> Tweepy docs: [API.lookup_users](http://docs.tweepy.org/en/latest/api.html#API.lookup_users)

?> The endpoint only lets you request up to 100 IDs at once, so you'll never than more than one page of results. Therefore you get more results, you should batch your IDs into groups of 100 and then lookup each group.


## Find tweets

See also [Search API](#search-api) section to lookup tweets matching keywords or hashtags or directed at a user

### Get my timeline

Get tweets from your own account's timeline - the homepage feed of tweets you see when you log into Twitter that is based on users you follow.

```python
tweets = api.home_timeline()
```

?> Tweepy docs: [API.home_timeline](http://docs.tweepy.org/en/latest/api.html#API.home_timeline)


### Get a user's timeline

Get the last 200 tweets of a user. 

?> You can use `user_id` instead of `screen_name`.

```python
screen_name = "foo"
tweets = api.user_timeline(
    screen_name=screen_name,
    count=200, 
    tweet_mode="extended"
)
```

Print the results.

```python
for tweet in tweets:
    print(tweet.full_text)
```

?> Tweepy docs: [API.user_timeline](http://docs.tweepy.org/en/latest/api.html#API.user_timeline)


Note that even though we use _extended_ mode to show expanded rather than truncated tweets, the message of a retweet will be truncated still. So you this approach to get the full message on the _original_ tweet. Example from [source](https://stackoverflow.com/questions/42705314/getting-full-tweet-text-from-user-timeline-with-tweepy).

```
tweets = api.user_timeline(id=2271808427, tweet_mode="extended")

# This is still truncated.
tweets[6].full_text
# => 'RT @blawson_lcsw: So proud of these amazing @HSESchools students who presented their ideas on how to help their peers manage stress in mean…'

# Original expanded text.
tweets[6].retweeted_status.full_text
# => 'So proud of these amazing @HSESchools students who presented their ideas on how to help their peers manage stress in meaningful ways! Thanks @HSEPrincipal for giving us your time!'
```

### Fetch tweets by ID

If you know the ID of a tweet, you can fetch it. This is useful if you want to find the latest engagements count on a tweet, or if you have a list of just IDs from outside Tweepy and you want to turn them into Tweepy objects so you can get the message, author, date, etc.

#### Lookup a single tweet

```python
tweet_id = 123
api.get_status(tweet_id)
```

?> Tweepy docs: [API.get_status](http://docs.tweepy.org/en/latest/api.html#API.get_status)


#### Lookup many tweets

```python
tweet_ids = [123, 456, 789]
api.statuses_lookup(tweet_ids)
```

?> Tweepy docs: [API.statuses_lookup](http://docs.tweepy.org/en/latest/api.html#API.statuses_lookup)


### Get retweets of a tweet

Get up to 100 retweets on a given tweet.

```python
tweet_id = 123
count = 100
retweets = api.retweets(tweet_id, count)
```

I've not tested if this works with paging to get more.

?> Tweepy docs: [API.retweets](http://docs.tweepy.org/en/latest/api.html#API.retweets)

See also:

```python
retweets = tweet.retweets
```

### Get the target of a reply

Get tweet.

```python
original_tweet_id = tweet.in_reply_to_status_id

if original_tweet_id is not None:
    original_tweet = api.get_status(original_tweet_id)
```

Get user.

```python
original_user = tweet.in_reply_to_user_id
```


## Get tweet engagements

See more on the [models](models.md) page of this guide.


### Get favorites

```python
tweet.favorite_count
# => 0
```

### Get retweets

```python
tweet.retweet_count
# => 0
```

Get the retweets list.

```python
retweets = tweet.retweets
```


## Engage with tweet

!> Note that you should only use these actions if you included them in your dev application otherwise you may get blocked. Also if you have a read-only app, you can upgrade to a read and write app.

?! Please use these **sparingly**. The automation policy for Twitter API allows use of these actions as long as they are not used indiscriminately. If do favorite or retweet every tweet on a timeline or in a stream, you may get blocked for spammy low-quality behavior. If you do a search for popular tweets matching a hashtag and engage with a few of them, this will be fine.

?> See this guide's [Twitter policies](policies) page


### Favorite 

```python
tweet.favorite()
```

### Retweet

```python
tweet.retweet()
```

### Reply

A reply is a tweet directed at another tweet ID or user. When you reply to a tweet, it becomes a "thread" or "threaded conversation".

>! The Twitter automation policy is strict on this. Please make sure you understand it before replying to tweets. Doing a search for tweets and replying to them without the user opting in (such as by tweeting to you) is considered **spammy** behavior and will get shutdown.

?> [Twitter policies](policies) page.

A novel way to make replies without hitting policy restrictions is to make a tweet and then reply to yourself. This means you could chain together a list of say 10 items perhaps with pictures and group them together. I've seen this before and is a great way to overcome the character limit for writing a blog post.


## Post tweet

### FAQs

#### Can I reply to a tweet or @mention someone?

>! The Twitter automation policy is strict on this. Please make sure you understand it before replying to tweets. Doing a search for tweets and replying to them without the user opting in (such as by tweeting to you) is considered **spammy** behavior and will get shutdown.

#### Can I make a plain tweet?

If you just want to make a tweet message without replying or mentioning, you are allowed to do this using the API. For example a bot which posts content daily from reddit or a weather or finance service.


### Message only

```python
msg = 'Hello, world!'

tweet = api.update_status(msg)
```

- Tweepy docs link: [API.update_status](http://docs.tweepy.org/en/latest/api.html#API.update_status).
- Twitter API endpoint: [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update)

### Message with media

Upload an image or animated GIF on disk.

```python
media_path = 'foo.gif'
msg = 'Hello, world!'

tweet = api.update_with_media(media_path, status=msg)
```

- Tweepy docs link: [API.update_with_media](http://docs.tweepy.org/en/latest/api.html#API.update_with_media).


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


## Streaming

**Links:**

- [Tweepy docs Streaming tutorial](http://docs.tweepy.org/en/latest/streaming_how_to.html).
- [Tweepy examples/streaming.py](https://github.com/tweepy/tweepy/blob/master/examples/streaming.py) script.
