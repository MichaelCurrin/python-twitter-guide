# Python Twitter Guide
> Code snippets and links to docs around using Twitter API and Tweepy

[![Made with Docsify](https://img.shields.io/badge/Made%20with-Docsify-blue.svg)](https://docsify.js.org/)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-twitter-guide.svg)](https://GitHub.com/MichaelCurrin/python-twitter-guide/tags/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/MichaelCurrin/python-twitter-guide/blob/master/README.md#license)


## Features

- Unofficial guide
- Aimed at Python developers learning to use _tweepy_
- Code snippets are provided for some common use-cases
- Links to tweepy docs and Twitter API docs are provided
- Links to Twitter policies are provided to encourage fair API usage

?> This site is expanding and work in progress. I'll be chipping away at adding new sections like streaming, replies, trends, API policies. And available attributes on tweets and users. If you want to see something added, message me directly on Tweepy discord or add a Github issue (or comment on an existing issue). I'll aim to do it in a day.

## About
> How to use this guide and why it exists

The Tweepy docs do cover how the library works on the API page, but examples of how to use the library are limited.

Also, the Tweepy library aims to be a _thin layer_ between your code and the Twitter API, so Tweepy does not always make it clear what values are valid in requests. This puts more burden on the developer to figuring things out by looking at both.

So this website aims at making Tweepy and Twitter API easier to use. With additional support by linking to docs and Twitter policies.

Note that is guide was written main for Linux and macOS systems, to some commands will not work on Windows (in particular any shell commands).


## Install Tweepy for your own projects

If you are new to Python or virtual environments, read through this guide for more background on the instructions below.

- [Setup a Python 3 virtual environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7)


### Install system dependencies

<!-- TODO: Link to Learn to Code project when links are updated -->

Install [Python 3](python.org/).


### Install Python packages

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


## Terms of use

Note that Tweepy and Twitter API are subject to change so this guide may not always be up to date.
If anything is inaccurate or not up to date, see the contributing guide in the repo and a submit a
Pull Request.

While a best effort is made to keep this guide accurate and reflect the APIs and policies at the
current time, this guide only provides recommendations and some useful info. _You_ are responsible
for ensuring that you use Twitter and the API fairly and that you understand how it works. By using
this guide, you take responsibility for your own actions and do not hold the contributors to this
guide responsible.
