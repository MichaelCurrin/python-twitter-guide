# Browser scraping
> How to get Twitter data without the API

Some data like tweets older than a week is not possible to get through the Twitter API, at least on the free tier. This can be limiting when doing searches and getting replies.

Using browser scraping is an alternative, which uses a simulated browser to scroll the pages and scrape data, or use the frontend's API. This is not the main part of this guide and just an add-on.


## Browser scraping tools

### GetOldTweets3

- [Mottl/GetOldTweets3](https://github.com/Mottl/GetOldTweets3)
    > A Python 3 library and a corresponding command line utility for accessing old tweets
- e.g.
    ```sh
    GetOldTweets3 --querysearch "europe refugees" --maxtweets 10
    ```
- e.g.
    ```python
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
                                       .setSince("2015-05-01")\
                                       .setUntil("2015-09-30")\
                                       .setMaxTweets(1)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    print(tweet.text)
    ```

### tweet_scrapper

- [tweet_scrapper](https://pypi.org/project/tweetscrape/) on PyPI
    > Twitter's API is annoying to work with, and has lots of limitations — luckily their frontend (JavaScript) has it's own API, which I reverse–engineered. No API rate limits. No restrictions. Extremely fast.
- [5hirish/tweet_scrapper](https://github.com/5hirish/tweet_scrapper) on Github
- Features
    - Scrapes using `requests` library - no API calls or API auth and no browser driver
    - Lets you search hashtags, mentions, profiles and reply threads.
    - Supports infinite scroll.
    - Exports to a file.
- Use the CLI tool or Python code.
- For help and usage instructions, see
    - [README.md](https://github.com/5hirish/tweet_scrapper/blob/master/README.md)
    - [USAGE.md](https://github.com/5hirish/tweet_scrapper/blob/master/USAGE.md)
    - Command-line help
        ```sh
        python -m tweetscrape.twitter_scrape --help
        ```
    - [twitter_scrape.py](https://github.com/5hirish/tweet_scrapper/blob/master/tweetscrape/twitter_scrape.py) which builds the CLI options.


### Articles

- [How to Scrape Tweets From Twitter](https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1) on Towards Data Science
    > A quick introduction to two options for scraping tweets from Twitter using Python


## Browser scraping snippets

Tips for using browser scraping tools to get data as an alternative to using Tweepy and Twitter API, should you need it.

See [Browser scraping tools](#browser-scraping-tools) for links.

### Get replies

!> The library used here works well for small volumes but it had issues which might be bugs in the library such as not getting more than a small amount of replies and repeating replies.

#### Install

Preferably inside a new virtual environment. e.g.

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Install [tweet_scrapper](#tweet_scrapper).

```sh
pip install tweetscrape
```

#### Get replies on one tweet

The shell CLI does not support getting a thread of replies ("conversations" in the project), but we can use the Python code. Here is an example based on the repo's example, getting the threaded tweets on this tweet: [ewarren/status/1146132929065738246](https://twitter.com/ewarren/status/1146132929065738246?conversation_id=1146132929065738246).

```python
from tweetscrape.conversation_tweets import TweetScrapperConversation


tweets = TweetScrapperConversation(
    username="ewarren",
    parent_tweet_id=1146415363460141057,
    num_tweets=40,
    tweet_dump_path='twitter_conv.csv',
    tweet_dump_format='csv'
)
tweet_count, last_tweet_id, last_tweet_time, dump_path = tweets.get_thread_tweets(True)

print(tweet_count)
```

Sample data from the first row in the CSV (shown vertically for readability).

Field | Value
---   | ---
`id` | `1146416291848359937`
`type` | `tweet`
`time` | `1562161918000`
`author` | `YaronFishman`
`author_id` | `1142627097397145600`
`re_tweeter` |
`associated_tweet` | `1146415363460141057`
`text` | `Why does this exclude @marwilliamson?`
`links` | `[]`
`hashtags` | `[]`
`mentions` | `['@marwilliamson']`
`reply_count` | `7`
`favorite_count` | `23`
`retweet_count` | `1`

#### Get replies on many tweets

If you need to repeat that for multiple tweets, you could do something like the following:

```python
from tweetscrape.conversation_tweets import TweetScrapperConversation


targets = [
    {"username": "foo", "tweet_id": 123},
    {"username": "bar", "tweet_id": 456},
    # ...,
]
path = 'twitter_conv.csv'

for target in targets:
    print(target["username"], target["tweet_id"])

    tweets = TweetScrapperConversation(
        username=target["username"],
        parent_tweet_id=target["tweet_id"],
        num_tweets=1000,
        tweet_dump_path=path,
        tweet_dump_format='csv'
    )

    tweet_count, _, _, _ = tweets.get_thread_tweets(save_output=True)
    print(tweet_count)
```


## Terms of use

!> Please read this section to ensure you understand conditions for use of this guide and what policies to follow.


See the [Twitter Policies](policies.md) page for use of Twitter. Read on below for terms of use for this guide.


Note that Tweepy and Twitter API are subject to change, so this guide may not always be up to date or work with newer versions. If anything is inaccurate or not up to date, see the contributing guide in the repo and a submit a Pull Request.

While a best effort is made to keep this guide accurate and reflect the APIs and policies at the
current time, this guide only provides recommendations and some useful info.

This guide comes with **no warranty or guarantee**.

**You** are responsible for ensuring that you use Twitter and the API fairly and that you understand how it works. By using
this guide, you take responsibility for your own actions and do not hold the contributors to this
guide responsible.

Scraping a website or API is generally legal. Just make sure you are not abusing the servers, breaking Twitter's policies, trying to build a copy of Twitter or trying to sell the scraped data. I've seen services that sell Twitter data but I don't know if they are legal.

Note that there are limitations on how you present the data - you can provide details like tweet messages on your website but not the tweet IDs as well.
