import os
import time


class ADBtoUSBSwitcher:

    def __init__(self, phidget_serial):
        self.phidget_serial = phidget_serial

    def switch_to_adb(self):
        for x in range(4):
            command_switch_to_adb = f'phidutil2 -s {self.phidget_serial} -p {x} 0'
            time.sleep(0.5)
            os.system(command=command_switch_to_adb)

    def switch_to_usb(self):
        for x in range(4):
            command_switch_to_usb = f'phidutil2 -s {self.phidget_serial} -p {x} 1'
            time.sleep(0.5)
            os.system(command=command_switch_to_usb)


if __name__ == '__main__':
    some = ADBtoUSBSwitcher("554160")
    # some.switch_to_adb()
    # time.sleep(30)
    some.switch_to_usb()
