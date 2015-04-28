# -*- coding: utf-8 -*-

from flask import jsonify, request

from restling import app, db
from restling.models.faq import FAQ
from restling.utils import errors, serializer
from restling.utils.services import RestlingCollection, RestlingDetail

'''
Restling FAQ Service
Author: David Zhang
(C) Copyright David Zhang, 2015.
'''


class FAQ_Collection(RestlingCollection):
	model = FAQ

	def get(self):
		return super(FAQ_Collection, self).get()

	def post(self):
		return super(FAQ_Collection, self).post()


class FAQ_Detail(RestlingDetail):
	model = FAQ

	def get(self, id):
		return super(FAQ_Detail, self).get(id)

	def put(self, id):
		return super(FAQ_Detail, self).put(id)

	def patch(self, id):
		return super(FAQ_Detail, self).patch(id)

	def delete(self, id):
		return super(FAQ_Detail, self).delete(id)
