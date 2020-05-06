# Resources
> Links to external docs for reference and some recommended tools


## Twitter dev docs

- [Twitter Developer docs](https://developer.twitter.com/en/docs) home
- [API Reference](https://developer.twitter.com/en/docs/api-reference-index)
- [Getting Started](https://developer.twitter.com/en/docs/basics/getting-started)
- [Twitter apps (https://developer.twitter.com/en/apps)](https://developer.twitter.com/en/apps) page to manage your dev account's apps once you login
- [Twitter libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries) recommended by Twitter, across programming languages


## Twitter libraries

See below for mostly Python libraries for interacting with the Twitter API. 

### Tweepy links

Tweepy is a Python library which is a wrapper on the Twitter API - you don't have to worry about writing URLs, handling auth, parsing data, paging and other complex tasks. The library can be used an abstract so you can fetch data and deal with it as Python objects and you can pass data to the API to perform actions like searches or post a status or retweet a status.

- [tweepy.org](https://www.tweepy.org/) homepage
- Tweepy docs
    - [Docs homepage](http://docs.tweepy.org/en/latest/)
        - This page is especially useful as a high-level view of the API method groups under _API Reference_ bullet point.
        - Redirects from [Tweepy Read the Docs](http://tweepy.readthedocs.org/)
    - [API Reference](http://docs.tweepy.org/en/latest/api.html)
        - Shows you what methods are available on the `api` object and what parameters they take.
        - Sometimes the methods on `API` can be used more conveniently on an object e.g. `API.retweet(tweet.id)` can be replaced with `tweet.retweet()`.
- Github repo
    - [tweepy/tweepy](https://github.com/tweepy/tweepy) repo on Github.
    - Highlights
        - [api.py](https://github.com/tweepy/tweepy/blob/master/tweepy/api.py)
        - [models.py](https://github.com/tweepy/tweepy/blob/master/tweepy/models.py)
        - [streaming.py](https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py)
        - [auth.py](https://github.com/tweepy/tweepy/blob/master/tweepy/auth.py)
        - [test_api.py](https://github.com/tweepy/tweepy/blob/master/tests/test_api.py) (useful to see how a method is used for the internal Tweepy tests)
- [Tweepy Discord channel](https://discord.gg/bJvqnhg)


As an alternative to Tweepy, use one of these below. You'll have to install one and configure it with API credentials, then you can do API requests.


### Twurl command-line tool

- Repo: [twitter/twurl](https://github.com/twitter/twurl)
- Command-line tool created by Twitter, like `curl` for request the Twitter API.
- Written in Ruby, but you can still use it in your command-line without knowing Ruby.
- Twitter docs includes a demo using `twurl` on their [homepage](https://developer.twitter.com/en).


### Python Twitter API wrapper libraries

- [twython](https://twython.readthedocs.io/en/latest/)
- [python-twitter](https://python-twitter.readthedocs.io/en/latest/)
- [Twitter libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries) section of Twitter docs - see Python section under Community libraries.

### Python utility scripts and repos

- [gmellini/twitter-scraper](https://github.com/gmellini/twitter-scraper)
    - Get replies using Twitter Search API.

!> Any searches will have the **one-week** limitation if doing a search for say hashtags or replies to a tweet. This limit is at the Twitter Search API level.
