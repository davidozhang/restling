# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView
from sqlalchemy.orm import class_mapper

from restling import app, db
from restling.utils import serializer
from restling.utils import errors

'''
Restling Service Base Classes
Author: David Zhang
(C) Copyright David Zhang, 2015.
'''


class RestlingCollection(MethodView):
	def get(self):
		return serializer.format(data=[i.serialize for i in self.model.query])

	def post(self):
		json = request.json
		try:
			item = self.model(json)
			db.session.add(item)
			db.session.commit()
			json['id'] = item.id
			return jsonify(json), 201
		except:
			return str(errors.BadRequestError()), 400

	def put(self):
		return str(errors.MethodNotAllowedError()), 405

	def patch(self):
		return str(errors.MethodNotAllowedError()), 405

	def delete(self):
		return str(errors.MethodNotAllowedError()), 405


class RestlingDetail(MethodView):
	def get(self, id):
		results = [i.serialize for i in self.model.query.filter_by(id=id)]
		if len(results) > 1:
			return str(errors.BadDataError(), id), 403
		return serializer.format(
			data=[i.serialize for i in self.model.query.filter_by(id=id)],
		), 200

	def post(self, id):
		return str(errors.MethodNotAllowedError()), 405

	def put(self, id):
		json = request.json
		item = self.model.query.get(id)
		if not item:
			return str(errors.NotFoundError()), 404
		try:
			p_keys = [i.name for i in class_mapper(self.model).primary_key]
			for key in self.model.__table__.columns._data.keys():
				if key in p_keys:	# prevent primary key overwrite
					continue
				setattr(item, key, json[key])
			db.session.commit()
			json['id'] = item.id
			return jsonify(json), 200
		except:
			return str(errors.BadRequestError()), 400

	def patch(self, id):
		json = request.json
		item = self.model.query.get(id)
		if not item:
			return str(errors.NotFoundError()), 404
		p_keys = [i.name for i in class_mapper(self.model).primary_key]
		for key in json.keys():
			if key in p_keys:	# prevent primary key overwrite
				continue
			setattr(item, key, json[key])
		try:
			db.session.commit()
			json['id'] = item.id
			return jsonify(json), 200
		except:
			return str(errors.BadRequestError()), 400

	def delete(self, id):
		item = self.model.query.get(id)
		if not item:
			return str(errors.NotFoundError()), 404
		db.session.delete(item)
		db.session.commit()
		return serializer.format(
			message='successfully deleted record with id {}'.format(id)
		), 204
