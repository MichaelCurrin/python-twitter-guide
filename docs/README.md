# Python Twitter Guide
> Code snippets and links to docs around using Twitter API and Tweepy

[![Made with Docsify](https://img.shields.io/badge/Made_with-Docsify-blue.svg)](https://docsify.js.org/)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-twitter-guide.svg)](https://GitHub.com/MichaelCurrin/python-twitter-guide/tags/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/MichaelCurrin/python-twitter-guide/blob/master/README.md#license)


## Features

- Unofficial guide to [Tweepy](#tweepy)
- Aimed at Python developers who want to use the Twitter API to do automated tasks, like make a bot or download thousands of tweets
- Find practical solutions for common Tweepy / Twitter API use-cases. This makes up for lack of practical examples or recommendations in official docs of both.
- Content here is based on experience from various developers and docs, to save you having to research yourself


## Site overview

Section | Description
---     | ---
[Code snippets](code_snippets.md) | This starts with an intro for setting up Tweepy. Then some Python code snippets are provided for some common use-cases, to avoid having to look at Tweepy docs or Twitter API docs directly. Links to the original docs are provided in some cases.
[Models](models.md) | Some Tweepy models are covered, to explain the attributes and actions available for objects like tweets and users.
[Twitter Policies](policies.md) | Recommendations and links are provided in this section to help you ensure you use the Twitter API fairly. Especially if you plan to make a bot or want to perform bulk actions but don't your account to be blocked or your dev application to be rejected.

?> **🚧 Note:** This site is an expanding work in progress. I'll be chipping away at adding content around topics like streaming, replies, trends, API policies and available attributes on tweets and users. If you want to see something added, message me directly on Tweepy discord or create / comment on a Github issue [here](https://github.com/MichaelCurrin/python-twitter-guide/issues). I'll aim to do the simple additions within a day.


## About
> How to use this guide and why it exists

The Tweepy docs do cover how the library works on the API page, but examples of how to use the library are limited.

Also, the Tweepy library aims to be a _thin layer_ between your code and the Twitter API, so Tweepy does not always make it clear what values are valid in requests. This puts more burden on the developer to figuring things out by looking at both.

So this website aims at making Tweepy and Twitter API easier to use. With additional support by linking to docs and Twitter policies.

?> **Note** This was guide was written main for _Linux_ and _macOS_ systems, so some commands will need to be adjusted to use on Window. In particular any shell commands - Python commands are mostly standard.


## Resources

### Twitter docs

- Twitter developer docs
    - [Developer docs](https://developer.twitter.com/en/docs) home
    - [API Reference](https://developer.twitter.com/en/docs/api-reference-index)
    - [Twitter apps](https://developer.twitter.com/en/apps) (manage your dev account apps)
- Twitter docs
    - [Terms of service](https://twitter.com/en/tos)
    - [Rules and policies](https://help.twitter.com/en/rules-and-policies)
    - [Twitter automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) policy (this will help ensure you use the API fairly for tweeting, retweeting, searching, making a bot, etc.)


### Tweepy

Tweepy is a Python library which is a wrapper on the Twitter API - you don't have to worry about writing URLs, handling auth, parsing data, paging and other complex tasks. The library can be used an abstract so you can fetch data and deal with it as Python objects and you can pass data to the API to perform actions like searches or post a status or retweet a status.

- [tweepy.org homepage](https://www.tweepy.org/)
- [Tweepy docs](http://tweepy.readthedocs.org/)
- [Tweepy Discord](https://discord.gg/bJvqnhg) channel


### Other Twitter API tools

As an alternative to Tweepy, use one of these. You'll have to install one and configure it with API credentials, then you can do API requests.

- Command-line
    - [twurl](https://github.com/twitter/twurl)
        - Command-line tool, like `curl` for request the Twitter API. 
        - Written in Ruby, but you can still use it in your command-line without knowing Ruby.
        - Twitter docs includes a demo using `twurl` on their [homepage](https://developer.twitter.com/en).
- Python Twitter API wrapper libraries
    - [twython](https://twython.readthedocs.io/en/latest/)
    - [python-twitter](https://python-twitter.readthedocs.io/en/latest/)
- Python utility scripts and repos
    - [gmellini/twitter-scraper](https://github.com/gmellini/twitter-scraper)
        - Get replies using Twitter Search API.

!> Any searches will have the **one-week** limitation if doing a search for say hashtags or replies to a tweet. This limit is at the Twitter Search API level.


## Browser scraping tools

These using browsing scraping to avoid Twitter API limits.

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

Tips for using browser scraping tools to get data as an alternative to using Tweepy and Twitter API.

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


### Policies 

See [Twitter Policies](policies.md) page.


### Legal

Note that Tweepy and Twitter API are subject to change, so this guide may not always be up to date or work with newer versions. If anything is inaccurate or not up to date, see the contributing guide in the repo and a submit a Pull Request.

While a best effort is made to keep this guide accurate and reflect the APIs and policies at the
current time, this guide only provides recommendations and some useful info. 

This guide comes with **no warranty or guarantee**. 

**You** are responsible for ensuring that you use Twitter and the API fairly and that you understand how it works. By using
this guide, you take responsibility for your own actions and do not hold the contributors to this
guide responsible.

Scraping a website or API is generally legal. Just make sure you are not abusing the servers, breaking Twitter's policies, trying to build a copy of Twitter or trying to sell the scraped data. I've seen services that sell Twitter data but I don't know if they are legal.

Note that there are limitations on how you present the data - you can provide tweet messages on your website but not the tweet IDs.

_References and links to be confirmed and shown here_.
