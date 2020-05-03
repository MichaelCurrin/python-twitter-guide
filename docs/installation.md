# Installation
> How to install Tweepy on Windows and macOS / Linux

Using your shell (PowerShell or Bash/ZSH), install the Tweepy Python package so that you can run it inside Python code in the rest of this guide.

I strongly recommend installing Tweepy in a **virtual environment** and not using a global install for your user or root user.

?> **Virtual env note:** <br>If you are new to Python or virtual environments or for more background on the instructions on this page, I recommend that you read through this guide to [Setup a Python 3 virtual environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).

!> **User install note:** <br>In general, when installing Python packages, **avoid** using the `sudo` command to become root and install with elevated privileges. Since running `sudo` allows a package to run arbitrary and possibly **malicious** code at the root level, including deleting files or installing a virus. There are known cases of this for Python and NPM packages<br>If you _really_ want to install at the global level for your user and `pip install PACKAGE` gives an error, add `--user` flag. Just don't add `sudo` as a prefix.


## Install system dependencies

<!-- TODO: Link to Learn to Code project or gist when links are updated -->

Install [Python 3](https://python.org/).


## Install Python packages

Navigate to your project root folder.

```bash
cd my-project
```

Create a virtual environment named `venv`.

?> Here we use the builtin `venv` tool after the `-m` module flag, but you can use something else like Pipenv if you like.

```bash
python3 -m venv venv
```

Activate the virtual environment.

```bash
# Linux and macOS
source venv/bin/activate

# Windows
source venv\Scripts\activate
```

Install Tweepy into the virtual environment.

```bash
pip install tweepy
```

?> You're already inside a sandboxes Python 3 environment so no need to specify `pip3` or `sudo`.

Now you can import Tweepy within the context of your project's virtual environment. A one-liner to test `tweepy`:

```bash
python -c 'import tweepy; print("It works!")
```

?> Use `deactivate` command to revert to the global environment. Make sure you use the activate command above whenever you need to use `tweepy` in your project.
