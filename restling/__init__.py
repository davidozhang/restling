# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:restling@localhost/restling'

from restling.utils import serializer


@app.route('/')
def index():
	return 'restling api index page.'


@app.route('/ping')
def ping():
	return 'restling is up and running!'


@app.route('/lyrics', methods=['GET'])
def lyrics():
	# Publicly available endpoint
	if 'artist' not in request.args or 'track' not in request.args:
		return serializer.format(status='error', message='invalid request.')

	from restling.services.lyrics import Lyrics
	l = Lyrics(artist=request.args['artist'], track=request.args['track'])
	return serializer.format(
		status=l.result['status'],
		message=l.result['message'],
		data=l.result['data'],
	)

if __name__ == '__main__':
	app.run(debug=True)
