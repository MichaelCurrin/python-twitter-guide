# Python Twitter Guide
> Code snippets and links to docs around using Twitter API and Tweepy

[![Made with Docsify](https://img.shields.io/badge/Made%20with-Docsify-blue.svg)](https://docsify.js.org/)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-twitter-guide.svg)](https://GitHub.com/MichaelCurrin/python-twitter-guide/tags/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/MichaelCurrin/python-twitter-guide/blob/master/LICENSE)


## Features

- Unofficial guide
- Aimed at Python developers learning to use _tweepy_
- Code snippets are provided for some common use-cases
- Links to tweepy docs and Twitter API docs are provided
- Links to Twitter policies are provided to encourage fair API usage


## About
> How to use this website and why it exists

The Tweepy docs do cover how the library works on the API page, but examples of how to use the library are limited.

Also, the Tweepy library aims to be a _thin layer_ between your code and the Twitter API, so Tweepy does not always make it clear what values are valid in requests. This puts more burden on the developer to figuring things out by looking at both.

So this website aims at making Tweepy and Twitter API easier to use. With additional support by linking to docs and Twitter policies.


## Install Tweepy

Install [Python 3](python.org/)

Create a virtual environment, as it is recommended to install Python packages inside a virtual
environment. Use the `venv` tool which built-in for Python 3.

```sh
cd my-project
python3 -m venv venv
# Linux and macOS
source venv/bin/activate
```

Install Tweepy in the virtual environment.

```sh
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
