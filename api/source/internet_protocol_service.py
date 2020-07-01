import miniupnpc
import logging
from exceptions import custom_exceptions

import json

#input: string
#output: string
def get_ip():
    uPnP = connect_to_upnp()
    dicOfIp = {}
    dicOfIp["public"] = uPnP.externalipaddress()
    dicOfIp["private"] = uPnP.lanaddr
    return dicOfIp

#input: none
#output: Upnp object
def connect_to_upnp():
    uPnP = miniupnpc.UPnP()
    uPnP.discoverdelay = 200
    uPnP.discover()
    uPnP.selectigd()
    return uPnP