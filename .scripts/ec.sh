#!/bin/sh
# Lauch a emacs with GUI (it launches the emacs daemon if it is not running)
emacsclient -c -n -a "" $1
