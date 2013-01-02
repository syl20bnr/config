#!/bin/sh
# Lauch a emacs with GUI (it launches the emacs daemon if it is not running)
emacsclient -t -n -a "" $1
