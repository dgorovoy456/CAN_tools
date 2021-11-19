from can_messages import *
from utils_can_controller import send_can_message


def run_test():
    send_can_message(CLICK_CN15)


if __name__ == '__main__':
    run_test()
