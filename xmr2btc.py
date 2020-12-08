from sys import argv
from typing import List
from xmr_to_btc.XMRToBTC import XMRToBTC


def init(args: List[str]) -> bool:
    arg_len: int = len(args)

    # One argument is REQUIRED, th second is OPTIONAL
    if arg_len < 1 or arg_len > 2:
        raise ValueError("E: Incorrect Argument count.  Refer to README for correct usage.")

    return True


def choose_activity(args: List[str]) -> None:
    pass


def shutdown() -> None:
    print(f"\nShutting Down\n")
    global xmr2btc

    xmr2btc = None

    return xmr2btc


# Command Line entry point
if __name__ == '__main__':
    line_args: List[str] = argv[1:]
    xmr2btc: XMRToBTC

    if init(line_args):
        xmr2btc = XMRToBTC()

        choose_activity(line_args)

    shutdown()
