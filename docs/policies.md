# Twitter policies
> A guide to fair use of Twitter and the Twitter API by following their policies

Follow this guide to:

- Avoid abusing the API policy
- Avoid reaching API rate limits or doing actions which Twitter does not allow
- Avoid getting your account blocked for bad behavior
- Make a successful dev app application

This guide is especially useful if you plan to make a **bot** or want to perform bulk actions but also be aware of the many and complex restrictions, so you can stay within in.


## Quick links

[Links to policies](#links-to-policies) &mdash; [Automation](#automation) &mdash; [Bots](#bots) &mdash; [Rate limits](#rate-limits)


## Why do I need to be familar with Twitter policies?

Tweeting using API requests and some code actually requires _registering_ a dev account and dev app on Twitter. This means filling in an application form with your motivation and getting approval from Twitter's team.

The process can take a few days for approval and some back and forth emails if Twitter asks for more details. 

If you don't do your homework on API best practice, or you don't have a valid use-case that complies with Twitter guidelines, or you don't explain how you'll use the API... you could get your application rejected. Then you'll have to respond with more info if they give you the chance to.


## Links to policies

### In Twitter developer docs
> Docs targeted at developers and the API

- [Developer agreement and policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy)
    - Reads as a formal legal doc.
- [Twitter developers policy](https://developer.twitter.com/en/developer-terms/policy)
    - This reads more like an easy to follow blog post, with chapters.
    - Chapter 1 says you need to comply with _all_ policies and it lists them. [Chapter 1](https://developer.twitter.com/en/developer-terms/policy#2-a)
    - Note "Chapter 3 - Platform usage guidelines". It covers topics such as _Spam, bots, and automation_, _Public display of Tweets_ _Content redistribution_ and _Replicating the Twitter experience_.


### On Twitter.com

- [Terms of service](https://twitter.com/en/tos)


### In Twitter.com help docs

#### General use policies
> These apply to ordinary uses, automated tasks and bots.

- [Twitter help center](https://help.twitter.com) homepage
- [Managing your account](https://help.twitter.com/en/managing-your-account#login-and-password)
    - If you need help managing your account's email and password or other login issues.
- [The Twitter Rules](https://help.twitter.com/en/rules-and-policies/twitter-rules)
    - Safety
    - Privacy
    - Authenticity
- [Rules and policies](https://help.twitter.com/en/rules-and-policies) overview
    - There are a lot of policies listed there. So some highlights are shown below.

#### Automation and bot policies

- [About Twitter's APIs](https://help.twitter.com/en/rules-and-policies/twitter-api)
    - How they work and what entities are available.
- [Twitter automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) policy
    - This will help ensure you use the API fairly for tweeting, retweeting, searching, making a bot, etc.
- [Display requirements](https://developer.twitter.com/en/developer-terms/display-requirements)
    - For showing Twitter content on your application, using the appropriate branding and styling.
        > You should comply with the display requirements below when you display Tweets, timelines, and other Twitter content.

### Updates to the Twitter Developer Policy

See this [blog post](https://blog.twitter.com/developer/en_us/topics/community/2020/twitter_developer_policy_update.html) from March 2020.

Some sections to note:

- Developer Use Case Approval
- Bot Accounts
- Off-Twitter matching


## Rate limits

### What are the rate limits?

The Twitter API sets rate limiting on a per-token basis, to avoid applications from overloading the Twitter API servers, unintentionally or maliciously.

See these docs:

- [Rate limit basics](https://developer.twitter.com/en/docs/basics/rate-limits) in the docs
- [Rate limits](https://developer.twitter.com/en/docs/basics/rate-limits) by endpoint
    - e.g. search API gives 180 or 450 tweets per 15 minute window depending how you so auth.


There is a limit per endpoint of how many requests can be done in a 15-minute window, or in a longer period such as an hour or 3 hours or 24 hours.

### How do I avoid being rate limited?

If you use the **wait** functionality built into Tweepy, you don't have to worry about waiting for most cases - Tweepy will tell you it is waiting and it will wait. This is covered in the [Auth](auth.md) page.

This works well for doing a search or getting a timeline using a cursor. I don't know if it works with actions such as liking a tweet.


## Automation

### Is a certain action allowed on the API?

Make sure you read the policies linked in the [Automation and bot policies](#automation-and-bot-policies) section on this page to understand what you can and can't do with a Twitter dev account for accessing the Twitter API.

When it comes to using the Twitter API and you are **not sure** if an action by your code is allowed by Twitter API, it is safest to be conservative by **not** doing the action. Also, say under any limits which might be considered abuse.

You can also check with the Twitter developers or tweepy support group to see if the action is allowed.

### What automated tasks can I do on behalf of a user?

See the _Consent & permissions_ section in Chapter 2 of this [page](https://developer.twitter.com/en/developer-terms/policy).


## Bots

### Am I allowed to make a bot?

Yes, you are allowed by Twitter to make a bot account, but one that follows Twitter's restrictions.

Your bot can do things like tweet on a schedule, retweet other tweets (selectively but not in bulk) or repost external data or links such as blog posts. But, you cannot use your bot to create tweets to users or reply to users, unless the users have explicitly given permission (such as by messaging your account or opting in within a website/app).

If you do want to message other users with tweets or direct messages when the policies would consider that unwanted spammy actions, you can of course use your Twitter bot account in the browser without using the API and write some hand-crafted messages.

### What can I do as a Twitter bot?

Follow the [Twitter automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) policy.

Follow these guidelines from [Platform usage guidelines](https://developer.twitter.com/en/developer-terms/policy).

> - Always get explicit consent before sending people automated replies or Direct Messages
> - Immediately respect requests to opt-out of being contacted by you
> - Never perform bulk, aggressive, or spammy actions, including bulk following
> - Never post identical or substantially similar content across multiple accounts

### Do I need to say that it is a bot account?

!> Yes, you are also required to **explicitly state in your profile** that your account is a bot. See recommendations below.

?> If you are doing automation that just involves search or streaming and you are *not* actually tweeting or acting like a bot (and people mistaking automated actions for human ones), then it's probably okay to not do this.

Info from Twitter's post in March 2020 on [blog.twitter.com](https://blog.twitter.com):

- From [Updates to the Twitter Developer Policy](https://blog.twitter.com/developer/en_us/topics/community/2020/twitter_developer_policy_update.html)
    - > ... Our new policy asks that developers clearly indicate (in their account bio or profile) if they are operating a bot account, what the account is, and who the person behind it is, so it’s easier for everyone on Twitter to know what’s a bot - and what’s not.
- From [How to quickly update your bot profile bios](https://blog.twitter.com/developer/en_us/topics/tips/2020/how-to-quickly-update-your-bot-profile-bio.html)
    - The post recommends saying the following to the end of a profile bio, where `@handle` is your personal account which is **not** a bot.
        - `#TwitterBot created by @handle`.
    - Example from the post:
        > "Developer Advocate @Twitter. Python programmer. Noted thought leader on vegan snacks. Makes music as Messica Arson. #TwitterBot created by @JessicaGarson"`.
    - The post provides an automation script for updating the bios of configured bios. Unless you have like 20 bots, I think it is less effort to just go into the profile settings and update the bio.

?> You can do add line breaks in your bio, so you might want to do that and move the bot notice to a line on its own.

### How do I get out of Twitter jail?

Your account can land in "Twitter jail" for breaking one of the Twitter or Twitter API policies or usage guidelines, including inappropriate or excessive use.

Follow this [WikiHow](https://www.wikihow.com/Get-Out-of-Twitter-Jail) on how avoid get restricted by Twitter and what to do when it happens. Note that these are not specific to the API, so apply both for API and standard use.


## Dev app notes
> Recommendations and warnings around applying for and using a Twitter dev app

Make sure you familiarize yourself with the policies cover on the rest of this page before you make an application. If your application fails, you might have to just reword and clarify your use-case / motivation, or you might have to reduce the scope to remove actions which are not allowed by the policies. Such as tweeting / replying to users directly without explicit permission.

### Application process

When you apply for a developer account, your motivation needs to cover a use-case which is compliant with the policies, otherwise you will not get your application approved.

If you use your app for something not allowed by the Twitter policies or beyond what you applied for, your app can get blocked.

If you get your application approved and later need to extend your app, from say just searching to posting tweets or replying to users, you must request additional app permissions. This will be similar to the initial application.

### App restrictions

Your dev app may get restricted or deactivated if you regularly exceed API limits or do actions not allowed by Twitter policies or do an action which is not covered by your dev application Twitter. Generally you won't have to worry if you are just consuming info. When you start posting or engaging with others using scheduled script or realtime bot, then you need to be careful that you follow the automation rules.

It is recommended to create a **new** Twitter account and use that to register a dev app, to avoid your main Twitter account getting blocked even from accidental violation of policies.

Even if you use a browser scraping approach rather than the API, note that Twitter might block your IP address if you do high volume scraping or similar suspicious behavior.
