#!/usr/bin/env python

# author: syl20bnr (2013)
# Feeder for dmenu: Returns the output names.

import i3


def get_prompt():
    return "Send to output ->"


def feed():
    res = []
    outputs = i3.msg('get_outputs')
    for o in outputs:
        res.append(o['name'])
    return res

if __name__ == '__main__':
    print('\n'.join(feed()))
