from ctypes import c_ubyte, string_at

import rtlsdr
import serial


class DeviceRTL(object):
    def __init__(self):
        self.isDevice = True
        self.indexRtl = None
        self.name = None
        self.serial = ''
        self.server = 'localhost'
        self.port = 1234
        self.gains = []
        self.gain = 0
        self.calibration = 0
        self.lo = 0
        self.offset = 250e3
        self.tuner = 0

    def set(self, device):
        self.gain = device.gain
        self.calibration = device.calibration
        self.lo = device.lo
        self.offset = device.offset
        self.tuner = device.tuner

    def get_gains_str(self):
        gainsStr = []
        for gain in self.gains:
            gainsStr.append(str(gain))

        return gainsStr

    def get_closest_gain_str(self, desired):
        gain = min(self.gains, key=lambda n: abs(n - desired))

        return str(gain)


def get_devices_rtl(currentDevices=None, statusBar=None):
    if statusBar is not None:
        statusBar.set_general("Refreshing device list...")

    if currentDevices is None:
        currentDevices = []

    devices = []
    count = rtlsdr.librtlsdr.rtlsdr_get_device_count()

    for dev in range(0, count):
        device = DeviceRTL()
        device.indexRtl = dev
        device.name = format_device_rtl_name(rtlsdr.librtlsdr.rtlsdr_get_device_name(dev))
        buffer1 = (c_ubyte * 256)()
        buffer2 = (c_ubyte * 256)()
        serial = (c_ubyte * 256)()
        rtlsdr.librtlsdr.rtlsdr_get_device_usb_strings(dev, buffer1, buffer2,
                                                       serial)
        device.serial = string_at(serial)
        try:
            sdr = rtlsdr.RtlSdr(dev)
        except IOError:
            continue
        device.gains = sdr.valid_gains_db
        device.calibration = 0.0
        device.lo = 0.0
        for conf in currentDevices:
            if conf.isDevice and device.name == conf.name and device.serial == conf.serial:
                device.set(conf)

        devices.append(device)

    for conf in currentDevices:
        if not conf.isDevice:
            devices.append(conf)

    if statusBar is not None:
        statusBar.set_general("")

    return devices


def format_device_rtl_name(name):
    remove = ["/", "\\"]
    for char in remove:
        name = name.replace(char, " ")

    return name


if __name__ == '__main__':
    print 'Please run rtlsdr_scan.py'
    exit(1)
