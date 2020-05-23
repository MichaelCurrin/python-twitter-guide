## Deploy

_Note: You probably don't need to run this if you're not the maintainer of the project, but this can help for your own docs site projects._


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

The output will go to a directory called `build`.

#### Notes on converting to a static site

See the make paths static script used in build step. There we URLs in the HTML pages so that they follow conventional paths and IDs. Since Docsify normally handle this but now we are running without it.

Scripts to remove at build time:

- Note that as part of the build process, Docsify must be removed otherwise it causes unnecessary redirects on the page. The site renders file.
- Also the search plugin is no longer valid as it points to markdown files which are not there or it would take too much effort to make it work.


### Test build

Start a dev server in the `build` directory, without using the Docsify CLI.

```sh
$ npm serve-static
```

Open the browser at:

- http://localhost:8080

Recommended: Turn off JavaScript in your browser settings before you load the page, so you can be sure that the site works _without_ JavaScript.
