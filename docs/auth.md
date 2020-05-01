# Authentication
> How to authenticate with the Twitter API using Tweepy and your dev app's credentials

See also the [Authentication](http://docs.tweepy.org/en/latest/auth_tutorial.html) tutorial in the Tweepy docs.


## Setup credentials

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


## Basic usage

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.verify_credentials()
```

## Use a function

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


# Example use:
api = get_api_connection(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)
```

If Access credentials are provided, the function will create an App Access Token. Otherwise, the access token step will be left out and the function will return an Application-only Access Token. Which has limited context (it can't access a current user) and has different API rate limit restrictions which can be more favorable for certain requests.

?> Not covered here is the User access token, which requires a user to sign into Twitter and then enter a short code into your application. So that your app can perform actions on their behalf - this flow is unnecessary if you want to make a bot, do bulk retweets as your own bot account or do searches. Rate limiting is on each user. This use flow would require you to setup your own API to handle this complex flow. Or you can enter the code on the command-line and capture using `input()` if you want to try that out locally without the extra setup.

Then set up an API instance which will automatically wait and print a notification if a rate limit is reached, to avoid getting blocked by the API.

If you are doing automation for a task like search, which doesn't need a concept of "me" as a Twitter account, you can use the "application-only" flow above which does **not** use access details, only consumer details. The drawback is that some methods around `.me` or `.home_timeline` will no longer work, but the advantage is that certain endpoints like `.search` have a higher threshold for rate limiting.

You can start using the application-only approach without hassle, but if you are interested to learn you can read the  [application-only](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only) doc.

> As this method is specific to the application, it does not involve any users. This method is typically for developers that need read-only access to public information.
>
> API calls using app-only authentication are rate limited per API method at the app level. [source](https://developer.twitter.com/en/docs/basics/authentication/oauth-2-0)


## Application-only flow

There are two way to do an application-only flow and get a App Access Token.

- One approach is using `OAuthHandler` - this is similar to the flow above but leaves out the `.set_access_token` step.
    ```python
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth)
    ```
- The other approach uses `AppAuthHandler` and is covered in the [OAuth 2](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-2-authentication) part of Tweepy docs.
    ```python
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    api = tweepy.API(auth)
    ```

## User auth flow

You can let a user sign in on the browser side of a web app, or in the command-line for a local terminal-based application. This is not necessary for doing searches or making a bot but is necessary if you want to perform actions on behalf of the user with their permission (such as a liking a Tweet in a mobile app you made).

The user will sign into Twitter and then will get a number to enter. The flow here is more complex. Read more [here](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-1a-authentication)
