# author: syl20bnr (2013)
# goal: Create a dmenu process.

from subprocess import Popen, PIPE


def call(binary, title, nl=0, height=0, ret_early=False):
    ''' Returns a dmenu process with the specified title and number
    of rows.
    '''
    cmd = [binary, '-i', '-b', '-l', str(nl), '-p', title,
           '-nb', '#002b36', '-nf', '#657b83',
           '-sb', '#859900', '-sf', '#eee8d5']
    if height:
        cmd.extend(['-h', str(height)])
    if ret_early:
        cmd.append('-r')
    dmenu = Popen(cmd, stdin=PIPE, stdout=PIPE)
    return dmenu
