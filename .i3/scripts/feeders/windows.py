#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns to stdout the list of all current windows.

import i3
import workspaces


def get_prompt():
    return "Go to window ->"


def get_windows():
    ''' returns a dictionary of key-value pairs of a window text and window id.
    each window text is of format "[workspace] window title (instance number)"
    '''
    res = {}
    for ws in workspaces.get_workspaces():
        workspace = i3.filter(name=ws)
        if not workspace:
            continue
        workspace = workspace[0]
        windows = i3.filter(workspace, nodes=[])
        instances = {}
        # adds windows and their ids to the clients dictionary
        for window in windows:
            win = '[%s] %s' % (workspace['name'], window['name'])
            # appends an instance number if other instances are present
            if win in instances:
                instances[win] += 1
                win = '%s (%d)' % (win, instances[win])
            else:
                instances[win] = 1
            res[win] = window['id']
    return res

if __name__ == '__main__':
    print('\n'.join(get_windows()))
