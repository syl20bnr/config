# author: syl20bnr (2013)
# goal: Create a dmenu process.

import os
from subprocess import Popen, PIPE

MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
DMENU = os.path.normpath(os.path.join(MODULE_PATH, '../bin/dmenu'))


def call(p='dmenu',
         f='fixed',
         l=0,
         h=10,
         r=False,
         nb='#002b36',
         nf='#657b83',
         sb='#859900',
         sf='#eee8d5'):
    ''' Returns a dmenu process with the specified title and number
    of rows.
    '''
    cmd = [DMENU, '-f', '-i', '-b', '-l', str(l),
           '-p', p, '-fn', f, '-nb', nb, '-nf', nf, '-sb', sb, '-sf', sf]
    if h:
        cmd.extend(['-h', str(h)])
    if r:
        cmd.append('-r')
    dmenu = Popen(cmd, stdin=PIPE, stdout=PIPE)
    return dmenu


def get_dmenu_monitor_argument(output):
    # not the best way to retrieve the monitor argument but it does the job.
    m = 0
    for i in range(0, 10):
        if str(i) in output:
            m = i
            break
    return str(m)
