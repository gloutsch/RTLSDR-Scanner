#! /usr/bin/env python

try:
    input = raw_input
except:
    pass

try:
    import rtlsdr  # @UnusedImport
except ImportError as error:
    print 'Import error: {}'.format(error)
    input('\nError importing libraries\nPress [Return] to exit')
    exit(1)

import argparse
import os.path
import signal

from cli import Cli
from constants import APP_NAME
from file import File


def __init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)


def __arguments():
    parser = argparse.ArgumentParser(prog="rtlsdr_scan.py",
                                     description='''
                                        Scan a range of frequencies and
                                        save the results to a file''')
    parser.add_argument("-s", "--start", help="Start frequency (MHz)",
                        type=int, required=True)
    parser.add_argument("-e", "--end", help="End frequency (MHz)", type=int, required=True)
    parser.add_argument("-w", "--sweeps", help="Number of sweeps", type=int,
                        default=1)
    parser.add_argument("-p", "--delay", help="Delay between sweeps (s)",
                        type=int, default=0)
    parser.add_argument("-g", "--gain", help="Gain (dB)", type=float, default=0)
    parser.add_argument("-d", "--dwell", help="Dwell time (seconds)",
                        type=float, default=0.1)
    parser.add_argument("-f", "--fft", help="FFT bins", type=int, default=1024)
    parser.add_argument("-l", "--lo", help="Local oscillator offset",
                        type=int, default=0)
    parser.add_argument("-c", "--conf", help="Load a config file",
                        default=None)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--index", help="Device index (from 0)", type=int,
                       default=0)
    group.add_argument("-r", "--remote", help="Server IP and port", type=str)
    types = File.get_type_pretty(File.Types.SAVE)
    types += File.get_type_pretty(File.Types.PLOT)
    help = 'Output file (' + types + ')'
    parser.add_argument("file", help=help)
    args = parser.parse_args()
    args.dirname, args.filename = os.path.split(args.file)
    return args


if __name__ == '__main__':
    print APP_NAME + "\n"
    args = __arguments()
    try:
        Cli(args)
    except KeyboardInterrupt:
        print '\nAborted'
        exit(1)
