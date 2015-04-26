# -*- coding: utf-8 -*-

import json


def dumps(data):
    return json.dumps(data)


def loads(json_data):
    return json.loads(json_data)


def format(data=None, status='success', message=None):
	return dumps({'status': status, 'message': message, 'data': data})
