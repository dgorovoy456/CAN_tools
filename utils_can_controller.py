import can
import can_dump_parcer


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
