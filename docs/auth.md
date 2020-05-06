# Authentication
> How to authenticate with the Twitter API using Tweepy and your dev app's credentials

See also the [Authentication](http://docs.tweepy.org/en/latest/auth_tutorial.html) tutorial in the Tweepy docs.


## TL;DR

There are three token types, covered under [Token types](#token-types) section.

Here's a common usecase for getting `api` object which authenticates through [App Access Token](#app-access-token) approach.

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
```

The `api` object can be used for searches, streaming, posting a tweet, looking up tweets and so on - see the [Tweepy code samples](code_snippets.md) page for now info.

Keep reading this doc for more info on how to handle different auth approaches and token types and how to add rate limit waiting to the auth flow.


## Resources

?> **Twitter dev docs:** [Authentication](https://developer.twitter.com/en/docs/basics/authentication/guides/authentication-best-practices) guide.


## How to do auth in Tweepy


### Setup credentials

Paste each of the four values from your credentials in your code like this. Replace the dummy values in quotes with your own values.

```python
CONSUMER_KEY = 'abc'
CONSUMER_SECRET = 'def'
ACCESS_KEY = 'foo'
ACCESS_SECRET = 'bar'
```

!> Make sure to **never** includes these in version control (repo commits). They can be stored in an unversioned config file ignored by `.gitignore`, as covered in this [tutorial](https://help.github.com/en/github/using-git/ignoring-files). Using environment variables.

A typical setup is to store your credentials in a config file ignored by `git`, rather than in a Python script. Here are some options for config files.

- `.env` - Shell script of properties. Readable from the shell or a Python package (e.g. `dotenv`).
- `config_local.ini` - A config file readable using the builtin ConfigParser in Python.
- `config_local.yaml` - A YAML config file. Readable using the PyYAML library once that is installed.


### Basic usage

Here we authorize with an [App Access Token](#app-access-token) approach, the typical flow for authorizing so you can fetch data and do automated tasks like tweet as the account which you authenticated with.

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
```

?> **Tweepy docs** See the parameters that `API` takes and what they mean at this [reference](http://docs.tweepy.org/en/latest/api.html#API).

You can continue with the steps here to make the `api` object more robust or add go to the [Token types](#token-types) section to explore other options. Or stick with your current `api` object setup and jump to [Tweepy code samples](code_snippets.md) section and start requesting the API.


### Add waiting

You don't have to worry about waiting for most cases - Tweepy will tell you it is waiting and it will wait.

```python
tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True,
)
```

### Add retries

Configure your API connection to retry 3 times at 5-second intervals.

The default error coded are limited, so cover the possible `4XX` and `5XX` [HTTP Status Codes](https://developer.twitter.com/en/docs/basics/response-codes).

```python
tweepy.API(
    auth,
    retry_count=3,
    retry_delay=5,
    retry_errors=[401, 404, 500, 503],
)
```

?> **Note:** Some codes like `429` for Too Many Requests can be left out if the Tweepy rate limit waiting will handle them already. Also, forcing a retry immediately when rate limiting could be a bad idea, so don't put `429` above.


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

    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True
        retry_count=3,
        retry_delay=5,
        retry_errors=[401, 404, 500, 503],
    )

    return api
```

Example use:

```python
api = get_api_connection(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_KEY,
    ACCESS_SECRET
)

api.verify_credentials()
print(api.me())
```


## Token types


Depending how you authenticate, you'll get an `api` object which has a different token on it and therefore has different scope and context.

- [App Access Token](#app-access-token)
- [Application-Only Auth Token](#application-only-auth-token)
- [User Access Token](#user-access-token)


### App Access Token

This is the most common case. It lets you searches and do actions as your own account, such as get your own timeline or bio or make a tweet.

#### How to get an App Access Token

Use this flow:

```python
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
```


### Application-Only Auth Token

This is useful for automated tasks like searches.  This method does **not** have a sense of a user context so get it can't get its own timeline or make a tweet. It is can be used for pulling data for known tweet IDs or users or for doing searches. It does have relaxed rate limits - in particular the search API with this token lets you do 480 requests per window rather than 180. Read more on the [Twitter policies](policies#rate-limit-docs) page.

?> **Twitter API docs:** [Application-only](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only)

> As this method is specific to the application, it does not involve any users. This method is typically for developers that need read-only access to public information.
>
> API calls using app-only authentication are rate limited per API method at the app level. [source](https://developer.twitter.com/en/docs/basics/authentication/oauth-2-0)


#### How to get an Application-only token

There are two ways to do an application-only flow to get a token which does not have user context.

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


### User Access Token

Implement follow the user sign-in flow to act as another user on their behalf, but without seeing their password.

!> This flow is complex and is **not** necessary for doing searches or making a bot. But is necessary if you want to perform actions on behalf of the user with their permission (such as a liking a Tweet in a mobile app you made).

The user will sign into Twitter in the browser and then will get a short number to enter in your app.This use flow would require you to setup your own API to handle this complex flow. Or you can enter the code on the command-line and capture using `input()` if you want to try that out locally without the extra setup.

?> Rate limiting is measured on *each user token*, not your application. This can be useful do perform many actions as various users which would exceed the limits of a single account. However, note that you cannot cheat this as you need those unique to actually sign into your application.

!> Note that you should **not** sign in your application with this flow as your own account, as it will reset the _consumer_ credentials. Then you'll have to copy them from your dev account settings again and then use them in your application. So rather have one Twitter account which you use for automation and one Twitter which you use for normal activity, then test your user sign-in flow with your real account.

?> **Tweepy docs:** [Auth tutorial](http://docs.tweepy.org/en/latest/auth_tutorial.html#oauth-1a-authentication)

?> **Twitter API docs:** [Log in with Twitter](https://developer.twitter.com/en/docs/basics/authentication/guides/log-in-with-twitter) guide.

#### How to get a User Access Token

I've used this flow before and got it to work. But I had no use-case so I stopped using it and it may be out of date with Tweepy or Twitter API changes.

Note you'll also have to setup the auth URL on your Twitter dev account.


<details>
<summary><b>user_token.py</b></summary>

[user_token.py](_scripts/user_token.py ':include :type=code')

</details>


## Next steps

Once you've got some `api` object setup, continue to [Tweepy code samples](code_snippets.md) section.
