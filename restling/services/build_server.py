# -*- coding: utf-8 -*-
import os
import subprocess

from flask import request, render_template, send_from_directory, flash

from restling import app
from restling.utils.services import RestlingCollection, RestlingDetail
from restling.utils import errors, serializer

'''
Restling C-File Build Server Endpoint
Built with Love for Pebble Code Challenge!
Author: David Zhang
'''

class Build_Server_Collection(RestlingCollection):
	'''
	Render the HTML page for uploading files to build server.
	'''
	def get(self):
		return render_template('upload.html')

	'''
	Allow client to upload C-File to the Restling Server.
	'''
	def post(self):
		accepted = set(['source.c'])
		file_ = request.files['file']
		if file_.filename not in accepted:
			flash('Please submit files with these names: {}.'.format(list(accepted)))
			return render_template('upload.html')
		self.file_path = os.path.join(
			app.config['UPLOAD_FOLDER'],
			file_.filename,
		)
		file_.save(self.file_path)
		return self._compile()

	'''
	Helper function for compiling the client's uploaded C-File.
	Uses flash to display build errors or successful compiles to client.
	'''
	def _compile(self):
		command = 'gcc -Wall -o output source.c'
		p = subprocess.Popen(
			[command],
			stderr=subprocess.PIPE,
			cwd=app.config['UPLOAD_FOLDER'],
			shell=True,
		)
		err = p.stderr.read()
		if err:
			flash('Build Error: '+err)
		else:
			flash('Compile Successful. Click Download to download a copy of the binary.')
		return render_template('upload.html')


class Build_Server_Detail(RestlingDetail):
	'''
	Allow client to download only the compiled binary file.
	It will return a JSON with error message if the client tries
	to download a file other than the specified output.
	Otherwise, it will return the binary file.
	'''	
	def get(self, filename):
		output = 'output'
		exists = os.path.exists(app.config['UPLOAD_FOLDER']+'/'+filename)
		if not exists:
			flash('The file \'{}\' does not exist.'.format(filename))
		elif filename!=output:
			flash('You can only download file with name \'{}\'.'.format(output))
		else:
			return send_from_directory(
				directory=app.config['UPLOAD_FOLDER'],
				filename=filename,
			)
		return render_template('upload.html')

	'''
    	Override parent post function on detail since it doesn't apply.
    	'''
	def post(self, filename):
		return str(errors.MethodNotAllowedError()), 405

	'''
   	Override parent put function on detail since it doesn't apply.
    	'''
	def put(self, filename):
		return str(errors.MethodNotAllowedError()), 405

	'''
   	Override parent patch function on detail since it doesn't apply.
    	'''
	def patch(self, filename):
		return str(errors.MethodNotAllowedError()), 405

	'''
    	Override parent delete function on detail since it doesn't apply.
    	'''
	def delete(self, filename):
		return str(errors.MethodNotAllowedError()), 405
