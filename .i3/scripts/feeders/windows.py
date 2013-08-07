#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns to stdout the list of all current windows,
# the output can be filtered by windows instance name and output.

from subprocess import Popen, PIPE
import re

import i3

import common
import workspaces


def get_prompt(win_inst=None, output='all'):
    prompt = "window"
    if win_inst:
        prompt = win_inst
    if output != 'all':
        m = common.get_natural_monitor_value(output)
        prompt += " on {0}".format(m)
    return "Go to {0} ->".format(prompt)


def feed(win_inst=None, output='all'):
    ''' Returns a dictionary of key-value pairs of a window text and window id.
    Each window text is of format "[instance] window title (instance number)"
    '''
    res = {}
    for ws in workspaces.get_workspaces_no_prefix():
        workspace = i3.filter(name=ws)
        if not workspace:
            continue
        workspace = workspace[0]
        windows = i3.filter(workspace, nodes=[])
        instances = {}
        # adds windows and their ids to the clients dictionary
        for window in windows:
            print window
            name = window['name']
            inst = _get_X_window_instance(window['window'])
            if inst:
                eligible = win_inst is None or win_inst == inst
                if eligible and output != 'all':
                    # list only the windows on the specified output
                    tree = i3.filter(name=output)
                    eligible = i3.filter(tree, name=name)
                if eligible:
                    win = '[%s] %s' % (inst, window['name'])
                    # appends an instance number if other instances are present
                    if win in instances:
                        instances[win] += 1
                        win = '%s (%d)' % (win, instances[win])
                    else:
                        instances[win] = 1
                    res[win] = window['id']
    return res


def _get_X_window_instance(id):
    ''' Returns the instance of the window with the given name.
    None if no instance is found.
    '''
    inst = None
    cmd = u'xprop -id "{0}" | grep "WM_CLASS(STRING)"'.format(id)
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    out = p.stdout.read()
    if out:
        print out
        m = re.match(r'^.*=\s"(.*?)"', out)
        if m:
            inst = m.group(1)
    return inst


if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser(prog='windows')
    common.add_monitor_param(PARSER)
    PARSER.add_argument('-i', '--instance',
                        default=None,
                        help='X window instance name.')
    args = PARSER.parse_args()
    mon = common.get_monitor_value(args)
    print('\n'.join(feed(args.instance, mon)))
