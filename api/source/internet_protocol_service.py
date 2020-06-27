import miniupnpc
import logging
from exceptions import custom_exceptions

#input: string
#output: string
def get_ip(typeOfIp):
    uPnP = connect_to_upnp()
    if (typeOfIp == "public"):
        return uPnP.externalipaddress()
    elif (typeOfIp == "private"):
        return uPnP.lanaddr
    else:
        logging.error("Error on user input")
        raise custom_exceptions.InputError(typeOfIp, "Incorrect value provided, please give either private or public")


#input: none
#output: Upnp object
def connect_to_upnp():
    uPnP = miniupnpc.UPnP()
    uPnP.discoverdelay = 200
    uPnP.discover()
    uPnP.selectigd()
    return uPnP