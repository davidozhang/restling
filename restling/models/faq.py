# -*- coding: utf-8 -*-

from restling import db

class FAQ(db.Model):
	__tablename__ = 'faq'

	id = db.Column(db.INTEGER, primary_key=True)
	question = db.Column(db.TEXT, nullable=False)
	answer = db.Column(db.TEXT, nullable=False)

	def __init__(self, _dict):
		for key in _dict:
			setattr(self, key, _dict[key])

	@property
	def serialize(self):
		return {
			'id': self.id,
			'question': self.question,
			'answer': self.answer,
		}
