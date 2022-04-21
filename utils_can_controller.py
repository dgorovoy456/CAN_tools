import can
import can_dump_parcer
import subprocess
import re


def set_up_can_interface():
    bus = can.interface.Bus(bustype='pcan', bitrate=500000, channel='PCAN_USBBUS1')

    return bus


def send_can_message(message):
    bus = set_up_can_interface()
    can_id_list, dlc_list, data_list = can_dump_parcer.parce_dump_file(message)
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
        except can.CanError:
            print("Message NOT sent")
            bus.shutdown()
            bus = set_up_can_interface()
            bus.send(x)
    bus.shutdown()


# /////////////////////////////////////////
my_regex = '.*visible\s=\s(\w*).*'
gear_regex = f'\w+[vi]+\w+[ ]\D[ ]\w+'
gear_state = 'shell logcat -d | grep "visible = "'


def gear_r_is_enable(adb_serial) -> bool:
    state = subprocess.getoutput(f'adb -s {adb_serial} {gear_state}')
    if re.match(my_regex, state):
        state1 = re.search(my_regex, state).group(1)
        print(state1)
        if state1 == 'false':
            return True
        else:
            return False
    else:
        return False




