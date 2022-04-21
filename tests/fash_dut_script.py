import time
import can
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-can'])

Signal = ['[-] 0.000244   CAN 1   VCU_HV_DrvSys_status   CAN Frame    Tx  D9    8     57 01 00 00 00 00 00 00']


def parce_dump_file(signal):
    can_id = []
    dlc = []
    data = []
    for x in signal:

        if x.find('Tx') > 0:
            data_frame = []
            data_from_file = x.split()
            data_from_file = data_from_file[8:]

            can_id.append(int(data_from_file[0], 16))
            dlc.append(int(data_from_file[1], 16))

            for y in data_from_file[2:]:
                data_frame.append(int(y, 16))
            data.append(data_frame)

    return can_id, dlc, data


def set_up_can_interface():
    bus = can.interface.Bus(bustype='pcan', bitrate=500000, channel='PCAN_USBBUS1')

    return bus


def send_can_message(signal):
    bus = set_up_can_interface()
    can_id_list, dlc_list, data_list = parce_dump_file(signal)
    message_list = []
    for (can_id, dlc, data) in zip(can_id_list, dlc_list, data_list):
        msg = can.Message(arbitration_id=can_id, dlc=dlc,
                          data=data,
                          is_extended_id=False)
        message_list.append(msg)
    for x in message_list:
        try:
            bus.send(x)
            print("Message sent on {}".format(bus.channel_info) + str(x))
            time.sleep(1200)
        except can.CanError:
            print("Message NOT sent")
            bus.shutdown()
            bus = set_up_can_interface()
            bus.send(x)
    bus.shutdown()


def run_test():
    send_can_message(Signal)


if __name__ == '__main__':
    run_test()
