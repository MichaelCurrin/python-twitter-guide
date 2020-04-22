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
2. Install [DocsifyJS](https://docsify.js.org/) globally:
  ```sh
  $ npm i -g docsify
  ```
3. Clone the repo (see the _Clone or download_ button on the repo's main page).


### Usage

1. Run this command in the project root to serve the [docs](/docs) directory.
    ```sh
    $ docsify serve docs
    ```
2. Open in the browser:
    - http://localhost:3000

The site will autoreload when you save changes.


## Notes

- Use `bash` for codeblocks - the syntax highlighting plugin does not recognize `sh` properly.
