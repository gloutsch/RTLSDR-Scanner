import numpy

APP_NAME = 'RTLSDR Scanner'

F_MIN = 0
F_MAX = 9999
GAIN = 0
SAMPLE_RATE = 2e6
BANDWIDTH = 500e3

LOCATION_PORT = 7786

TIMESTAMP_FILE = 'version-timestamp'

MODE = ["Single", 0,
        "Continuous", 1,
        "Maximum", 2]

NFFT = [16,
        32,
        64,
        128,
        256,
        512,
        1024,
        2048,
        4096,
        8192,
        16384,
        32768]

DISPLAY = ["Plot", 0,
           "Spectrogram", 1,
           "3D Spectrogram", 2,
           "Status", 3,
           "Time Line", 4,
           "Preview", 5]

TUNER = ["Unknown",
         "Elonics E4000",
         "Fitipower FC0012",
         "Fitipower FC0013",
         "FCI FC2580",
         "Rafael Micro R820T",
         "Rafael Micro R828D"]

WINFUNC = ["Bartlett", numpy.bartlett,
           "Blackman", numpy.blackman,
           "Hamming", numpy.hamming,
           "Hanning", numpy.hanning]


class Warn(object):
    SCAN, OPEN, EXIT, NEW, MERGE = range(5)


class Cal(object):
    START, DONE, OK, CANCEL = range(4)


class Display(object):
    PLOT, SPECT, SURFACE, STATUS, TIMELINE, PREVIEW = range(6)


class Mode(object):
    SINGLE, CONTIN, MAX = range(3)


class Plot(object):
    STR_FULL = 'Full'
    STR_PARTIAL = 'Partial'


class PlotFunc(object):
    NONE, AVG, MIN, MAX, VAR, SMOOTH, DIFF, DELTA = range(8)


class Markers(object):
    MIN, MAX, AVG, GMEAN, \
    HP, HFS, HFE, \
    OP, OFS, OFE = range(10)


if __name__ == '__main__':
    print 'Please run rtlsdr_scan.py'
    exit(1)
