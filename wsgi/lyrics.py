# -*- coding: utf-8 -*-

'''
Restling Lyrics Jsonifier
Author: David Zhang
(C) Copyright David Zhang, 2015.
All lyrics fetched through the app belong to respective artists, owners,
Lyrics Wiki and Gracenote. I do not own any of the lyrics contents.
'''

import StringIO

import requests

from bs4 import BeautifulSoup as bs


class Lyrics(object):

	def get(self, artist, track):
		apiFunctions = {'preview': 'getSong', 'hometown': 'getHometown'}
		result = {'preview': 'N/A','hometown': 'N/A', 'lyrics': 'N/A'}
		for key, function in apiFunctions.iteritems():
			apiURL = '{0}api.php?func={1}&artist={2}&song={3}&fmt=text'.format(
				self.root,
				function,
				artist,
				track,
			)
			if key=='preview' and self._preview(apiURL)=='Not found':
				return None
			elif key=='hometown' and self._preview(apiURL)=='':
				result[key] = 'N/A'
			else:
				result[key] = self._preview(apiURL)

		result['lyrics'] = self._sanitize(
			self._html(
				self.root,
				artist,
				track,
			),
			result['preview'],
		)
		return result

	def __init__(self, *args, **kwargs):
		artist = kwargs.get('artist','N/A')
		track = kwargs.get('track', 'N/A')
		self.root = 'http://lyrics.wikia.com/'
		self.result = {'status':'success', 'data': None, 'message': None}
		self.data = self.get(artist=artist, track=track)
		if self.data:
			self.result['data'] = self.data
		else:
			self.result['status'] = 'error'
			self.result['message'] = 'no lyrics found for {} - {}'.format(
				artist.replace('_', ' '),
				track.replace('_', ' '),
			)

	def _html(self, root, artist, track):
		r = requests.get(root+artist+':'+track)
		return str(bs(r.text)).decode('utf_8')

	def _sanitize(self, html, firstLine):
		result = html[html.index(firstLine):html.index('<p>NewPP')]
		return str(bs(result.replace('<br/>','\n')).text.encode('utf_8'))

	def _preview(self, url):
		r = requests.get(url)
		buf = StringIO.StringIO(bs(r.text).text)
		return buf.readline().replace('\n','').replace('[...]','')
