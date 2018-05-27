#!/usr/bin/env python3
# encoding=utf8

import sys
import logging

import re
from radius_response import RadiusResponse
from re2o import Re2o

logging.basicConfig(filename='/var/log/radius/re2o-radius.log', level=logging.INFO)

switch = sys.argv[1]
mac = sys.argv[2]
port = sys.argv[3]

mac = re.sub(r'(..)\B', r'\1:', mac)

logging.debug("Mac address: {mac}".format(mac=mac))

re2o = Re2o()
re2o.init_connection()

is_authorized = re2o.check_mac(mac)
RadiusResponse.send(is_authorized)
