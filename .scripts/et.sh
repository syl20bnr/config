#!/bin/sh
# Lauch a emacs in the current terminal.
# It launches the emacs daemon if it is not running.
emacsclient -t -n -a "" $1
