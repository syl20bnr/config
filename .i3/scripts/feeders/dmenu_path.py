#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns applications under paths.

from subprocess import Popen, PIPE


def get_prompt(win_inst=None, output='all'):
    prompt = 'Launch application'
    if output != 'all':
        prompt += " on {0}".format(output)
    return "{0} ->".format(prompt)


def feed(win_inst=None, output='all'):
    ''' Returns a list of all found executables under paths.
    '''
    p = Popen('dmenu_path', stdout=PIPE, stderr=PIPE, shell=True)
    return p.stdout.read()


if __name__ == '__main__':
    print(feed())
