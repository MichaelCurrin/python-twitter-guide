# Resources
> Links to external docs and tools


## Twitter dev docs

- [Twitter Developer docs](https://developer.twitter.com/en/docs) home
- [Twitter API Reference](https://developer.twitter.com/en/docs/api-reference-index)
- [Twitter apps](https://developer.twitter.com/en/apps) (manage your dev account apps)


## Tweepy links

Tweepy is a Python library which is a wrapper on the Twitter API - you don't have to worry about writing URLs, handling auth, parsing data, paging and other complex tasks. The library can be used an abstract so you can fetch data and deal with it as Python objects and you can pass data to the API to perform actions like searches or post a status or retweet a status.

- [tweepy.org](https://www.tweepy.org/) homepage
- [Tweepy docs](http://tweepy.readthedocs.org/)
- [Tweepy Discord channel](https://discord.gg/bJvqnhg)


## Other Twitter API tools

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
