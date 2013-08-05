#!/usr/bin/env python

# author: syl20bnr (2013)
# goal: i3 actions module.

import os
from subprocess import Popen

import dmenu

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
DMENU_EARLY = os.path.normpath(os.path.join(MODULE_PATH, '../bin/dmenu_early'))

DMENU_MAX_ROW = 32
DMENU_HEIGHT = 18


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
            workspace_id = self._get_workspace_id(workspace)
            return "workspace {0}".format(workspace_id)

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
            workspace_id = self._get_workspace_id(workspace)
            return "move workspace {0}".format(workspace_id)

    def layout_cmd(self, cmd):
        return "layout {0}".format(cmd)

    def _get_workspace_id(self, raw):
        workspace_id = raw.decode('utf-8').rstrip()
        workspace_id = workspace_id.replace(',', '')
        return workspace_id


# ----------------------------------------------------------------------------
#  Action groups
# ----------------------------------------------------------------------------


def launch_app(feeder, output='all', free=False):
    ''' Launch an application on the specified monitor.
    output='all' means the current workspace on the current monitor.
    If free is true then the application is opened in a new workspace.
    '''
    from feeders import cur_workspace
    from feeders.free_workspaces import get_free_workspaces
    from feeders.cur_output import get_current_output
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt(),
                      height=DMENU_HEIGHT)
    reply = proc.communicate(feeder.feed().encode('utf-8'))[0]
    if reply:
        if not free and (output == 'all' or output == get_current_output()):
            # open on the current workspace
            action = Action()
            action.add_action(Action.exec_, (reply))
            action.process()
        if not free and (output != 'all' and output != get_current_output()):
            # open on the visible workspace on another output
            otherw = cur_workspace.feed(output)
            action = Action()
            action.add_action(Action.jump_to_workspace, (otherw))
            action.add_action(Action.exec_, (reply))
            action.process()
        elif free and (output == 'all' or output == get_current_output()):
            # free workspace on the current output
            freew = get_free_workspaces()[0]
            action = Action()
            action.add_action(Action.jump_to_workspace, (freew))
            action.add_action(Action.exec_, (reply))
            action.process()
        elif free and (output != 'all' and output != get_current_output()):
            # free workspace on another output
            freew = get_free_workspaces()[0]
            action = Action()
            action.add_action(Action.jump_to_workspace, (freew))
            action.add_action(Action.exec_, (reply))
            action.add_action(Action.send_workspace_to_output, (output))
            action.process()


def jump_to_window(feeder, inst, output='all'):
    ''' Jump to the window chosen by the user using dmenu. '''
    windows = feeder.feed(inst, output)
    size = max([0, min([DMENU_MAX_ROW, len(windows)])])
    proc = dmenu.call('/usr/bin/dmenu',
                      feeder.get_prompt(inst, output), nl=size)
    reply = proc.communicate(
        '\n'.join(windows).encode('utf-8'))[0]
    if reply:
        win = reply.decode('utf-8').rstrip()
        action = Action()
        action.add_action(Action.jump_to_window, (windows.get(win)))
        action.process()


def jump_to_workspace(feeder):
    ''' Jump to the workspace chosen by the user using dmenu. '''
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt("Go to"),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def jump_to_currently_used_workspace(feeder, output='all'):
    ''' Jump to a curently used workspace on the specified outputs
    and chosen by the user using dmenu.
    '''
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt("Go to", output),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.feed(output)).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def send_workspace_to_output(feeder):
    ''' Send the current workspace to the selected output. '''
    from feeders import cur_workspace
    cur_wks = cur_workspace.get_current_workspace()
    if not cur_wks:
        return
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt(),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.send_workspace_to_output, (reply))
        action.process()


def send_window_to_workspace(feeder):
    ''' Send the current window to the selected workspace. '''
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt("Send to"),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
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
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt("Send to", output),
                      height=DMENU_HEIGHT, ret_early=True)
    reply = proc.communicate(
        '\n'.join(feeder.feed(output)).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.send_window_to_workspace, (reply))
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def execute_layout_cmd(feeder):
    ''' Execute: i3-msg layout *user_choice* '''
    proc = dmenu.call(DMENU_EARLY, feeder.get_prompt(), height=DMENU_HEIGHT)
    reply = proc.communicate(
        '\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.layout_cmd, (reply))
        action.process()
