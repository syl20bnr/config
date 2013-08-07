#!/usr/bin/env python

# author: syl20bnr (2013)
# goal: i3 actions module.

from subprocess import Popen

import dmenu

DMENU_MAX_ROW = 32
DMENU_HEIGHT = 18
DMENU_FONT = 'DejaVu Sans Mono-10:normal'


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

    def layout_cmd(self, cmd):
        return "layout {0}".format(cmd)


# ----------------------------------------------------------------------------
#  Action groups
# ----------------------------------------------------------------------------


def launch_app(feeder, app=None, output='all', free=False):
    ''' Launch an application on the specified monitor.
    output='all' means the current workspace on the current monitor.
    If free is true then the application is opened in a new workspace.
    '''
    from feeders import cur_workspace
    from feeders.free_workspaces import get_free_workspaces
    from feeders.cur_output import get_current_output
    reply = app
    if not reply:
        proc = dmenu.call(p=feeder.get_prompt(free, output),
                          f=DMENU_FONT,
                          h=DMENU_HEIGHT)
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
    (windows, d) = feeder.feed(inst, output)
    size = max([0, min([DMENU_MAX_ROW, len(windows)])])
    proc = dmenu.call(p=feeder.get_prompt(inst, output),
                      f=DMENU_FONT,
                      l=size,
                      sb='#b58900')
    reply = proc.communicate('\n'.join(windows).encode('utf-8'))[0]
    if reply:
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
                      sb='#d33682')
    reply = proc.communicate('\n'.join(feeder.feed(output)).encode('utf-8'))[0]
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
    proc = dmenu.call(p=feeder.get_prompt(),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      r=True,
                      sb='#268bd2')
    outputs = feeder.get_outputs_dictionary()
    reply = proc.communicate(
        '\n'.join(sorted(outputs.keys())).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.send_workspace_to_output, (outputs[reply]))
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
        action = Action()
        action.add_action(Action.send_window_to_workspace, (reply))
        action.add_action(Action.jump_to_workspace, (reply))
        action.process()


def execute_layout_cmd(feeder):
    ''' Execute: i3-msg layout *user_choice* '''
    proc = dmenu.call(p=feeder.get_prompt(),
                      f=DMENU_FONT,
                      h=DMENU_HEIGHT,
                      sb='#dc322f')
    reply = proc.communicate('\n'.join(feeder.feed()).encode('utf-8'))[0]
    if reply:
        action = Action()
        action.add_action(Action.layout_cmd, (reply))
        action.process()
