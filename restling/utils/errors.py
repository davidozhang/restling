# -*- coding: utf-8 -*-
from restling.utils import serializer


class MethodNotAllowedError(Exception):

	def __str__(self):
		return serializer.format(
				status='error',
				message='http method not allowed on this endpoint.',
			)


class MethodNotImplementedError(Exception):

	def __str__(self):
		return serializer.format(
				status='error',
				message='http method not implemented on this endpoint.',
			)


class BadDataError(Exception):

	def __str__(self):
		return serializer.format(
			status='error',
			message='bad data, more than one result received.',
		)


class BadRequestError(Exception):

	def __str__(self):
		return serializer.format(
			status='error',
			message='bad request, one or more required fields is missing?',
		)

class NotFoundError(Exception):

	def __str__(self):
		return serializer.format(
			status='error',
			message='nothing found with requested id.',
		)