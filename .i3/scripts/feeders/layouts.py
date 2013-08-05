#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns a list of all possible layout commands.


def get_prompt():
    return "Set layout ->"


def feed():
    ''' Return a list of possible layout commands. '''
    return ['default', 'splith', 'splitv', 'stacking', 'tabbed']

if __name__ == '__main__':
    print('\n'.join(feed()))
