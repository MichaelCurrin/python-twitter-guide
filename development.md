# Development
> Guide for running the docs site


## Remote setup
> How to run the docs site on GitHub pages

1. Add a fork this repo to your Github repos.
2. Go to Settings.
3. Enable Github Pages.
4. Check the _environment_ tab to check on the deploy.


## Run locally
> How to run the docs site in a local dev environment


### Installation

1. Install NPM.
2. Install DocsifyJS globally:
  ```sh
  $ npm i -g docsify
  ```
3. Clone the repo (see the _Clone or download_ button on the repo's main page).


### Usage

1. Serve the docs site from the project root.
    ```sh
    $ docsify serve docs
    ```
2. Open in the browser:
    - http://localhost:3000

The site will autoreload when you save changes.


## Notes

- Use `bash` for codeblocks - the syntax highlighting plugin does not recognize `sh` properly.
