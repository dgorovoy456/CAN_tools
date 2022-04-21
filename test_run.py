import time
import subprocess
import re

from can_messages import *
from utils_can_controller import send_can_message, gear_r_is_enable


def run_test():

    # send_can_message(CLICK_CL151)
    # print(gear_r_is_enable('0000'))
    # print('sasa')
    # pass
    # send_can_message(DEFAULT_STATE)
    # send_can_message(CLICK_CL_)
    # time.sleep(1)
    # send_can_message(CLICK_CL15)
    # time.sleep(1)
    # time.sleep(1)
    # time.sleep(2)
    # send_can_message(CLICK_CL30)
    # send_can_message(CLICK_CL15_GEAR_P)
    send_can_message(CLICK_CL15_GEAR_R)
    # send_can_message(CLICK_CL15_CL30_GEAR_R)
    # time.sleep(1)
    # send_can_message(SWITCH_GEAR_R)
    # send_can_message(SWITCH_GEAR_P)

    # print('dsds')
    # m = subprocess.check_output(f'adb logcat -d | grep "visible = " | tail -1', shell=True)
    # s = subprocess.getoutput(f'adb logcat -d | grep "visible = " | tail -1')
    # ss = '\w+[vi]+\w+[ ]\D[ ]\w+'
    # sss = '12-16 16:27:15.247  3765  3765 D EVS_FloatingWindow: visible = false is already set. Ignored in setLayoutVisible'
    # ssss = re.findall(ss, sss)
    # print(ssss)
    # print(m)
    # print(s)


if __name__ == '__main__':
    run_test()
