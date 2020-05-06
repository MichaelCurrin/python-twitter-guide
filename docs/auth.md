# Authentication
> How to authenticate with the Twitter API using Tweepy and your dev app's credentials

See also the [Authentication](http://docs.tweepy.org/en/latest/auth_tutorial.html) tutorial in the Tweepy docs.


## TL;DR

Here's a common usecase for getting an [App Access Token](#app-access-token).

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
```

The `api` object can be used for searches, streaming, posting a tweet, looking up tweets and so on - see the [Tweepy code samples](code_snippets.md) page for now info.

Keep reading this doc for more info on how to handle different auth approaches and token types and how to add rate limit waiting.


## Token types

The following types of authorization are available:


### App Access Token

This is the most common case. It lets you searches and do actions as your own account, such as get your own timeline or bio or make a tweet.


### Application-Only Auth Token

This is useful for automated tasks like searches.  This method does **not** have a sense of a user context so get it can't get its own timeline or make a tweet. It is can be used for pulling data for known tweet IDs or users or for doing searches. It does have relaxed rate limits - in particular the search API with this token lets you do 480 requests per window rather than 180. Read more on the [Twitter policies](policies#rate-limit-docs) page.

?> **Twitter API docs:** [Application-only](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only)

> As this method is specific to the application, it does not involve any users. This method is typically for developers that need read-only access to public information.
>
> API calls using app-only authentication are rate limited per API method at the app level. [source](https://developer.twitter.com/en/docs/basics/authentication/oauth-2-0)


### User Access Token

Implement follow the user sign-in flow to act as another user on their behalf, but without seeing their password.


See Twitter's documentation:

The flow implemented here is based on this article:


## How to do auth in Tweepy


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


### Basic usage

Authorize with an _App Access Token_.

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
```

### Add waiting

You don't have to worry about waiting for most cases - Tweepy will tell you it is waiting and it will wait.

```python
tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
```

### Add retries

Configure your API connection to retry 3 times at 5-second intervals. The default error coded are limited, so cover the possible 4XX and 5XX codes.

```python
tweepy.API(
    retry_count=3,
    retry_delay=5,
    retry_errors=[401, 404, 500, 503],
)
```

Note that some codes like `429` is Too Many Requests and the rate limit waiting will handle that.


### Test it

Confirm that it works:

```python
api.verify_credentials()
```

### Putting it all together


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
```

Example use:

```python
api = get_api_connection(CONSUMER_KEY, CONSUMER_SECRET,
                         ACCESS_KEY, ACCESS_SECRET)
```


### How to get an Application-only token

There are two way to do an application-only flow to get a token which does not have user context.

One approach is using `OAuthHandler` - this is similar to the flow above but leaves out the `.set_access_token` step.

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)
```

The other approach uses `AppAuthHandler` and is covered in the [OAuth 2](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-2-authentication) part of Tweepy docs.

```python
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)
```


### User access token

>! This flow is complex and is **not** necessary for doing searches or making a bot. But is necessary if you want to perform actions on behalf of the user with their permission (such as a liking a Tweet in a mobile app you made).

The user will sign into Twitter in the browser and then will get a short number to enter in your app.This use flow would require you to setup your own API to handle this complex flow. Or you can enter the code on the command-line and capture using `input()` if you want to try that out locally without the extra setup.

Rate limiting is on *each user* token.

?> **Tweepy docs**: [auth tutorial](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-1a-authentication)
