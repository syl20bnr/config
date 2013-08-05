#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns to stdout the list of all possible workspaces

import string

import i3


def get_prompt(verb):
    return "{0} workspace ->".format(verb)


def get_workspaces_no_prefix():
    ''' Return a raw list of all possible workspaces formed with one char.
    The '`' workspace means back_and_forth command instead of a workspace.
    '''
    return ([str(x) for x in range(0, 10)] +
            [x for x in string.lowercase] +
            ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
             '_', '=', '+', '[', '{', ']', '}', '|', '\\', ';', ':',
             "'", '"', '.', '<', '>', '/', '?', '~', '`'])


def feed():
    ''' Return a list of all possible workspaces formed with one char with
    special prefixes for more possibilities.
    Current workspaces are prefixed with a dot '>', so the ',' workspace
    does not exist.
    '''
    workspaces = get_workspaces_no_prefix()
    for i, ws in enumerate(workspaces):
        workspace = i3.filter(name=ws)
        if workspace:
            workspaces[i] = ',' + ws
    return workspaces

if __name__ == '__main__':
    print('\n'.join(feed()))
