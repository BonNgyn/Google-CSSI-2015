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
import datetime
from google.appengine.ext import ndb
import logging
import json


class Temperature(ndb.Model):
	temperature = ndb.IntegerProperty()
	latitude = ndb.FloatProperty()
	longitude = ndb.FloatProperty()
	created = ndb.DateTimeProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
		howhot = ' wating for temperature'

		temp = Temperature(temperature = int(howhot), latitude=lat, longitude= lon, created=datetime.datetime.now())
        temp.put()
        # query = User.query()
        # data = query.fetch()
        # logging.info(data)

JINJA_ENVIRONMENT = jinja2.Environment(loader=
	jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
