#!/bin/sh
# Starts emacs client with GUI.
# It will start the emacs daemon if it is not.
emacsclient -t -a "" $1
