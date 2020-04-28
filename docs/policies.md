# Twitter policies

A guide to fair use of Twitter and the Twitter API by following their policies. Follow this guide to avoid abusing the API, getting your account rate-limited or get blocked because of doing actions which Twitter does not allow.


## Resources
> Links to docs on Twitter dev and Twitter around automation and policies

### Twitter developer docs
> Docs targeted at developers and the API

- [developer.twitter.com docs homepage](https://developer.twitter.com/en/docs)
- [Developer agreement and policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy)
    - Reads as a formal legal doc.
- [Twitter developers policy](https://developer.twitter.com/en/developer-terms/policy)
    - This reads more like an easy to follow blog post, with chapters.
- [Rate limits](https://developer.twitter.com/en/docs/basics/rate-limits)

### Twitter.com docs

- [Terms of service](https://twitter.com/en/tos)
- [Twitter help center](https://help.twitter.com)
    - [Rules and policies](https://help.twitter.com/en/rules-and-policies) overview
        - There are a lot of policies listed there. So some highlights are shown here.
    - [About Twitter's APIs](https://help.twitter.com/en/rules-and-policies/twitter-api)
        - How they work and what entities are available.
    - [Twitter automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) policy
        - This will help ensure you use the API fairly for tweeting, retweeting, searching, making a bot, etc.


## Is an action allowed on the API?

When it comes to using the Twitter API and you are **not sure** if an action by your code is allowed by Twitter API, it is safest to be conservative by **not** doing the action and staying well under any limits which might be considered abuse.

Or, check with the Twitter developers or tweepy support group to see if the action is allowed.

## Dev app
> Recommendations and warnings around applying for and using 

### Application process

When you apply for a developer account, your motivation needs to cover a use-case which is compliant with the policies, otherwise you will not get your application approved.

If you use your app for something not allowed by the Twitter policies or beyond what you applied for, your app can get blocked. If you need to extend your app from say just searching to posting tweets or replying to users, you must request additional app permissions.


## App restrictions

Your dev app may get restricted or deactivated if you regularly exceed API limits or do actions not allowed by Twitter policies or do an action which is not covered by your dev application Twitter. Generally you won't have to worry if you are just consuming info. When you start posting or engaging with others using a bot, then you need to be careful that you follow the automation rules.

It is recommended to create a **new** Twitter account and use that to register a dev app, to avoid your main Twitter account getting blocked even from accidental violation of policies.

Even if you use a browser scraping approach rather than the API, note that Twitter might block your IP address if you do high volume scraping or similar suspicious behavior.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA5MzY3MTU0NiwtMTI0Nzk2MjA5MV19
-->