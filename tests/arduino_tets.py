import time
import serial

arduino_serial = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)


def enable_blue_light(arduino_serial) -> bool:
    time.sleep(2)
    arduino_serial.flushInput()
    arduino_serial.flushOutput()
    arduino_serial.write(b'1')
    isenable = arduino_serial.readline()
    # arduino_serial.write(b'2')
    # isenable2 = arduino_serial.readline()
    # print(isenable2)
    # print(isenable2)
    assert isenable is True

    return isenable == b'Blue_enabled\n'



def enable_red_light(arduino_serial):
    # time.sleep(2)
    # serial.write(b'2')
    #
    # time.sleep(5)
    a = 1
    print(chr(a))



if __name__ == '__main__':
    a = enable_blue_light(arduino_serial)
    print(a)
    # read_from_port(arduino_serial, '/home/dhorovyi/arser.log')
