#!/bin/sh
# Starts emacs client in a terminal.
# It will start the emacs daemon if it is not already started.
# test required for compatibility with ranger
if [ "$1" = "--" ]; then
  emacsclient -nw -a "" -c $2
else
  emacsclient -nw -a "" -c $1
fi
