# Resources
> Links to external docs for reference and some recommended tools


## Twitter dev docs

- [Twitter Developer docs](https://developer.twitter.com/en/docs) home
- [Twitter apps](https://developer.twitter.com/en/apps) page to manage your dev account's apps once you login
- [Twitter libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries) recommended by Twitter, across programming languages
- [API Reference](https://developer.twitter.com/en/docs/api-reference-index)

### Basics

- [Getting Started](https://developer.twitter.com/en/docs/basics/getting-started)
- [Things every developer should know](https://developer.twitter.com/en/docs/basics/things-every-developer-should-know)
- [Authentication](https://developer.twitter.com/en/docs/basics/authentication/overview)
- [Response codes](https://developer.twitter.com/en/docs/basics/response-codes) guide
    - Including _HTTP Status Codes_, _Error Messages_ and _Error Codes_.


## Twitter libraries

See below for mostly Python libraries for interacting with the Twitter API.

### Tweepy links

Tweepy is a Python library which is a wrapper on the Twitter API - you don't have to worry about writing URLs, handling auth, parsing data, paging and other complex tasks. The library can be used an abstract so you can fetch data and deal with it as Python objects and you can pass data to the API to perform actions like searches or post a status or retweet a status.

- [tweepy.org](https://www.tweepy.org/) homepage
- [Tweepy Discord](https://discord.gg/bJvqnhg)
    - Join here using a Discord account.
    - Ask your question in `#support` channel. 
    - Please check the Tweepy and Twitter docs and search Google / StackOverflow for answers to your question before asking on Discord.
- Tweepy docs
    - [docs.tweepy.org](https://docs.tweepy.org/en/latest/) homepage
        - This page is especially useful as a high-level view of the API method groups under _API Reference_ bullet point.
        - Redirects from [Tweepy Read the Docs](http://tweepy.readthedocs.org/)
    - [Tweepy API Reference](http://docs.tweepy.org/en/latest/api.html)
        - Shows you what methods are available on the `api` object and what parameters they take.
        - Sometimes the methods on `API` can be used more conveniently on an object e.g. `API.retweet(tweet.id)` can be replaced with `tweet.retweet()`.
    - Github repo
        - [![tweepy/tweepy](https://img.shields.io/github/stars/tweepy/tweepy?style=social)](https://github.com/tweepy/tweepy)
    - Highlights
        - [api.py](https://github.com/tweepy/tweepy/blob/master/tweepy/api.py)
        - [models.py](https://github.com/tweepy/tweepy/blob/master/tweepy/models.py)
        - [streaming.py](https://github.com/tweepy/tweepy/blob/master/tweepy/streaming.py)
        - [auth.py](https://github.com/tweepy/tweepy/blob/master/tweepy/auth.py)
        - [test_api.py](https://github.com/tweepy/tweepy/blob/master/tests/test_api.py) (useful to see how a method is used for the internal Tweepy tests)


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


## My Twitter projects

These are projects I created using Tweepy. They have different purposes and levels of complexity. Perhaps they can be of use as inspiration or implementation examples.

### Searching for tweets and trends

- Twitterverse
    - [MichaelCurrin/twitterverse](https://github.com/MichaelCurrin/twitterverse) on Github
    - [docs site](https://michaelcurrin.github.io/twitterverse/)
    - One of my oldest Python projects. It covers fetching of tweets, users, trends, country data and storing them in a SQLite database. Plus there is some dabbling in user auth flow and streaming.
    - However, the repo has become large and unwieldily. So I am limiting new development on it.
- Trends dashboard
    - [michaelcurrin.pythonanywhere.com/](https://michaelcurrin.pythonanywhere.com/)
    - Built on my Twitterverse repo, I run a nightly cron job to get trending data by town or country and store that in a database.
    - The content is shown on a web app, based on filters I chose.
    - Hosted for free, thanks the amazing [pythonanywhere.com](https://pythonanywhere.com/) service.
- Scroll and Scrape
    - [scroll-and-scrape](https://github.com/MichaelCurrin/scroll-and-scrape)
        > Store tweets from a Twitter search results, using browser scraping

### Bots that tweet

- Boris the Baby Bot
    - [MichaelCurrin/boris-the-babybot](https://github.com/MichaelCurrin/boris-the-babybot) on Github
    - [@boristhebabybot](https://twitter.com/boristhebabybot)
    - A bot account I made for a friend's book.
    - Boris tweets a message daily using a random combination of some messages, hashtags and emojis.
- Whoopi Goldbot
    - [@WhoopiGoldbot](https://twitter.com/WhoopiGoldbot)
    - A parody bot account I made for my friends' entertainment.
    - Whoopi tweets the gold price daily, with some Whoopi Goldberg quote and sometimes a photo or GIF.

