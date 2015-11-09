# -*- coding: utf-8 -*-

from flask import Flask, request
import serializer
'''
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:restling@localhost/restling'

from restling.utils import serializer

# Import and register all services and endpoints
from restling.services.faq import FAQ_Collection, FAQ_Detail
app.add_url_rule('/faq', view_func=FAQ_Collection.as_view('faq_collection'))
app.add_url_rule('/faq/<id>', view_func=FAQ_Detail.as_view('faq_detail'))
'''

@app.route('/')
def index():
	return 'welcome to restling api!'

@app.route('/ping')
def ping():
	return 'restling is up and running!'

@app.errorhandler(401)
def unauthorized(e):
	return serializer.format(status='error', message='unauthorized.'), 401

@app.errorhandler(404)
def not_found(e):
	return serializer.format(status='error', message='page not found.'), 404

@app.errorhandler(500)
def internal_error(e):
	return serializer.format(
		status='error',
		message='something\'s wrong with the restling server.',
	), 500

@app.route('/lyrics', methods=['GET'])
def lyrics():
	# Publicly available endpoint
	if 'artist' not in request.args or 'track' not in request.args:
		return serializer.format(status='error', message='invalid request.')

	from lyrics import Lyrics
	l = Lyrics(artist=request.args['artist'], track=request.args['track'])
	return serializer.format(
		status=l.result['status'],
		message=l.result['message'],
		data=l.result['data'],
	)

if __name__ == '__main__':
	app.run()
