# Development
> Guide for running the docs site


## Remote setup
> How to run the docs site on GitHub pages

1. Add a fork this repo to your Github repos.
2. Go to Settings.
3. Enable Github Pages for the **/docs** directory.
4. Check the _environment_ tab to check on the deploy.


## Run locally
> How to run the docs site in a local dev environment


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
