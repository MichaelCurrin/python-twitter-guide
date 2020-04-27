# Models
> The attributes and actions you can perform on Tweepy objects


Links:

- See [models.py] in the Tweepy source code.



## Status

The [tweepy.Status] class, which represents a tweet.

### Attributes
> Read-only values on a tweet

| Name                | Type                 | Description                                                                                                                                                               |
| ------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `author`            | [tweepy.User](#user) | The Twitter profile that made the tweet.                                                                                                                                  |
| `contributors`      |                      |                                                                                                                                                                           |
| `coordinates`       |                      |                                                                                                                                                                           |
| `created_at`        | `str`                | Date and time that the tweet was posted, always with UTC time zone regardless of settings of you or the other account. e.g. `'2020-01-24T08:37:37+00:00'`. See [Code snippets](code_snippets.md) page for parsing this value.                                              |
| `entities`          |                      | See [entities-object] in Twitter dev docs.                                                                                                                                |
| `extended_entities` |                      |                                                                                                                                                                           |
| `favorite_count`    | `int`                | Count of stars/favorites.                                                                                                                                                 |
| `favorited`         | `bool`               | Whether the *authenticated* user has favorited this tweet.                                                                                                                |
| `full_text`         | `str`                | The tweet message, expanded. Only available is using *extended mode*. See [Expand truncated messages](#expand-truncated-messages) section.                                |
| `text`              | `str`                | The tweet message which may be truncated. The default. Not available if is using *extended mode*.                                                                         |
| `id`                | `int`                | Tweet ID - this can be used to lookup a tweet in the browser.                                                                                                             |
| `id_str`            | `str`                | Tweet ID - This version is not really needed for Python. But it necessary for JavaScript, where the numeric `.id` value is unreliable due to limitations of the language. |

[entities-object]: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object

### Methods
> Actions you can perform on a tweet

| Name       | Description                            |
| ---------- | -------------------------------------- |
| `destroy`  | Delete this tweet (by your own user).  |
| `favorite` | Star/favorite this tweet as your user. |

### Unsorted

- `_json`
    - `dict`
    - Return the object as a dictionary. Note this is very long and has nested values which could be looked up easier using one of the attributes on the tweet object. However, this is JSON attribute is useful if you want to convert to tweet to a string then write it out to a text file such as CSV or JSON. 
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

### Deprecated
> Do not use these on the tweet object - they are marked as deprecated.

- `user`


### Expanded truncated messages


By default Tweepy will return tweets which have a message up to 140 characters on the `tweet.text` attribute. 

For tweets which go past this up to 280 characters, you need to pass in a flag. It is safe to do this all the time, regardless of whether the tweet is actually truncated.

```python
tweets = api.search(q=query, tweet_mode='extended')
```

Using the Cursor approach, based on the Tweepy [Cursor tutorial]

```python
tweets = tweepy.Cursor(api.search, q=query, tweet_mode='extended')

for tweet in tweets:
    print(tweet.full_text)
```

## User

The [tweepy.User] class, which represents a Twitter profile.



[models.py]: https://github.com/tweepy/tweepy/blob/master/tweepy/models.py
[tweepy.Status]: https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/models.py#L83
[tweepy.User]: https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/models.py#L144
[Cursor tutorial]: http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html
