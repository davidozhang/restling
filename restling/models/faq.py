# -*- coding: utf-8 -*-

from restling import db

class FAQ(db.Model):
	__tablename__ = 'faq'

	id = db.Column(db.INTEGER, primary_key=True)
	question = db.Column(db.TEXT, nullable=False)
	answer = db.Column(db.TEXT, nullable=False)

	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

	@property
	def serialize(self):
		return {
			'id': self.id,
			'question': self.question,
			'answer': self.answer,
		}
