```
  _                    _    ____
 (_) ___   ___   _ __ | |_ |___ \
 | |/ __| / _ \ | '__|| __|  __) |
 | |\__ \| (_) || |   | |_  / __/
 |_||___/ \___/ |_|    \__||_____|
```

This package adds the `isort2` command which runs
[isort](https://pycqa.github.io/isort/) and sorts the imports of the python file. It
replaces the old `isort` sublime package which doesn't work anymore and is no longer
maintained.

## Installation

### Package Control

Available in [package control](https://packagecontrol.io/). Just bring up the package
control menu in sublime (default `ctrl-shift-p`), and enter `Package Control: Install
Package`, search for `isort`.

### Manual

Clone this repository from your Sublime packages directory:

```bash
cd ~/.config/sublime-text-2/Packages
git clone git@github.com:ConstantinGahr/sublime-text-isort2.git
```

## Using isort2

You can run `isort2` via the command palette (default `ctrl-shift-p`):

```
Isort2: Sort Imports
```

You can also run this command on save by changing the settings:

```js
{
    "isort_on_save": false,
    "path" : "isort",

    // args is a list of arguments passed to isort
    "args": ["--honor-noqa", "--profile", "black"]
}

```
