#!/usr/bin/env python

# author: syl20bnr (2013)
# goal: i3 actions module.

from subprocess import Popen

import i3

import dmenu
from constants import DMENU_MAX_ROW, DMENU_FONT, DMENU_HEIGHT
from feeders import (cur_workspace,
                     cur_workspaces,
                     free_workspaces,
                     cur_output,
                     outputs,
                     windows)


class Action(object):
    ''' Define an i3-msg action. '''

    def __init__(self):
        self._actions = []

    def add_action(self, action, args):
        action = action.__call__(self, args)
        self._actions.append(action)

    def process(self):
        cmd = 'i3-msg ' + ','.join(self._actions)
        Popen(cmd, shell=True)

    def exec_(self, app):
        return 'exec {0}'.format(app)

    def jump_to_window(self, window):
        ''' Jump to the specified window. '''
        return '[con_id={0}] focus'.format(window)

    def jump_to_workspace(self, workspace):
        ''' Jump to the given workspace.
        Current used workspaces are prefixed with a dot '.'
        Workspace '`' means "back_and_forth" command.
        Workspace '=' is the scratch pad
        '''
        if workspace == '`':
            return "workspace back_and_forth"
        elif workspace == '=':
            return "scratchpad show"
        else:
            return "workspace {0}".format(workspace)

    def send_workspace_to_output(self, output):
        ''' Send the current workspace to the specified output. '''
        return "move workspace to output {0}".format(output)

    def send_window_to_workspace(self, workspace):
        ''' Send the current window to the passed workspace. '''
        if workspace == '`':
            return "move workspace back_and_forth"
        elif workspace == '=':
            return "move scratchpad"
        else:
            return "move workspace {0}".format(workspace)

    def cmd(self, cmd):
        # wonderful method :-)
        return cmd


# ----------------------------------------------------------------------------
#  Action groups
# ----------------------------------------------------------------------------


def launch_app(feeder, app=None, output='all', free=False):
    ''' Launch an application on the specified monitor.
    output='all' means the current workspace on the current monitor.
    If free is true then the application is opened in a new workspace.
    '''
    reply = app
    if not reply:
        proc = dmenu.call(p=feeder.get_prompt(free, output),
                          f=DMENU_FONT,
                          h=DMENU_HEIGHT)
        reply = proc.communicate(feeder.feed().encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        if not free and (output == 'all' or
                         output == cur_output.get_current_output()):
            # open on the current workspace
            action = Action()
            action.add_action(Action.exec_, (reply))
            action.process()
        if not free and (output != 'all' and
                         output != cur_output.get_current_output()):
            # open on the visible workspace on another output
            otherw = cur_workspace.feed(output)
            action = Action()
            action.add_action(Action.jump_to_workspace, (otherw))
            action.add_action(Action.exec_, (reply))
            action.process()
        elif free and (output == 'all' or
                       output == cur_output.get_current_output()):
            # free workspace on the current output
            freew = free_workspaces.get_free_workspaces()[0]
            action = Action()
            action.add_action(Action.jump_to_workspace, (freew))
            action.add_action(Action.exec_, (reply))
            action.process()
        elif free and (output != 'all' and
                       output != cur_output.get_current_output()):
            # free workspace on another output
            freew = free_workspaces.get_free_workspaces()[0]
            action = Action()
            action.add_action(Action.jump_to_workspace, (freew))
            action.add_action(Action.exec_, (reply))
            action.add_action(Action.send_workspace_to_output, (output))
            action.process()


def jump_to_window(feeder, inst, output='all'):
    ''' Jump to the window chosen by the user using dmenu. '''
    (wins, d) = feeder.feed(inst, output)
    size = max([0, min([DMENU_MAX_ROW, len(wins)])])
    proc = dmenu.call(p=feeder.get_prompt(inst, output),
                      f=DMENU_FONT,
                      l=size,
                      sb='#b58900')
    reply = proc.communicate('\n'.join(wins).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.jump_to_window, (d.get(reply)))
        action.process()


def jump_to_workspace(feeder):
    ''' Jump to the workspace chosen by the user using dmenu. '''
    proc = dmenu.call(p=feeder.get_prompt("Go to"),
                      h=DMENU_HEIGHT,
                      r=True,
                      sb='#d33682')
    reply = proc.communicate(
        '\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def jump_to_currently_used_workspace(feeder, output='all'):
    ''' Jump to a curently used workspace on the specified outputs
    and chosen by the user using dmenu.
    '''
    proc = dmenu.call(p=feeder.get_prompt("Go to", output),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      r=True,
                      sb='#268bd2')
    reply = proc.communicate('\n'.join(feeder.feed(output)).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def send_workspace_to_output(feeder):
    ''' Send the current workspace to the selected output. '''
    from feeders import cur_workspace
    cur_wks = cur_workspace.get_current_workspace()
    if not cur_wks:
        return
    proc = dmenu.call(p=feeder.get_prompt(),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      r=True,
                      sb='#268bd2')
    outs = feeder.get_outputs_dictionary()
    reply = proc.communicate(
        '\n'.join(sorted(outs.keys())).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.send_workspace_to_output, (outs[reply]))
        action.process()


def send_window_to_workspace(feeder):
    ''' Send the current window to the selected workspace. '''
    proc = dmenu.call(p=feeder.get_prompt("Send to"),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      r=True,
                      sb='#6c71c4')
    reply = proc.communicate('\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.send_window_to_workspace, (reply))
        action.process()


def send_window_to_free_workspace(feeder, output):
    ''' Send the current window to a free workspace on the given output. '''
    freew = feeder.feed()
    if freew:
        from feeders import cur_output
        w = freew[0]
        action = Action()
        action.add_action(Action.send_window_to_workspace, (w))
        action.add_action(Action.jump_to_workspace, (w))
        if output != 'all' and output != cur_output.feed():
            action.add_action(Action.send_workspace_to_output, (output))
        action.process()


def send_window_to_used_workspace(feeder, output):
    ''' Send the current window to a used workspace on the given output. '''
    proc = dmenu.call(p=feeder.get_prompt("Send to", output),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      r=True,
                      sb='#6c71c4')
    reply = proc.communicate('\n'.join(feeder.feed(output)).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.send_window_to_workspace, (reply))
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def send_window_to_visible_workspace(feeder):
    ''' Send the current window to the visible workspace on the
    next output.
    '''
    noutput = _get_next_output()
    otherw = cur_workspace.feed(noutput)
    action = Action()
    action.add_action(Action.send_window_to_workspace, (otherw))
    action.add_action(Action.jump_to_workspace, (otherw))
    action.process()


def send_window_to_win_workspace(feeder):
    ''' Send the current window to the workspace of the selected window. '''
    (wins, d) = feeder.feed()
    size = max([0, min([DMENU_MAX_ROW, len(wins)])])
    proc = dmenu.call(p="Send to workspace of window ->",
                      f=DMENU_FONT,
                      l=size,
                      sb='#d33682')
    ws = cur_workspace.feed()
    excluded_wins = _get_window_ids_of_workspace(ws)
    if excluded_wins:
        # remove the wins of the current output from the list
        wins = [k for k, v in d.iteritems() if v not in excluded_wins]
    reply = proc.communicate('\n'.join(wins).encode('utf-8'))[0]
    if reply:
        ws = _get_window_workspace(d.get(reply))
        reply = reply.decode('utf-8')
        action = Action()
        action.add_action(Action.send_window_to_workspace, (ws))
        action.add_action(Action.jump_to_workspace, (ws))
        action.process()


def execute_cmd(feeder, prefix):
    ''' Execute: i3-msg prefix *user_choice* '''
    proc = dmenu.call(p=feeder.get_prompt(prefix),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      sb='#cb4b16')
    reply = proc.communicate('\n'.join(feeder.feed(prefix)).encode('utf-8'))[0]
    if reply:
        reply = reply.decode('utf-8')
        cmd = reply
        if prefix:
            cmd = prefix + ' ' + cmd
        action = Action()
        action.add_action(Action.cmd, cmd)
        action.process()


def _get_next_output():
    coutput = cur_output.get_current_output()
    outs = outputs.get_outputs_dictionary()
    for o in outs.itervalues():
        if o != coutput:
            return o
    return None


def _get_window_workspace(win_id):
    cworkspaces = cur_workspaces.get_cur_workspaces()
    for ws in cworkspaces:
        ws_tree = i3.filter(name=ws)
        if i3.filter(tree=ws_tree, id=win_id):
            return ws
    return None


def _get_window_ids_of_workspace(ws):
    res = []
    wks = i3.filter(name=ws)
    wins = i3.filter(tree=wks, nodes=[])
    for w in wins:
        res.append(w['id'])
    return res
