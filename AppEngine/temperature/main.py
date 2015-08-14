#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import urllib2
import logging
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
		temperature = ndb.IntegerProperty()
		latitude = ndb.FloatProperty()
		longitude = ndb.FloatProperty()
		created = ndb.DateTimeProperty()
        self.response.write('Hello world!')

class TemperatureHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('main.html')
		lat = self.request.get('lat')
		lon = self.request.get('lon')
		url = ('http://api.openweathermap.org/data/2.5/weather?' + 
            'lat=%s&lon=%s&units=imperial&APPID=de442c99365c2f7ecb50f91cdbcc3c6bd' % (lat,lon))
		string = urllib2.urlopen(url).read()
		dictionary = json.loads(string)

		if lat == '' or lon == '':
			form = True
			temperature = 'Wating...'
		else:
			form = False
			temperature = dictionary['main']['temp']	
			howhot = ' wating for temperature'

		temp = Temperature(temperature = int(howhot), latitude=lat, longitude= lon, created=datetime.datetime.now())
        temp.put()
		
		template_vars = {'temperature': temperature, 'form':form}
		self.response.write(template.render(template_vars))

s

app = webapp2.WSGIApplication([
    ('/', TemperatureHandler)
], debug=True)
