# Models

Objects in Tweepy and their attributes.


Links:

- See [models.py] in the Tweepy source code.


## Status

The [tweepy.Status] class, which represents a tweet.

<!-- Separate: -->
<!-- Attributes you can read -->
<!-- Methods for performing actions on a tweet -->

Attributes and methods:

- `author`
    - type: `tweepy.User`
- `contributors`
- `coordinates`
- `created_at`
    - type: `str`
- `destroy`
- `display_text_range`
- `entities`
    - See [entities-object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object) in Twitter dev docs.
- `extended_entities`
- `favorite`
    - Action to star or favorite the tweet.
- `favorite_count`
    - type: `int`
- `favorited`
    - type: `bool`
    - Whether the authenticated user has favorited this tweet.
- `full_text`
- `geo`
- `id`
    - type `int`
- `id_str`
    - type `str`
    - Not really needed for Python. But necessary for JavaScript where the int value will unreliable.
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
- `user`
    - Do not use. Marked as deprecated.


## User

The [tweepy.User] class, which represents a Twitter profile.




[models.py]: [https://github.com/tweepy/tweepy/blob/master/tweepy/models.py
[tweepy.Status]: https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/models.py#L83
[tweepy.User]: https://github.com/tweepy/tweepy/blob/v3.8.0/tweepy/models.py#L144
