# Twitter policies
> A guide to fair use of Twitter and the Twitter API by following their policies

Follow this guide to:

- avoid abusing the API policy
- avoid reaching API rate limits or doing actions which Twitter does not allow
- avoid getting your account blocked for bad behavior
- make a successful dev app application

This guide is especially useful if you plan to make a **bot** or want to perform bulk actions but also be aware of the many and complex restrictions, so you can stay within in.


## Twitter developer docs
> Docs targeted at developers and the API

- [Developer agreement and policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy)
    - Reads as a formal legal doc.
- [Twitter developers policy](https://developer.twitter.com/en/developer-terms/policy)
    - This reads more like an easy to follow blog post, with chapters.

### Rate limits docs

- [Rate limit basics](https://developer.twitter.com/en/docs/basics/rate-limits) in the docs
- [Rate limits](https://developer.twitter.com/en/docs/basics/rate-limits) by endpoint


## Twitter.com docs

- [Terms of service](https://twitter.com/en/tos)
- [Twitter help center](https://help.twitter.com)
    - [Rules and policies](https://help.twitter.com/en/rules-and-policies) overview
        - There are a lot of policies listed there. So some highlights are shown here.
    - [About Twitter's APIs](https://help.twitter.com/en/rules-and-policies/twitter-api)
        - How they work and what entities are available.
    - [Twitter automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) policy
        - This will help ensure you use the API fairly for tweeting, retweeting, searching, making a bot, etc.


## FAQs

### What are the rate limits?

The Twitter API sets rate limiting on a per-token basis, to avoid applications from overloading the Twitter API servers, unintentionally or maliciously.

See the links in the [Rate limits docs](#rate-limits-docs) section of this page.

There is a limit per endpoint of how many requests can be done in a 15-minute window, or in a longer period such as an hour or 3 hours or 24 hours.


### How do I avoid being rate limited?

If you use the **wait** functionality built into Tweepy, you don't have to worry about waiting for most cases - Tweepy will tell you it is waiting and it will wait. This is covered in the [Auth](auth.md) page.

This works well for doing a search or getting a timeline using a cursor. I don't know if it works with actions such as liking a tweet.


### Is a certain action allowed on the API?

When it comes to using the Twitter API and you are **not sure** if an action by your code is allowed by Twitter API, it is safest to be conservative by **not** doing the action and staying well under any limits which might be considered abuse.

Or, check with the Twitter developers or tweepy support group to see if the action is allowed.


### How do I get out of Twitter jail?

Follow this [Wikihow](https://www.wikihow.com/Get-Out-of-Twitter-Jail) on how avoid get restricted by Twitter and what to do when it happens. Note that these are not specific to the API, so apply both for API and standard use.


## Dev app notes
> Recommendations and warnings around applying for and using a Twitter dev app

### Application process

When you apply for a developer account, your motivation needs to cover a use-case which is compliant with the policies, otherwise you will not get your application approved.

If you use your app for something not allowed by the Twitter policies or beyond what you applied for, your app can get blocked. If you need to extend your app from say just searching to posting tweets or replying to users, you must request additional app permissions.


## App restrictions

Your dev app may get restricted or deactivated if you regularly exceed API limits or do actions not allowed by Twitter policies or do an action which is not covered by your dev application Twitter. Generally you won't have to worry if you are just consuming info. When you start posting or engaging with others using scheduled script or realtime bot, then you need to be careful that you follow the automation rules.

It is recommended to create a **new** Twitter account and use that to register a dev app, to avoid your main Twitter account getting blocked even from accidental violation of policies.

Even if you use a browser scraping approach rather than the API, note that Twitter might block your IP address if you do high volume scraping or similar suspicious behavior.
