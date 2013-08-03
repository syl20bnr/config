#!/usr/bin/env python

# author: syl20bnr (2013)
# goal: Go to the selected i3 window

import os
import subprocess

import dmenu

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
DMENU_EARLY = os.path.normpath(os.path.join(MODULE_PATH, '../bin/dmenu_early'))

DMENU_MAX_ROW = 32
DMENU_HEIGHT = 18


def jump_to_window(feeder):
    ''' Jump to the window chosen by the user using dmenu. '''
    windows = feeder.get_windows()
    size = max([0, min([DMENU_MAX_ROW, len(windows)])])
    proc = dmenu.call('/usr/bin/dmenu', feeder.get_prompt(), nl=size)
    reply = proc.communicate(
        '\n'.join(windows).encode('utf-8'))[0]
    if reply:
        win = reply.decode('utf-8').rstrip()
        arg = '[con_id={0}] focus'.format(windows.get(win))
        subprocess.Popen(["i3-msg", arg])


def jump_to_workspace(feeder):
    ''' Jump to the workspace chosen by the user using dmenu. '''
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt(),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.get_workspaces()).encode('utf-8'))[0]
    if reply:
        if reply == '`':
            subprocess.Popen(["i3-msg", "workspace", "back_and_forth"])
        else:
            workspace_id = reply.decode('utf-8').rstrip()
            subprocess.Popen(["i3-msg", "workspace", workspace_id])


def send_workspace_to_output(feeder):
    ''' Send the current workspace to the selected output. '''
    from feeders import cur_workspace
    cur_wks = cur_workspace.get_current_workspace()
    if not cur_wks:
        return
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt(),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.get_outputs()).encode('utf-8'))[0]
    if reply:
        subprocess.Popen(
            ["i3-msg", "move", "workspace", "to", "output", reply])


def send_window_to_workspace(feeder):
    ''' Send the current window to the selected workspace. '''
    proc = dmenu.call(DMENU_EARLY, "Send to workspace ->",
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.get_workspaces()).encode('utf-8'))[0]
    if reply:
        if reply == '`':
            subprocess.Popen(["i3-msg", "move", "workspace", "back_and_forth"])
        else:
            subprocess.Popen(["i3-msg", "move", "workspace", reply])
