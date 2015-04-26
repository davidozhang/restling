# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView

from restling import app, db
from restling.models.faq import FAQ
from restling.utils import serializer
from restling.utils import errors

'''
Restling FAQ Service
Author: David Zhang
(C) Copyright David Zhang, 2015.
'''


class Collection(MethodView):
	def get(self):
		return serializer.format(data=[i.serialize for i in FAQ.query])

	def post(self):
		json = request.json
		try:
			faq = FAQ(
				question=request.json['question'],
				answer=request.json['answer'],
			)
		except:
			return str(errors.BadRequestError()), 400
		db.session.add(faq)
		db.session.commit()
		json['id'] = faq.id
		return jsonify(json), 201

	def put(self):
		return str(errors.MethodNotAllowedError()), 405

	def patch(self):
		return str(errors.MethodNotAllowedError()), 405

	def delete(self):
		return str(errors.MethodNotAllowedError()), 405


class Detail(MethodView):
	def get(self, id):
		results = [i.serialize for i in FAQ.query.filter_by(id=id)]
		if len(results) > 1:
			return str(errors.BadDataError(), id), 403
		return serializer.format(
			data=[i.serialize for i in FAQ.query.filter_by(id=id)],
		), 200

	def post(self, id):
		return str(errors.MethodNotAllowedError()), 405

	def put(self, id):
		json = request.json
		faq = FAQ.query.get(id)
		if not faq:
			return str(errors.NotFoundError()), 404
		try:
			faq.question = json['question']
			faq.answer = json['answer']
		except:
			return str(errors.BadRequestError()), 400
		db.session.commit()
		json['id'] = faq.id
		return jsonify(json), 200

	def patch(self, id):
		json = request.json
		faq = FAQ.query.get(id)
		if not faq:
			return str(errors.NotFoundError()), 404
		try:
			faq.question = json.get('question', faq.question)
			faq.answer = json.get('answer', faq.answer)
		except:
			return str(errors.BadRequestError()), 400
		db.session.commit()
		json['id'] = faq.id
		return jsonify(json), 200

	def delete(self, id):
		faq = FAQ.query.get(id)
		db.session.delete(faq)
		db.session.commit()
		return serializer.format(
			message='successfully deleted record with id {}'.format(id)
		), 204
