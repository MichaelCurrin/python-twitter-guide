# Deploy

## Notes

### Do I need this?

You probably don't need to run this if you're not the maintainer of the project, but this can help for your own docs site projects._

## Warnings

- The Docsify SSR tutorial is difficult to follow and has issues - you need an old version of Docsify, you need a site already running it seems and it must be on the root path to avoid errors and you have to setup the app to run on Vercel.
- An alternative followed here is using _presite_, but to get it do work for Docsify involves hacky solutions to make it work and those are not simple to maintain or add to other projects. Also it does not come with a sitemap or robots which I added myself.
- Waiting for Docsify 5 with prerendered solution will be nice.
- Also consider moving to a static mark-down based site like MkDocs.


## What Docsify does

Docsify is a single-page application - it runs from a single `index.html` page and combines that with the navbar config and content in markdown files.

This needs JavaScript to run in the browser. This is fine for most people. But SEO crawlers have little or no support for JavaScript, so they are unable to crawl the site.


## Motivation for prerendering

On solution is to use a utility to _prerender_ the fully-rendered application and store the result as HTML files.

Here we use [presite](https://www.npmjs.com/package/presite), inspired by what Docute uses to build a site. Presite works well for a React or Vue app which have a build directory. But since Docsify does not have one, this takes more effort.


## How to run

See [package.json](/package.json). Presite has been added.


### Build

Run this command to do a production build.

```sh
$ npm run build
```

This can be done locally or on Netlify - see [netlify.toml](/netlify.toml).

The hostname is defined in [processNav.js](/processNav.js) - this is used for the sitemap and should be updated if the Netlify app URL changes.

The output will go to an unversioned directory named `build`.

#### Notes on converting to a static site

See the make paths static script used in build step. There we URLs in the HTML pages so that they follow conventional paths and IDs. Since Docsify normally handle this but now we are running without it.

Scripts to remove at build time:

- Note that as part of the build process, Docsify must be removed otherwise it causes unnecessary redirects on the page. The site renders file.
- Also the search plugin is no longer valid as it points to markdown files which are not there or it would take too much effort to make it work. The search bar has to be hidden using CSS changes.


### Test build
> Preview prerendered site locally before deploying

Start a dev server in the `build` directory, without using the Docsify CLI.

```sh
$ npm serve-static
```

Open the browser at:

- http://localhost:8080

Recommended: Turn off JavaScript in your browser settings before you load the page, so you can be sure that the site works _without_ JavaScript.
