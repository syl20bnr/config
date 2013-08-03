#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns to stdout the list of all possible workspaces

import string


def get_prompt():
    return "Go to workspace ->"


def get_workspaces():
    ''' Return a list of all possible workspaces formed with one char. '''
    return ([str(x) for x in range(0, 10)] +
            [x for x in string.lowercase] +
            ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
             '+', '[', '{', ']', '}', '|', '\\', ';', ':', "'", '"', ',',
             '<', '.', '>', '/', '?', '~', '`'])

if __name__ == '__main__':
    print('\n'.join(get_workspaces()))
