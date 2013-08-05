# author: syl20bnr (2013)
# Common functions for all feeders.


def add_monitor_param(parser):
    parser.add_argument('-m', '--monitor',
                        type=int,
                        choices=[0, 1],
                        default=0,
                        help='Monitor index, 0 for main and 1 for second.')


def get_monitor_value(args):
    return 'xinerama-{0}'.format(args.monitor)
