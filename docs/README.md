# Python Twitter Guide
> Code snippets and links to docs around using Twitter API and Tweepy

[![Made with Docsify](https://img.shields.io/badge/Made%20with-Docsify-blue.svg)](https://docsify.js.org/)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-twitter-guide.svg)](https://GitHub.com/MichaelCurrin/python-twitter-guide/tags/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/MichaelCurrin/python-twitter-guide/blob/master/README.md#license)


## Features

- Unofficial guide to _Tweepy_
- Aimed at Python developers who want to use the Twitter API to do automated tasks, like make a bot or download thousands of tweets
- Find practical solutions for common _Tweepy_ / Twitter API use-cases. This makes up for lack of practical examples or recommendations in official docs of both.
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

- [tweepy.org homepage](https://www.tweepy.org/)
- [Tweepy docs](http://tweepy.readthedocs.org/)
- [Tweepy Discord](https://discord.gg/bJvqnhg) channel
- Twitter developer docs
    - [Developer docs](https://developer.twitter.com/en/docs) home
    - [API Reference](https://developer.twitter.com/en/docs/api-reference-index)
    - [Twitter apps](https://developer.twitter.com/en/apps) (manage your dev account apps)
- Twitter docs
    - [Terms of service](https://twitter.com/en/tos)
    - [Rules and policies](https://help.twitter.com/en/rules-and-policies)
    - [Twitter automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) policy (this will help ensure you use the API fairly for tweeting, retweeting, searching, making a bot, etc.)


## Terms of use

Note that Tweepy and Twitter API are subject to change so this guide may not always be up to date.
If anything is inaccurate or not up to date, see the contributing guide in the repo and a submit a
Pull Request.

While a best effort is made to keep this guide accurate and reflect the APIs and policies at the
current time, this guide only provides recommendations and some useful info. _You_ are responsible
for ensuring that you use Twitter and the API fairly and that you understand how it works. By using
this guide, you take responsibility for your own actions and do not hold the contributors to this
guide responsible.
