#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns the current workspace.

import i3


def get_prompt():
    return "Current workspace ->"


def get_current_workspace():
    ''' Returns the current workspace (the workspace with focus) '''
    workspaces = i3.msg('get_workspaces')
    workspace = i3.filter(tree=workspaces, focused=True)
    if workspace:
        return workspace[0]['name']
    return ''

if __name__ == '__main__':
    print(get_current_workspace())
