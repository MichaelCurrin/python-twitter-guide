# Development
> Guide for running the docs site


## Working with the docs site

The Github Pages site is served from the `docs` directory and uses DocsifyJS a single-page JS application which builds an elegant site focused on documentation.

Mostly you'll just have to write markdown and not have to learn any templating syntax or config values.

For interest, Docsify works using an `index.html` page as the base to specify plugins and config values, markdown files are read as content and there are some other configs sidebar or navbar.

To learn more about DocsifyJS, see my [Docsify JS Tutorial](https://github.com/MichaelCurrin/docsify-js-tutorial).

If your changes are simple enough you can even make them all on Github without setting up and testing locally. However, testing locally makes testing much easier and also Docsify is so light that you don't even have to install anything to get it working locally.


## Remote setup
> How to run the docs site on GitHub pages

<!-- TODO use gist instead -->

1. Add a fork this repo to your Github repos.
2. Go to Settings.
3. Enable Github Pages for the **/docs** directory.
4. Check the _environment_ tab to check on the deploy.


## Run locally
> How to run the docs site in a local dev environment

<!-- TODO use gist instead -->

### Installation

1. Install [NPM](https://npmjs.com/).
2. Clone the repo (see the _Clone or download_ button on the repo's main page) and navigate to the project root.
3. Install node dependencies (just Docsify CLI). This can be run from the VS Code task too.
    ```sh
    $ npm install
    ```


### Usage

1. Serve the [docs](/docs) directory. This can be run from the configured VS Code task too.
    ```sh
    $ npm start
    ```
2. Open in the browser:
    - http://localhost:3000

The browser will auto reload when you save changes.


## Notes

- The `python` and `bash` highlighting extensions have been added to [index.html](/docs/index.html), so those will work on the frontend.
- Use `bash` only for shell codeblock language - the syntax highlighting plugin does not recognize `sh` properly.
- Add info blocks with `?> Message` and alert blocks with `!> Message`.


### Plugins

- [Search](https://docsify.now.sh/plugins?id=full-text-search)
    - Ensure the search paths are kept up to date with the navbar. The `auto` setting for search seemed limited.
- [Edit on Github](https://github.com/njleonzhang/docsify-edit-on-github)
    - Unlike other plugins, this one must be loaded *before* the app is setup.


## Hyperlinks

Use an understated info block for external links.

```
?> **Tweepy docs:** [Cursor tutorial](http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html)
```

?> **Tweepy docs:** [Cursor tutorial](http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html)


Avoid using stronger CTA button:

```html
<a href="http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html">
    <button class="myButton">See Cursor tutorial on Tweepy docs</button>
</a>
```

<a href="http://docs.tweepy.org/en/v3.8.0/cursor_tutorial.html">
    <button class="myButton">See Cursor tutorial on Tweepy docs</button>
</a>
