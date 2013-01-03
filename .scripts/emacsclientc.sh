#!/bin/sh
# Starts emacs client with GUI.
# It will start the emacs daemon if it is not.
emacsclient -c -a "" $1
