# Models
> The attributes and actions you can perform on Tweepy objects


?> **Tweepy repo:** [models.py] module - in case you want to see the Tweepy code. This is useful for methods but attributes come from the Twitter API so use the API references rather.


## Status

The [tweepy.Status] class, which represents a tweet.

### Attributes
> Read-only values on a tweet object

These do not require an API call as the data is already on the object.

Example:

```python
tweet.created_at
```

Available attributes:

?> **Twitter API reference:** [Twitter Tweet object] - see the data dictionary section for field name, language-agnostic data types and meanings. This is the original source so a better and more up to date reference than Tweepy.


| Name                | Type                 | Description                                                                                                                                                                                                                   |
| ------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `author`            | [tweepy.User](#user) | The Twitter profile that created the tweet.                                                                                                                                                                                      |
| `contributors`      |                      |                                                                                                                                                                                                                               |
| `coordinates`       |                      |                                                                                                                                                                                                                               |
| `created_at`        | `str`                | Date and time that the tweet was posted, always with UTC time zone regardless of settings of you or the other account. e.g. `'2020-01-24T08:37:37+00:00'`. See [Code snippets](code_snippets.md) page for parsing this value. |
| `entities`          |                      | See [Entities](#entities).                                                                                                                                                                                   |
| `extended_entities` |                      |                                                                                                                                                                                                                               |
| `favorite_count`    | `int`                | Count of stars/favorites.                                                                                                                                                                                                     |
| `favorited`         | `bool`               | Whether the *authenticated* user has favorited this tweet. Twitter API has a bug around this field.                                                                                                                                                                   |
| `full_text`         | `str`                | The tweet message, expanded to allow up to 280 characters. Only available if using *extended mode*. See [Expand truncated messages](#expand-truncated-messages) section.                                                                                    |
| `text`              | `str`                | The tweet message, which may be truncated and end with ellipsis if it is more than 140 characters. The default. Not available if if using *extended mode*.                                                                                                                             |
| `id`                | `int`                | Tweet ID - this can be used to lookup a tweet in the browser.                                                                                                                                                                 |
| `id_str`            | `str`                | Tweet ID - This version is not really needed for Python. But it necessary for JavaScript, where the numeric `.id` value is unreliable due to limitations of the language.                                                     |


### Methods
> Actions you can perform on a tweet

Example:

```python
tweet.favorite()
```

Available methods:

| Name       | Description                            |
| ---------- | -------------------------------------- |
| `destroy`  | Delete this tweet (by your own user).  |
| `favorite` | Star/favorite this tweet as your user. |

### Unsorted

- `_json`
    - `dict`
    - Return the object as a dictionary. Note this is very long and has nested values which could be looked up easier using one of the attributes on the Python tweet object. However, this is JSON attribute is useful if you want to convert an entire tweet to a string then write it out to a text file, CSV or JSON file. Then you can parse the data later when you read it again. 
- `display_text_range`
- `geo`
- `in_reply_to_screen_name`
- `in_reply_to_status_id`
- `in_reply_to_status_id_str`
- `in_reply_to_user_id`
- `in_reply_to_user_id_str`
- `is_quote_status`
- `lang`
- `metadata`
- `parse`
- `parse_list`
- `place`
- `possibly_sensitive`
- `retweet`
    - Action to retweet the tweet.
- `retweet_count`
    - type `int`
- `retweeted`
    - type `bool`
    - whether your tweet has retweeted
- `retweets`
    - get retweets on the tweet
- `source`
- `source_url`
- `truncated`
- `retweeted_status` - the original tweet, if the current tweet is a retweet. This attribute is not always available on a tweet object, but if it is then it means the current tweet is a retweet.

### Deprecated
> Do not use these on the tweet object - they are marked as deprecated.

- `user`


### Expand truncated messages


By default Tweepy will return tweets which have a message up to 140 characters on the `tweet.text` attribute.

For tweets which go past this up to 280 characters, you need to pass in a flag. It is safe to do this all the time, regardless of whether the tweet is actually truncated.

```python
tweets = api.search(q=query, tweet_mode='extended')
```

Using the Cursor approach, based on the [Paging] guide.

```python
tweets = tweepy.Cursor(api.search, q=query, tweet_mode='extended')

for tweet in tweets:
    print(tweet.full_text)
```

## User

The [tweepy.User] class, which represents a Twitter profile.


### Attributes
> Read-only fields on a user object

These do not require an API call as the data is already on the object.

Example:

```python
user.id
```

Available attributes:

?> **Twitter API reference:** [Twitter User object] - see the data dictionary section for field name, language-agnostic data types and meanings. This is the original source so a better and more up to date reference than Tweepy.



### Methods

#### Get data

This requires one or more API calls.

```python
user.timeline()
```

#### Perform action

```python
user.follow()
```


## Entities
> Metadata available about tweet contents

Rather than parsing a tweet message yourself, Twitter makes a field available to easily give you hashtags, mentions and URLs, or empty arrays if they do not apply to the content tweet.

Tweepy makes the data available as a dictionary on the object, based on the original JSON data.

Example:

```python
tweet.entities
```

```json
{
    "hashtags": [],
    "urls": [],
    "user_mentions": [],
    "symbols": []
}
```

?> **Twitter API docs:** [Twitter Entities object]

### Media

If there are media, on the tweet, then the `"media"` key will be included above too.

See the [Get media on a tweet](code_snippets.md#get-media-on-at-tweet) section on the Tweepy sample code page.


## Extended entities


The API docs linked above recommend using entended entities for that case.

> if you are working with native media (photos, videos, or GIFs), the Extended Entities object is the way to go.

This is available on the tweet as an attribute.

```python
tweet.extended_entities
```

?> **Twitter API docs:** [Twitter Extended Entities object]


## Direct message

When fetching a direct message, you'll get an object back. You can access useful data on that using this attribute:

```python
dm.message_create
```


That is a `dict` object.

To see how to lookup values, see [Get attributes on a message object](code_snippets.md#get-attributes-on-a-message-object).


### JSON data structure

Here is a full breakdown the values, copied from the [Message Create Object] reference in the API docs.

[Message Create Object]: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/guides/message-create-object


<details>
<summary><button>Click to see Example JSON output</button></summary>

```json
{
    "target": {
        "recipient_id": "1234858592"
    },
    "sender_id": "3805104374",
    "source_app_id": "268278",

    "message_data": {
        "text": "Blue Bird",
        "entities": {
            "hashtags": [],
            "symbols": [],
            "urls": [],
            "user_mentions": [],
        },
        "quick_reply_response": {
            "type": "options",
            "metadata": "external_id_2"
        },
        "attachment": {
            "type": "media",
            "media": {
            }
        }
    }
}
```

</details>


## Rate limit status

See the [Get rate limit status](code_snippets.md#get-rate-limit-status) section on the code snippets page.

The resources are split into:

- `users`
- `statuses`
- `help`
- `search`

Within those is a path of an endpoint e.g. `/users/search`.

Then each time has the follow attributes:

- `limit` - The maximum number of requests available for any window period.
- `remaining` - How many requests are left in the current rate limit window.
- `rest` - Time that the window rests. This is a unixtimestamp.


<details>
<summary><b>Click to see example JSON output</b></summary>

Copied from [Rate Limit Status API reference](https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status).

```json
{
    "rate_limit_context": {
        "access_token": "..."
    },
    "resources": {
        "help": {
            "/help/configuration": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/help/languages": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/help/privacy": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/help/tos": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            }
        },
        "search": {
            "/search/tweets": {
                "limit": 180,
                "remaining": 180,
                "reset": 1403602426
            }
        },
        "statuses": {
            "/statuses/home_timeline": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/statuses/lookup": {
                "limit": 900,
                "remaining": 900,
                "reset": 1403602426
            },
            "/statuses/mentions_timeline": {
                "limit": 75,
                "remaining": 75,
                "reset": 1403602426
            },
            "/statuses/oembed": {
                "limit": 180,
                "remaining": 180,
                "reset": 1403602426
            },
            "/statuses/retweeters/ids": {
                "limit": 75,
                "remaining": 75,
                "reset": 1403602426
            },
            "/statuses/retweets/:id": {
                "limit": 75,
                "remaining": 75,
                "reset": 1403602426
            },
            "/statuses/retweets_of_me": {
                "limit": 75,
                "remaining": 75,
                "reset": 1403602426
            },
            "/statuses/show/:id": {
                "limit": 900,
                "remaining": 900,
                "reset": 1403602426
            },
            "/statuses/user_timeline": {
                "limit": 900,
                "remaining": 900,
                "reset": 1403602426
            }
        },
        "users": {
            "/users/contributees": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/users/contributors": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/users/lookup": {
                "limit": 900,
                "remaining": 900,
                "reset": 1403602426
            },
            "/users/profile_banner": {
                "limit": 180,
                "remaining": 180,
                "reset": 1403602426
            },
            "/users/search": {
                "limit": 900,
                "remaining": 900,
                "reset": 1403602426
            },
            "/users/show/:id": {
                "limit": 180,
                "remaining": 180,
                "reset": 1403602426
            },
            "/users/suggestions": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/users/suggestions/:slug": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            },
            "/users/suggestions/:slug/members": {
                "limit": 15,
                "remaining": 15,
                "reset": 1403602426
            }
        }
    }
}
```

</details>



<!-- Centralized links -->

[Twitter Entities object]: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object
[Twitter Extended Entities object]: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/extended-entities-object
[Twitter User object]: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object
[Twitter Tweet object]: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
[models.py]: https://github.com/tweepy/tweepy/blob/master/tweepy/models.py
[tweepy.Status]: https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/models.py#L83
[tweepy.User]: https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/models.py#L144
[Paging]: code_snippets.md#paging
