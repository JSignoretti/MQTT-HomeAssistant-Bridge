'''
Kristijan Stojanovski
10/7/2025

You'll notice that I do static typing, this is just  for me and my code editor for bug checking.
'''

# LIBRARIES
from enum import Enum
import ipaddress
import argparse

# SCRIPTS
from networking import *


class Mode(Enum):
    CONTROLLER = 0
    HYBRID = 1
    DEVICE = 2
    NONE = 3
    CLIENT = 4
    SERVER = 5



def main()->None:

    # DEFULT MODE
    mode: Mode = Mode.NONE


    # Commandline arg setup
    argParser = argparse.ArgumentParser(description="Ill figure this out later.")

    argParser.add_argument("mode", type=str, help="Operating mode for script.",)

    argParser.add_argument("ip", type=str, help="IP address of forward device.\n IP of Controller for Devices, IP of Broker for Controller/Hybrid.")

    argParser.add_argument("port", type=str, help="Port of forward device.\n IP of Controller for Devices, IP of Broker for Controller/Hybrid.")

    args = argParser.parse_args()


    # SET MODE
    match args.mode:
        case "controller":
            mode = Mode.CONTROLLER
        case "hybrid":
            mode = Mode.HYBRID
        case "device":
            mode = Mode.DEVICE
        case "client":
            mode = Mode.CLIENT
        case "server":
            mode = Mode.SERVER
        case _:
            mode = Mode.NONE


    if(mode == Mode.NONE):
        raise ValueError("Invalid mode provided.")

    print(f"Starting in {args.mode} mode...")


    # SET IP ADDRESS
    try:
        ipAddr = ipaddress.ip_address(args.ip)

    except ValueError as e:
        raise ValueError(f"Invalid ip address: {e}.")


    print(f"Upstream ip address set as {ipAddr}...")


    if(mode == Mode.SERVER):
        runServer(str(ipAddr), int(args.port))
    elif(mode == Mode.CLIENT):
        runClient(str(ipAddr), int(args.port))
    else:
        print("Mode not implemented.")




if(__name__ ==  "__main__"):
    main()
    quit()