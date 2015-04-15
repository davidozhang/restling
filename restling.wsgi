#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/restling/")

from restling import app as application
application.secret_key = 'restling'
