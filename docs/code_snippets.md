# Code snippets
> Common use-cases for the Twitter API and how to solve them with Tweepy


This section aims at making at easier by doing that work for you and suggesting a good path, by providing recommended code snippets and samples of the data or returned. This guide is not meant to be complete, but rather to cover typical situations in a way that is easy for beginners to follow.

This based on Tweepy docs, Tweepy code and the Twitter API docs.

?> **Snippet use:**<br>You may copy and paste the code here into your own project and modify it as you need.<br><br>Pasting into a *script* and running is straightforward. But, note that if you paste into the *interactive* Python terminal you may get a syntax error because of the empty lines in functions.


## Naming conventions

- A tweet is called a status in the API and Tweepy.
- A profile is called a user.
- A username is called in a screen name.

These terms will be used interchangeably in this guide.


## Installation
> How to install Tweepy

Using your shell (PowerShell or Bash/ZSH), install the Tweepy Python package so that you can run it inside Python code in the rest of this guide.

I strongly recommend installing Tweepy in a virtual environment and not using a global install for your user or root user.

!> Avoid using the `sudo` command to become root and install with elevated privileges. i.e. Leave out `sudo` here: `sudo pip install ...`. Since running `sudo` allows a package to run malicious code at the root level including deleting files or installing a virus. If you _really_ want to install at the global level for your user and `pip install PACKAGE` gives an error, add `--user` flag.

>? If you are new to Python or virtual environments, I recommend that you read through this guide for more background on the instructions covered below. [Setup a Python 3 virtual environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7)


### Install system dependencies

<!-- TODO: Link to Learn to Code project or gist when links are updated -->

Install [Python 3](https://python.org/).


### Install Python packages

Navigate to your project root folder.

```bash
cd my-project
```

Create a virtual environment named `venv`.

?> Here we use the builtin `venv` tool after the `-m` module flag, but you can use something else like Pipenv if you like.

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

?> You're already inside a sandboxes Python 3 environment so no need to specify `pip3` or `sudo`.

Now you can import Tweepy within the context of your project's virtual environment. A one-liner to test `tweepy`:

```sh
python -c 'import tweepy; print("It works!")
```

?> Use `deactivate` command to revert to the global environment. Make sure you use the activate command above whenever you need to use `tweepy` in your project.


## Authentication
> Authenticating with the Twitter API using a dev app's credentials

See also the [Authentication](http://docs.tweepy.org/en/latest/auth_tutorial.html) tutorial in the Tweepy docs.

### Setup credentials

Paste each of the four values from your credentials in your code like this. Replace the dummy values in quotes with your own values.

```python
CONSUMER_KEY = 'abc'
CONSUMER_SECRET = 'def'
ACCESS_KEY = 'foo'
ACCESS_SECRET = 'bar'
```

!> Make sure to **never** includes these in version control (repo commits). They can be stored in an unversioned config file (ignored by `.gitignore`) or using environment variables.

A typical setup is to store your credentials in a config file ignored by `git`, rather than in a Python script. Here are some options:

- `.env` - Shell script of properties. Readable from the shell or a Python package (e.g. `dotenv`).
- `config_local.ini` - A config file readable using the builtin ConfigParser in Python.
- `config_local.yaml` - A YAML config file. Readable using the PyYAML library once that is installed.


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

#### User auth flow

You can let a user sign in on the browser side of a web app, or in the command-line for a local terminal-based application. This is not necessary for doing searches or making a bot but is necessary if you want to perform actions on behalf of the user with their permission (such as a liking a Tweet in a mobile app you made).

The user will sign into Twitter and then will get a number to enter. The flow here is more complex. Read more [here](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-1a-authentication)


## Tweepy API overview

The `api` object returned in the auth section above will cover most of your needs for requesting the Twitter API, whether fetching or sending data.

The `api` object is an instance of `tweepy.API` class and is covered in the docs here and is useful to see the allowed parameters, how they are used and what is returned.

The methods on `tweepy.API`  also include some useful links in their docstrings, pointing to the Twitter API endpoints docs. These do not appear in the Tweepy docs. Therefore you might want to look at the [api.py](https://github.com/tweepy/tweepy/blob/master/tweepy/api.py) script in the Tweepy repo to see these links.



## Paging

Follow the Tweepy tutorial to get familiar with how to use a Cursor to do paging - iterate over multiple pages of items of say 100 tweets each.


http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html

The tutorial also explains truncated and full text.


## Users

### Fetch the profile for the authenticated user

```python
api.me()
```

### Get the author of a tweet

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

### Search for user

```python
users = api.search_users(q, count=20)
```

The count argument may not be greater than 20 according to Tweepy docs, but you may use paging.

?> Tweepy docs: [API.search_users](http://docs.tweepy.org/en/latest/api.html#API.search_users)


## Find tweets

?> If you want to do a search for tweets based on hashtags or phrases or that are directed at a user, go to the [Search API](#search-api) section.

**Links:**

- Twitter API: [Timelines overview](https://developer.twitter.com/en/docs/tweets/timelines/overview)
- Twitter API: [Post, retrieve, and engage with Tweets](https://developer.twitter.com/en/docs/tweets/post-and-engage/overview)


### Get my timeline

Get tweets from your own users's timeline, as a mix of their own and friend's tweets.

```python
tweets = api.home_timeline()
```

> Returns the 20 most recent statuses, including retweets, posted by the authenticating user and that user’s friends.
This is the equivalent of /timeline/home on the Web.

?> Tweepy docs: [API.home_timeline](http://docs.tweepy.org/en/latest/api.html#API.home_timeline)


### Get a user's timeline

Get the last 200 tweets of a user.

```python
tweets = api.user_timeline()
```

The default behavior is for the authenticated use. You can specify `user_id` or `screen_name` to target a user.


Example:

```python
screen_name = "foo"
tweets = api.user_timeline(
    screen_name=screen_name,
    count=200,
    tweet_mode="extended"
)

for tweet in tweets:
    print(tweet.full_text)
```

?> Tweepy docs: [API.user_timeline](http://docs.tweepy.org/en/latest/api.html#API.user_timeline) <br>Twitter API docs: [GET statuses/user_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline) - note daily limit of 100k tweets and getting 3,200 most recent tweets, otherwise there is not really a date restriction on how many days or years you can go back to.


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

Get the favorites list. Supports paging.

```python
tweet.favorites
```

### Get retweets

```python
tweet.retweet_count
# => 0
```

Get the retweets list. Supports paging.

```python
retweets = tweet.retweets
```


## Engage with a tweet

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

Yes, but only if they have first messaged you. The Twitter automation [policy](policies.md is **strict** on this. Please make sure you understand it before replying to tweets. 

Doing a search for tweets and replying to them without the user opting in (such as by tweeting to you) is considered **spammy** behavior and will likely get your account shutdown.

#### Can I make a plain tweet?

If you just want to make a tweet message without replying or mentioning, you are allowed to do this using the API. For example a bot which posts content daily from reddit or a weather or finance service.


### Tweet a text message

```python
msg = 'Hello, world!'

tweet = api.update_status(msg)
```

- Tweepy docs link: [API.update_status](http://docs.tweepy.org/en/latest/api.html#API.update_status).
- Twitter API endpoint: [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update)


To choose a random text message:


```python
msgs = ["Foo", "Bar baz")
msg = randon.choice(msgs)
```

### Tweet a message with media

Upload an image or animated GIF.

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

The Twitter Search API lets you get tweets made in the past 7 to 10 days. The approaches below take you from getting 20 tweets to thousands of tweets.

?> If you want a live stream of tweets, see the [Streaming](#streaming) section.

### Query syntax

Twitter has a flexible search syntax for using "and" / "or" logic and quoting phrases.

Twitter API docs on search.

- [Overview of standard operators](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators).
- [Guide to build standard queries](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/guides/build-standard-queries).

?> Be sure to use the _standard_ docs as the _premium_ operators do not work on the free search services.

?> You can test a search query out in the Twitter search bar before trying it in the API.


### Search query examples

Some examples to demonstrate common use of the search syntax.

- Single term
    - `'foo`
    - `#foo`
    - `@some_handle`
- Require _all terms_. Note that `AND` logic is implied. The order does not matter.
    - `foo bar baz`
    - `to:some_handle foo`
    - `from:some_handle foo`
- Require _at least one term_ - uses the `OR` keyword.
    - `foo OR bar`
    - `#foo OR bar`
- Exclusion - Using leading minus sign.
    - `foo -bar`
- Groups
    - Require _all groups_.
        - `(foo OR bar) (spam OR eggs)`
        - `(foo OR bar) -(spam OR eggs)`
    - Require _any group_.
        - `(foo OR bar) OR (spam OR eggs)`
- Exact match on a phrase
    - `"Foo bar"`
    - `"Foo bar" OR "Fizz buzz" OR spam`
    
?> Searching is case **insensitive**.

?> The `to` and `from` operators are provided by the Twitters docs. Using `@some_handle` might provide the same as `to:some_handle` but I have not tested. Using `@some_handle` might include tweets by the user too. 

?> When looking up a user, you may wish to _leave off_ the `@` to get more results which are still relevant, provided the handle is not a common word. I found this increase the volume.

?> When combing `AND` and `OR` functionality in a single rule, the `AND` logic is evaluated first. Such that `foo OR bar fizz`  is equivalent to `foo OR (bar fizz)`. Though, braces are preferred for readability.

?> Note for the last example above that double-quoted phrases must be *before* ordinary terms, due to a known Twitter Search API bug. 


### Tweepy search method


**Links to docs:**

- Twitter API  docs: [Standard search API](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets).
- Tweepy docs: [API.search](http://docs.tweepy.org/en/latest/api.html#API.search)
    - That section explains how it works and what the method parameters do.


#### Define query


Create a variable which contains your query. The query should be a single string, not a list, and should match exactly what you'd put in the Twitter.com search bar (which also makes it easy to test).


**Examples:**

- Basic.
    ```python
    query = "#python"
    ```
- Complex - Use the rules linked above or see the [Query syntax](#query-syntax) section.
    ```python
    query = "foo bar"
    
    query = "foo OR bar"
    ```
- A quoted phrase - just change the outside to single quotes.
    ```python
    query = '"foo bar"'
    ```


#### Basic

Return tweets for a search query. Only gives 20 tweets by default, so read on to get more.

```python
tweets = api.search(query)
```

Example of iterating over the results in `tweets` object:

```python
def process_tweet(tweet):
    print(tweet.id)
    print(tweet.text)
    print(tweet.author)
    print()


for tweet in tweets:
    process_tweet(tweet)
```

#### Get a page of 100 tweets

With search API, you can specify a max of up to `100` items (tweets) per page. The other endpoints like user timelines seem to mostly allow up to `200` items on a page.

```python
tweets = api.search(
    query,
    count=100
)
```

If you want to get the _next_ 100 tweets after that, you could get the ID of the last tweet and use that to start the search at the next page, modified with `since_id=last_tweet_id-1`. You'd also have to check when there are no Tweets left and then stop searching. However, it is much more practical to use Tweepy's **Cursor** approach to do paging, covered next.

#### Get many tweets using paging

This approach using the [Paging](#paging) approach to do multiple requests for pages of up to 100 tweets each, allowing you get thousands of tweets.

!> Twitter API imposes **rate limiting** against a token, to prevent abuse. So, after you've met your quota of searches in a 15-minute window (whether new searches or paging on one search), you will have have to **wait** until it resets and then do more queries. Any requests before then will fail (though other will have their own limit). This **waiting** can be turned on as covered in [Installation](#installation) section.

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

## Get entities on tweets

### Get media

How to get images on tweets.

?> This example is for the [Search API](#search-api) but can work for other methods too such as [User timeline](#get-a-user39s-timeline).


Add _entities_ to your request (this may not always be needed on some endpoints), then use the media value, if one exists on a tweet's entities.

```python
cursor = tweepy.Cursor(
    api.search,
    q=query,
    count=100
    include_entities=True
)

for tweet in cursor:
    if 'media' in tweet.entities:
        for image in tweet.entities['media']:
            print(image['media_url'])
```


## Streaming

This section focuses on the free streaming API service. There are other premium services available, covered in Twitter's dev docs.

### Resources

- Tweepy
    - [Streaming tutorial](http://docs.tweepy.org/en/latest/streaming_how_to.html) in the docs.
    - [streaming.py](https://github.com/tweepy/tweepy/blob/master/examples/streaming.py) example script in the repo.
    - [streaming.py](https://github.com/tweepy/tweepy/blob/tweepy/streaming.py) script in the repo. This is useful to find or override existing methods.
        - See [StreamListener](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L30) class.
        - See [Stream](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L209) class and [Stream.filter](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L451-L474) method.
     - [test_streaming.py](https://github.com/tweepy/tweepy/blob/master/tests/test_streaming.py) - Python tests for `streaming` module.
- Twitter API docs
    - [Filter realtime Tweets](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter)
        - Make sure to use "POST statuses/filter" as the other endpoints are premium only.
    - [Basic stream parameters](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters)


### Setup stream  object

Based on the script in the [tweepy/examples](https://github.com/tweepy/examples/) repo.

See the original [StreamListener](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L30) class.

```python
import tweepy


class StreamWatcherListener(tweepy.StreamListener):

    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print(self.status_wrapper.fill(status.text))
            print('\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source))
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        
        return True  # keep stream alive

    def on_timeout(self):
        print('Snoozing Zzzzzz')
      

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
stream = tweepy.Stream(
    auth, 
    StreamWatcherListener(), 
    timeout=None
)
```

Follow the sections below to start streaming using the `stream` object.


### Follow tweets by users

Use the **follow** parameter the IDs of one or more Twitter users

!> Do not use Twitter handles. 

If you need to the get ID of a user, use:

```python
user = api.get_user(screen_name=screen_name)
user_id = user.id
```

In Tweepy, this must be a `list` of strings.

e.g.

```python
user_ids = ["1234567", "456789", "9876543"]

streamer.filter(follow=user_ids)
```

?> Twitter API docs: [Basic stream parameters](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) (see **follow**).


### Follow tweets by content

Use the **track** parameter and one or more terms.

Example:

```python
track = ["foo", "#bar", "fizz buzz", "example.com"]

streamer.filter(track=track)
```

The Twitter API will look for a tweet which contains _at least one_ of the items in the list, so it uses `OR` logic. Use a space between words in a string to use `AND` logic.

!> You **cannot** use quoted phrases. The API doc says: "Exact matching of phrases (equivalent to quoted phrases in most search engines) is not supported.".

>? UTF-8 characters are supported. e.g. `Twitter’s`.

?> Twitter API docs: [Basic stream parameters](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) (see **track**).
