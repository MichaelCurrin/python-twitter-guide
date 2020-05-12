# Tweepy code samples
> Common use-cases for the Twitter API and how to solve them in Python 3 using Tweepy


## Quick links
> Jump to some highlighted sections

[Get users](#get-users) | [Get tweets](#get-tweets) | [Post tweet](#post-tweet) | [Search API](#search-api) | [Streaming](#streaming)


## TL;DR
> A summary of this page.

If you have authenticated with Twitter as per the [Authentication](auth.md) instructions, then you can interact with the Twitter API using the `api` object.

For example:

```python
api.me()

api.search(q="#foo")

api.update_status("Hello, world!")
```

Keep reading this page for more details.


## About

This section aims at making at easier by doing that work for you and suggesting a good path, by providing recommended code snippets and samples of the data or returned. This guide is not meant to be complete, but rather to cover typical situations in a way that is easy for beginners to follow.

This based on Tweepy docs, Tweepy code and the Twitter API docs.

?> **Snippet use:**<br>You may copy and paste the code here into your own project and modify it as you need.<br><br>Pasting into a *script* and running is straightforward. And pasting most code into the **interactive terminal* is fine, but you'll get a syntax error if you paste a function which has empty lines, so use a script instead for that.


## Naming conventions

- A _tweet_ is called a _status_ in the API and Tweepy.
- A _profile_ is called a _user_ or _author_ in the API and Tweepy.
- A _username_ is called a _screen name_ in the API and Tweepy.

These terms will be used interchangeably in this guide.


## Tweepy API overview

The `api` object returned in the auth section above will cover most of your needs for requesting the Twitter API, whether fetching or sending data.

The `api` object is an instance of `tweepy.API` class and is covered in the docs here and is useful to see the allowed parameters, how they are used and what is returned.

The methods on `tweepy.API`  also include some useful links in their docstrings, pointing to the Twitter API endpoints docs. These do not appear in the Tweepy docs. Therefore you might want to look at the [api.py](https://github.com/tweepy/tweepy/blob/master/tweepy/api.py) script in the Tweepy repo to see these links.



## How do I get a high of volume of tweets?

- Add a [waiting](auth.md#add-waiting) config option as per the auth guide so that Tweepy will automatically wait when it rates a rate limit exceeded point.
- Use [Paging](#paging) here so that Tweepy will iterate over multiple pages for you.
- Pick a token auth approach that gives the most tweets in a window. See the [Rate limits](policies#rate-limits) section on Twitter policies page. For example, App-only Token is more suitable for search than for App Access Token (with user context).


## Paging

Follow the Tweepy tutorial to get familiar with how to use a Cursor to do paging - iterate over multiple pages of items of say 100 tweets each.


?> **Tweepy docs**: [Cursor tutorial](http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html). The tutorial also explains truncated and full text.


### Setup the cursor

An `api` method must be passed to the cursor, along with any parameters.

```python
cursor = tweepy.Cursor(
    api.search,
    query,
    count=100
)
```

?> **Tweepy repo:** [Cursor class](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/cursor.py#L9)


### Pages and items

When iterating over the cursor, you must specify if you want the response to be pages or items.

Pages is how Twitter API works - you get multiple pages of say 100 tweets each, so you iterate over page which then have a list (or iterator) of tweets.


```python
for page in cursor.pages():
    for tweet in page:
        print(tweet.id)
```

Or you can use items approach, where Tweepy flattens multiple pages into what feels like one long list (or iterator).

```python
for tweet in cursor.items():
    print(tweet.id)
```

### Limit

The cursor will carry on it until it gets all available data. You can optionally limit this by omitting the limit.

In both examples below, we process 5 pages of `100` tweets each and get a total of 500 tweets.


```python
for tweet in cursor.items(500):
    print(tweet.id)
```

```python
for page in cursor.pages(5):
    for tweet in page:
        print(tweet.id)
```


## Get users
> Various approaches to get profiles of Twitter users

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

?> **Tweepy docs**: [API.get_user](http://docs.tweepy.org/en/v3.8.0/api.html#API.get_user)


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


### Lookup user ID for a screen name


```python
user = api.get_user(screen_name='foo')
```

Get ID as an `int`. You will probably fine with this in most cases.

```python
user_id = user.id
# 1234567
```

Get ID as a `str`. You probably don't need this.

```python
user_id = user.id_str
# "1234567"
```

#### Lookup many profiles

Lookup one or more users by screen name.

```python
screen_names = ["foo", "bar", "baz"]
users = api.lookup_users(screen_names=screen_names)
```

Lookup one or more users by ID.

```python
user_ids = [123, 456, 789]
users = api.lookup_users(user_ids=user_ids)
```

?> **Tweepy docs**: [API.lookup_users](http://docs.tweepy.org/en/latest/api.html#API.lookup_users)

?> The endpoint only lets you request up to 100 IDs at once, so you'll never than more than one page of results. Therefore you get more results, you should batch your IDs into groups of 100 and then lookup each group.

### Search for user

```python
users = api.search_users(q, count=20)
```

The count argument may not be greater than 20 according to Tweepy docs, but you may use paging.

?> **Tweepy docs**: [API.search_users](http://docs.tweepy.org/en/latest/api.html#API.search_users)


## Get followers of a user


### Followers method

Get the followers of a given user.

- [api.followers](http://docs.tweepy.org/en/latest/api.html#API.followers)
    > Returns a user’s followers ordered in which they were added. If no user is specified by id/screen name, it defaults to the authenticated user.
- Specify user ID or screen name.
- Supports paging.
- Returns a list of `tweepy.User` objects.

```python
for user in api.followers(screen_name="foo"):
    print(user.screen_name)
```

### Follower IDs method

Similar to above, but only returns user IDs and not users.

- [api.followers_ids](http://docs.tweepy.org/en/latest/api.html#API.followers_ids)
    > Returns an array containing the IDs of users following the specified user.
- Specify user ID or screen name.
- Supports paging.
- Return a list of `int` objects.

 This can be useful if you want to map user IDs to user IDs in a graph of followers and maybe combined with tweet IDs, without actually using the profile data like screen name.

```python
for user_id in api.followers(screen_name="foo"):
    print(user_id)
```

With paging:

```python
cursor = tweepy.Cursor(
    api.followers,
    screen_name="foo",
    count=100
)
user_id_pages = list(cursor.pages())
```

You can combine this approach with [Lookup users](#lookup-many-profiles) method, to lookup a batch users with known IDs or screen names.

```python
cursor = tweepy.Cursor(
    api.lookup_users,
    user_ids=user_id_pages,
    count=100
)
```

?> You will have to split the user IDs into batches of at most 100 items so that the query will work. Here we use pages from above so it will already be batched.

?> This uses two steps to get IDs and the users, so consider the rate limit impact for the first and second step.

### Rate limits on follower approaches

See [Rate Limits on Twitter Policies](policies.md#rate-limits) page details.

If you want to see which approach works better for you at scale, see these references from people who have done research:

[Tweepy issue 627](https://github.com/tweepy/tweepy/issues/627)


| API            | Max Return/Call Size | Requests / 15-min window | Total Results Per Window |
| -------------- | -------------------- | ------------------------ | ------------------------ |
| followers/list | 200                  | 15                       | 3000                     |
| followers/ids  | 5000                 | 15                       | 75000                    |
| users/lookup   | 100                  | 180                      | 18000                    |


[StackOverflow](https://stackoverflow.com/questions/31000178/how-to-get-large-list-of-followers-tweepy)

<details>
<summary><b>Twitter provides two ways to fetch the followers</b></summary>

> Fetching full followers list (using followers/list in Twitter API or api.followers in tweepy) - Alec and mataxu have provided the approach to fetch using this way in their answers. The rate limit with this is you can get at most 200 * 15 = 3000 followers in every 15 minutes window.
>
> Second approach involves two stages:-
>
> a) Fetching only the followers ids first (using followers/ids in Twitter API or api.followers_ids in tweepy).you can get 5000 * 15 = 75K follower ids in each 15 minutes window.
>
> b) Looking up their usernames or other data (using users/lookup in twitter api or api.lookup_users in tweepy). This has rate limitation of about 100 * 180 = 18K lookups each 15 minute window.
>
> Considering the rate limits, Second approach gives followers data 6 times faster when compared to first approach.

</details>


## Get tweets

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

?> **Tweepy docs**: [API.home_timeline](http://docs.tweepy.org/en/latest/api.html#API.home_timeline)


### Get a user's timeline

Get the most recent by a user. You can specify `user_id` or `screen_name` to target a user.

```python
screen_name = "foo"
tweets = api.user_timeline(screen_name=screen_name)
```

If you don't specify a user, the default behavior is for the authenticated user.

```python
tweets = api.user_timeline()
```

The API doesn't say what the default is but the max without paging is  `200`.

```python
tweets = api.user_timeline(count=200)
```

?> **Tweepy docs**: [API.user_timeline](http://docs.tweepy.org/en/latest/api.html#API.user_timeline) <br>**Twitter API docs:** [GET statuses/user_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline) - note daily limit of 100k tweets and getting 3,200 most recent tweets, otherwise there is not really a date restriction on how many days or years you can go back to.


#### Fuller examples

Get `200` tweets of user.

?> See [Extended message](#extended-message) section regarding the Tweet mode parameter.

```python
screen_name = "foo"
tweets = api.user_timeline(
    screen_name=screen_name,
    count=200,
    tweet_mode="extended",
)

for tweet in tweets:
    try:
        print(tweet.full_text)
    except AttributeError:
        print(tweet.text)
```

Using paging to get `1000` tweets - `3200` is the max for a timeline.

```python
screen_name = "foo"
cursor = tweepy.Cursor(
    api.user_timeline,
    screen_name=screen_name,
    count=200,
    tweet_mode="extended",
)

for tweet in cursor.items(1000):
    try:
        print(tweet.full_text)
    except AttributeError:
        print(tweet.text)
```


#### Get expanded message on a user's retweets

Note that even though we use _extended_ mode to show expanded rather than truncated tweets, the message of a **retweet** will still be **truncated**. So you can this approach to get the full message on the _original_ tweet.

Example from [source](https://stackoverflow.com/questions/42705314/getting-full-tweet-text-from-user-timeline-with-tweepy).

```python
tweets = api.user_timeline(id=2271808427, tweet_mode="extended")

# This is still truncated.
tweets[6].full_text
# => 'RT @blawson_lcsw: So proud of these amazing @HSESchools students who presented their ideas on how to help their peers manage stress in mean…'

# Original expanded text.
tweets[6].retweeted_status.full_text
# => 'So proud of these amazing @HSESchools students who presented their ideas on how to help their peers manage stress in meaningful ways! Thanks @HSEPrincipal for giving us your time!'
```

?> **Tweepy docs:** [Handling Retweets](http://docs.tweepy.org/en/latest/extended_tweets.html#handling-retweets) in Extended Tweets guide.


### Fetch tweets by ID

If you know the ID of a tweet, you can fetch it. This is useful if you want to find the latest engagements count on a tweet, or if you have a list of just IDs from outside Tweepy and you want to turn them into Tweepy objects so you can get the message, author, date, etc.

#### Lookup a single tweet

```python
tweet_id = 123
api.get_status(tweet_id)
```

?> **Tweepy docs**: [API.get_status](http://docs.tweepy.org/en/latest/api.html#API.get_status)


#### Lookup many tweets

```python
tweet_ids = [123, 456, 789]
api.statuses_lookup(tweet_ids)
```

?> **Tweepy docs**: [API.statuses_lookup](http://docs.tweepy.org/en/latest/api.html#API.statuses_lookup)


### Get retweets of a tweet

Get up to 100 retweets on a given tweet.

```python
tweet_id = 123
count = 100
retweets = api.retweets(tweet_id, count)
```

?> **Tweepy docs**: [API.retweets](http://docs.tweepy.org/en/latest/api.html#API.retweets)

See also:

```python
retweets = tweet.retweets
```

### Get the target of a reply

Get original tweet on the current tweet, if it has one.

```python
original_tweet_id = tweet.in_reply_to_status_id

if original_tweet_id is not None:
    original_tweet = api.get_status(original_tweet_id)
```

Get user who was the target of the reply.

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

Get a list of retweets of the tweet. This has a max of 100 but supports paging.

```python
api.retweets(tweet.id)

# Untested
retweets = tweet.retweets()
```


### Get retweeters

Get the user IDs of the users who retweeted the tweet. This has a max of 100 but supports paging.

```python
# Untested
retweeters = tweet.retweeters
```

## Filter tweets by language

Twitter assigns a tweet a language e.g. `en` for English or `it` for Italian.

?> **Twitter dev docs:** [Supported languages](https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview)

?> **Twitter API docs:** [Get Supported Languages](https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages) endpoint. There is some sample output there. 


### Where does it come from?

These are based on the **content** of the tweet and is inferred.

Tweepy docs say "Language detection is best-effort.".

!> **Warning:** In my experience is **not** reliable in my experience. Tweets appear as unknown language, or a user making several tweets which I can see are all in one language get labelled as different language. If you still want to use language, you can continue.


### What about the settings of the user?

There is **no** account setting to change what language you are posting in.

There is a *Display Language* setting in Twitter account settings, but this how the interface appears to you. The help text for the item explain that is does not affect the content of Tweets.

?> See the [Search API](#search-api) section on this page for more details how on to do searches.

### Show the language

```python
tweets = api.search("python")

for tweet in tweets:
    print(tweet.lang, tweet.text)
   if tweet.lang == "en":
      print(tweet.text)
```

### Filter on the result

```python
tweets = api.search("python")

for tweet in tweets:
    if tweet.lang == 'en':
      print(tweet.text)
```


### Filter query

Some endpoints let you specify languages so that only matching tweets will be returned.

#### Search filtered by language

From the [api.search](http://docs.tweepy.org/en/latest/api.html#API.search) docs:

> **lang** – Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.

e.g.

```python
tweets = api.search("python", lang="en")
```

#### Streaming filtered by language

Note use of `languages`, not `lang`.

e.g.

```python
stream.filter(track=["python"], languages=["en"])
```


## Get replies to a tweet

The only way to get replies to a tweet is using the [Search API](#search-api), which means you can only get replies which happened in the past week.

This approach gets all replies to a user with screen name `foo`. You can replace the handle with your own.

```
to:foo filter:replies
```

That can be tested into browser.

Here is how to do it with Tweepy.

```python
screen_name
query = "to:{} filter:replies".format(screen_name)
tweets = api.search(query)
```

To get replies to a specify tweet, you'll have to check the `tweet.in_reply_to_status_id` attribute for a match on the current ID.

This can be further optimized by specifying a condition in the search which only shows tweets _after_ the target tweet ID, but if you're iterating back from most recent tweets the way Twitter does then it only helps a bit.

You'll also have to apply recursive logic to get replies to replies.


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

?> **Tweepy docs:** [API.update_with_media](http://docs.tweepy.org/en/latest/api.html#API.update_with_media).

!> Note that this method does work, but the docs says this is deprecated. The preferred approach is to use `api.upload_media` and then attach the return ID as part of the `media_ids` list parameter on the `api.update_status` method covered above.


## Handle time values


### Date and time

The Twitter API often provides a datetime value in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format and Tweepy returns this to you as a string still.

e.g. `"2020-05-03T18:01:41+00:00"`.

This section covers how to parse a datetime string to a timezone-aware datetime object, to make it more useful for calculations and representations.

```python
import datetime


TIME_FORMAT_IN = r"%Y-%m-%dT%H:%M%z"


def parse_datetime(value):
    """
    Convert from Twitter datetime string to a datetime object.

    >>> parse_datetime("2020-01-24T08:37:37+00:00")
    datetime.datetime(2020, 1, 24, 8, 37, tzinfo=datetime.timezone.utc)
    """
    dt = ":".join(value.split(":", 2)[:2])
    tz = value[-6:]
    clean_value = f"{dt}{tz}"

    return datetime.datetime.strptime(clean_value, TIME_FORMAT_IN)
```

?> When splitting, we don't need seconds and any decimals (plus these have changed style before between API versions so are unreliable). So we just ignore after the 2nd colon (minutes) and pick up the timezone from the last 6 characters.

?> The datetime value from Twitter will be always be UTC zone (GMT+00:00), regardless of your location or profile settings. Lookup the datetime docs for more info.

Example usage:

```python
>>> dt = parse_datetime(tweet.created_at)
>>> print(dt.year)
2020
```

### Timestamp

If you get any numbers which are timestamps such as from the Rate Limit endpoint, you can convert them to datetime objects.

```python
import datetime


timestamp = "1403602426"
datetime.datetime.fromtimestamp(float(timestamp))
# => datetime.datetime(2014, 6, 24, 11, 33, 46)
```


## Search API

The Twitter Search API lets you get tweets made in the past 7 to 10 days. The approaches below take you from getting 20 tweets to thousands of tweets.

?> If you want a live stream of tweets, see the [Streaming](#streaming) section.

?> If you want to go back more than a week and are willing to pay, see the [Batch historical tweets](https://developer.twitter.com/en/docs/tweets/batch-historical/overview) API docs.

### Query syntax

Twitter has a flexible search syntax for using "and" / "or" logic and quoting phrases.

Twitter API docs on search.

- [Overview of standard operators](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/overview/standard-operators).
- [Guide to build standard queries](https://developer.twitter.com/en/docs/tweets/rules-and-filtering/guides/build-standard-queries).

?> Be sure to use the _standard_ docs as the _premium_ operators do not work on the free search services.

?> You can test a search query out in the Twitter search bar before trying it in the API.


### Search query examples


#### Basic

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
- Exact match on phrase. i.e. all words must be used and in order.
    - `foo bar`
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


#### Advanced

See the links in [Query syntax](#query-syntax) section for more details.

Query | Description
---   | ---
`to:some_handle` | Mentions of user `@some_handle`.
`filter:retweets #bar` | Retweets only about `#bar`.
`-filter:retweets #bar` | Exclude retweets about `#bar`.
`filter:replies #bar` | Replies only about `#bar`.
`to:some_handle filter:replies` | Replies to `@some_handle`.



### Tweepy search method


?> **Tweepy docs:** [API.search](http://docs.tweepy.org/en/latest/api.html#API.search) - that section explains how it works and what the method parameters do. <br>**Twitter API docs:** [Standard search API](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets)


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
- An exact match phrase in quotes - just change the outside to single quotes.
    ```python
    query = '"foo bar"'
    ```


#### Basic

Return tweets for a search query. Only gives 20 tweets by default, so read on to get more.

```python
tweets = api.search(query)
```

Or use `q` explicitly, for the same result.

```python
tweets = api.search(q=query)
```


Example of iterating over the results in `tweets` object:

```python
def process_tweet(tweet):
    print(tweet.id, tweet.author, tweet.text)


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

!> Twitter API imposes **rate limiting** against a token, to prevent abuse. So, after you've met your quota of searches in a 15-minute window (whether new searches or paging on one search), you will have have to **wait** until it resets and then do more queries. Any requests before then will fail (though other will have their own limit). This **waiting** can be turned on as a config option on setting up the `auth` object, as covered in [Installation](installation.md) section.

```python
cursor = tweepy.Cursor(
    api.search,
    query,
    count=100
)
```

```python
for tweet in cursor.items():
    process_tweet(tweet)
```

See [Paging](#paging) section for more info.



#### Extended message

You can choose to set `tweet_mode` to `extended`.

- This will give messages that are not truncated (with an ellipsis at the end).
- Note that retweets messages might _still_ be truncated even with this option.

When using this option, make sure to use the `tweet.full_text` attribute and not `tweet.text`. But still allow fallback to plain `tweet.text`. Since the Tweepy docs say:

> If status is a Retweet, it will not have an extended_tweet attribute, and status.text could be truncated.


```python
tweets = api.search(
    query,
    tweet_mode="extended",
)
```

```python
for tweet in tweets.items():
    try:
        print(tweet.full_text)
    except AttributeError:
        print(tweet.text)
```

?> **Tweepy docs:** [Extended mode](http://docs.tweepy.org/en/latest/extended_tweets.html)


#### Result type

Set `result_type` to one of the following, according to Twitter API:

- `mixed` - A balance of the other two. Default option.
- `recent` - The tweets that are the most recent.
- `popular`- The tweets with the highest engagements. Note that this list might be very short (just a few tweets) - compared with running the `recent` query.

```python
result_type = "popular"
count = 100

tweets = api.search(
    query,
    count=count,
    result_type=result_type
)
```

#### Limit date range

You can specify that the tweets should be up to a date. If you don't care about tweets in the last few days or you already stored them, this can be useful to go back further.

Add `until` as a parameter with year, month, date formatted date as a string.

e.g. 

```python
api.search(
    q=query, 
    until="2020-05-07"
)
```

?> You are still bound by the search API's limit of one week, so if you set until to be a week ago you'll get close to zero tweets.

#### Filter by location 

Search for tweets at a point within a radius. 

?> You can leave the search query parameter `q` unset and this will still work.

Format of geocode value:

```
LATITUDE,LONGITUDE,RADIUS
```

Example usage:

```python
api.search(geocode="33.333,12.345,10km")

api.search(geocode="37.781157,-122.398720 ,mi") 	
```

?> **Twitter API reference:** [Standard Search API](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets) - see `geocode` unde _Parameters_.

> Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile.
>
> The parameter value is specified by `latitude,longitude,radius`, where radius units must be specified as either `mi` (miles) or `km` (kilometers).
>
> Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly.
>
> A maximum of 1,000 distinct "sub-regions" will be considered when using the radius modifier.


## Get entities on tweets

### Get media

How to get images on tweets.

?> This example is for the [Search API](#search-api) but can work for other methods too such as [User timeline](#get-a-user39s-timeline).


Add entities to your request - this may not always be needed on some endpoints such as `.search` where the default is `True`. Check the Tweepy docs.

Then use the media value, if one exists on a tweet's entities.

```python
cursor = tweepy.Cursor(
    api.search,
    query,
    count=count,
    include_entities=True,
)

for tweet in cursor:
    if 'media' in tweet.entities:
        for image in tweet.entities['media']:
            print(image['media_url'])
```


## Streaming

This section focuses on the standard and free "filtered" Streaming API service. There are more services available, covered in the [Other streams](#other-streams) subsection.


### What is streaming and how many tweets can I get?

The [Search API](#search-api) gives about 90% of tweets and back 7 days, but you have to query it repeatedly if you want "live" data and this can result in reaching API limits.

The filtered streaming API lets you connect to the firehose of Twitter tweets made in realtime. You must specify a filter to apply - either keywords or users to track.

However, the volume is much lower than the search API.

> Studies have estimated that using Twitter’s Streaming API users can expect to receive anywhere from 1% of the tweets to over 40% of tweets in near real-time.
>
> The reason that you do not receive all of the tweets from the Twitter Streaming API is simply because Twitter doesn’t have the current infrastructure to support it, nor do they don’t want to support it; hence, the Twitter Firehose. [source](https://brightplanet.com/2013/06/25/twitter-firehose-vs-twitter-api-whats-the-difference-and-why-should-you-care/)


### Streaming resources


#### Tweepy

- [Streaming tutorial](http://docs.tweepy.org/en/latest/streaming_how_to.html) in the docs.
- [streaming.py](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py) module in the repo. This is useful to find or override existing methods.
    - See [StreamListener](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L30) class.
    - See [Stream](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L209) class and [Stream.filter](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L451-L474) method.
- [streaming.py](https://github.com/tweepy/tweepy/blob/master/examples/streaming.py) example script in the repo.
- [test_streaming.py](https://github.com/tweepy/tweepy/blob/master/tests/test_streaming.py) - Python tests for `streaming` module.


#### Twitter API docs

- [Filter realtime Tweets](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter)
    - Make sure to use "POST statuses/filter" as the other endpoints are premium only.
    - Note deprecation warning:
        > This endpoint will be deprecated in favor of the filtered stream endpoint, now available in Twitter Developer Labs.
- [POST statuses/filter](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter) endpoint reference
    - Including URL and response structure.
    - Including allowed parameters.
- [Basic stream parameters](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters)
    - Covers parameters in more detail.
    - `filter_level`
        - The default value is `none`, which is all available tweets. If you don't need all tweets or performance is an issue, you can set this to `low` or `medium`.
    - `language`
        - You can this to a standard code like `en`. However, when using the Search API I found the labels were inconsistent even on several tweets from the same person. Twitter guesses the language, it doesn't use your settings.
- [Premium stream operators](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/premium-operators)


### Setup stream listener class

Create a class which inherits from [StreamListener](https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/streaming.py#L30).

Most of the methods just return, so you will need to override methods to handle statuses and errors.

?> There are a couple of errors which can happen so they are not handled here - see the original class linked above for what methods there are or see the examples at the end of this section.


```python
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
```

?> Some people name this class as `_StdOutListener`.


### Setup stream instance

```python
myStreamListener = MyStreamListener()
stream = tweepy.Stream(auth=auth, listener=myStreamListener)
```

Some people do this in one line instead:

```python
stream = tweepy.Stream(auth=auth, listener=MyStreamListener())
```

### Start streaming

Follow the sections below to start streaming with the `stream` object.

?> Only the `.filter` method is covered here as that is accessible without a premium account.


#### Follow tweets by users

Stream public tweets by one or more users. This includes tweets and retweets created and replies to the user, but not mentions of the user.

First get the user IDs of one or more Twitter users to follow.

?> Make sure you specify **user IDs** and not screen names. If you need to, see the instructions on how to [Lookup user ID for a screen name](#lookup-user-id-for-a-screen-name).

Then pass the **follow** parameter using a `list` of strings.

e.g.

```python
user_ids = ["1234567", "456789", "9876543"]

stream.filter(follow=user_ids)
```

?> **Twitter API docs**: [Basic stream parameters](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) (see **follow** section).


#### Follow tweets matching keywords

Use the **track** parameter and one or more terms, like keywords or hashtags or URLs.

Example:

```python
track = ["foo", "#bar", "fizz buzz"]

stream.filter(track=track)
```

- OR
    - The Twitter API will look for a tweet which contains *any* (i.e. _at least one_) of the items in the list, so it uses `OR` logic.
- AND
    - Use a *space between words* to use `AND` logic. e.g. `"fizz buzz"`.


!> You **cannot** use quoted phrases. The API doc says: "Exact matching of phrases (equivalent to quoted phrases in most search engines) is not supported.".

?> The docs say you can track a URL but recommends including a space between parts for the most inclusive search. `"example com"`.

?> UTF-8 characters are supported but must be used explicitly in your search. e.g. `'touché'`, `'Twitter’s'`.

?> **Twitter API docs**: [Basic stream parameters](https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/basic-stream-parameters) (see **track** section).


#### Full stream examples

<details>
<summary><b>tweepy_docs_example.py</b></summary>

[tweepy_docs_example.py](_scripts/streaming/tweepy_docs_example.py ':include :type=code')

</details>

<details>
<summary><b>tweepy_example_repo_example.py</b></summary>

[tweepy_example_repo_example.py](_scripts/streaming/tweepy_example_repo_example.py ':include :type=code')

</details>


### Update stream

If you want to update a stream, you must **stop** it and then **start** a new stream, according to this [Twitter dev page](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview).

> One filter rule on one allowed connection, disconnection required to adjust rule.

!> This also means you are **not** allowed to have more than one streaming running at a time for account, not in the same script, same machine or even on another machine.

One way is to stop your application, reconfigure it and then start it again.

If you want to keep the script running, you can restart like this:


```python
track = ["foo"]
# Start initial stream.
stream.filter(track=track, is_async=True)

time.sleep(5)

# Update. This won't get applied yet.
track.append("bar")

# Stop.
stream.running = False

# Start again.
stream.filter(track=track, is_async=True)
```

The gap will hopefully be very short so you don't lose much.


### How do I stream faster?

The streaming API is meant to be realtime but you have still experience a delay. In one case I heard that posting a tweet was delayed in the streaming up by 5 seconds, which I'd say is still good.

This delay might just be built into the way the Twitter API works.

Here are some ideas to improve performance when streaming:

- The obvious ones - improve your internet connection speed or improve your hardware. Use a remote machine through AWS to "rent" a machine in the cloud dedicated to your application. Besides choosing higher specs than your local machine, it can also be online and run 24/7.
- Run your script in _unbuffered_ mode. Rather than waiting until the console output meets a threshold, tell Python to print immediately.
    - e.g.
        ```sh
        python -U script.py
        ```
- If you performance bottleneck is processing the tweet locally (writing to CSV or database), you can make that task asynchronous by using RabbitMQ or similar.
    - This may not improve the delay, but it will make sure your application can process every tweet that Twitter Streaming API sends at you and that you don't get disconnected (which can happen if Twitter Streaming API decides you are handling the offloaded tweets to slowly).
    - Example of repo which does this (though it's archived, so it's not maintained and might not work).
        - [ukgovdatascience/twitter-mq-feed](https://github.com/ukgovdatascience/twitter-mq-feed)
        > A script that gets data from the Twitter real-time API, passes it to a message-queue (e.g. RabbitMQ) and stores tweets into MongoDB
- If using the premium streaming API, use an advanced filter.


### Other streams


#### Decahose

Enterprise stream to get 10% of tweets.


?> **Twitter docs:** [Decahose API reference](https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/decahose)


#### Powertrack

Enterprise stream to get 100% of tweets.

> The PowerTrack API provides customers with the ability to filter the full Twitter firehose, and only receive the data that they or their customers are interested in.

?> **Twitter docs:** [Powertrack API reference](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview/powertrack-api)


#### Lab streams

Experimental Twitter API endpoints.

- [Labs V2 Overview](https://developer.twitter.com/en/docs/labs/overview/introduction)
- [Sample stream v1](https://developer.twitter.com/en/docs/labs/sampled-stream/overview) (replaces [Sample realtime tweets](https://developer.twitter.com/en/docs/tweets/sample-realtime/overview/get_statuses_sample) endpoint)
    > The sampled stream endpoint allows developers to stream about 1% of all new public Tweets as they happen. You can connect no more than one client per session, and can disconnect and reconnect no more than 50 times per 15 minute window.
- [Filtered stream v1](https://developer.twitter.com/en/docs/labs/filtered-stream/overview)
    > The filtered stream endpoints allow developers to filter the real-time stream of public Tweets. Developers can filter the real-time stream by applying a set of rules (specified using a combination of operators), and they can select the response format on connection.
    >
    > This preview contains a streaming endpoint that delivers Tweets in real-time. It also contains a set of rules endpoints to create, delete and dry-run rule changes. During Labs, you can create up to 10 rules (each one up to 512 characters long) can be set on your stream at the same time. Unlike the existing statuses/filter endpoint, these rules are retained and are not specified at connection time.
- [COVID-19 stream](https://developer.twitter.com/en/docs/labs/covid19-stream/overview)


## How do I store tweets?

You can easily write to a CSV file using the Python `csv` module.


Here are some options for storing in a database.

- [Twitter MQ feed](https://github.com/ukgovdatascience/twitter-mq-feed) - this project stores in MongoDB.
- [Streaming Twitter Data into a MySQL Database](https://towardsdatascience.com/streaming-twitter-data-into-a-mysql-database-d62a02b050d6)


### SQLite

<details>
<summary><b>Demo script using SQLite</b></summary>

[SQLite3 demo](//gist.githubusercontent.com/MichaelCurrin/8105070b9e580342c380a9c42f1d97e1/raw/python_sqlite_demo.py ':include :type=code')

</details>


## Direct messages

Methods relating to Twitter account direct messages.

!> Please ensure you comply with the Twitter API policies and do not spam users. See [Twitter policies](policies.md) page to find links to appropriate docs.

?> **Tweepy docs:** [Direct message methods](http://docs.tweepy.org/en/latest/api.html#direct-message-methods)


Twitter API docs:

- [Sending and receiving events overview](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/overview)
    > *Receiving messages events*
    >
    > You can retrieve Direct Messages from up to the past **30** days with GET direct_messages/events/list.
    >
    > Consuming Direct Messages in **real-time** can be accomplished via webhooks with the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview).


### List messages

Get direct messages to the authenticated Twitter account (such as your bot) in the last **30** days.

```python
dms = api.list_direct_messages()
```

The default value for count is `20` and this can be increased to `50`.

If you need to get more than that, using paging.

```python
tweepy.Cursor(api.direct_messages, count=50).items(200)
```

?> **Twitter API docs:** [List messages endpoint](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events)


### Get message

Fetch a message by known ID.

```python
dm_id = dms[0].id
dm = api.get_direct_message(dm_id)
```

?> **Twitter API docs:** [Show message endpoint](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/get-event)


### Get attributes on a message object

- Get the text of a message.
    ```python
    dm.message_create['message_data']['text'])
    ```
- Get recipient user ID:
    ```python
    dm.message_create['target']['recipient_id']
    ```

See the [Direct message](models.md#direct-message) section on the Models page to see a preview of the full structure.

### Show all data

Print the entire object, prettified with the `json` builtin library.

```python
import json
print(json.dumps(dm.message_create, indent=4))
```


### Filter to messages from a certain user

```python
user_id = "12345"

filtered_dms = [dm for dm in dms if msg.message_create['target']['recipient_id'] == user_id
```

?> We use a list comprehension here with an `if` condition, as it is has faster performance than a standard `for` loop and also it can be more readable (since it fits on one line and there's no `.append` step needed).

?> If don't have a user ID, then [Lookup user ID for a screen name](#lookup-user-id-for-a-screen-name).

Here's a more complete example:

```python
dms = api.list_direct_messages()

screen_name = "foo"
user_id = api.get_user(screen_name).id

for dm in dms:
    if dm.message_create['target']['recipient_id'] == str(user_id):
        print(dm.message_create['message_data']['text'])
```

### Send message

Send a direct message to given user ID.

```python
user_id = "123"
msg = "Hello, world!

api.send_direct_message(user_id, msg)
```

?> If don't have a user ID, then [Lookup user ID for a screen name](#lookup-user-id-for-a-screen-name).

?> **Twitter API doc:** [Create message endpoint](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) - see optional parameters like `quick_reply` and `attachment`.


## Get rate limit status


Twitter provides an endpoint to get the rate limit status for your token across all endpoints at once.

```python
data = api.rate_limit_status()
```

The response is a `dict` which you can lookup like this:

```python
data['resources']['statuses']['/statuses/home_timeline']
data['resources']['users']['/users/lookup']
```

See more on the [Rate limit status](models#rate-limit-status) section of the models page.

?> **Twitter API docs:** [Get app rate limit status](https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status)

?> There is also a way to get the rate limit stats on the response object on a successful call, though this is not covered here.
