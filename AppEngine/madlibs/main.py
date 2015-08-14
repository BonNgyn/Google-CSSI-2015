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
import jinja2
import os
from google.appengine.api import users
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            entry = jinja_environment.get_template('templates/entry.html')
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url(self.response.write(entry.render()))))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            
            

        self.response.out.write('<html><body>%s</body></html>' % greeting)

class ByeByeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>HI</body></html>')
        

class ResponseHandler(webapp2.RequestHandler):
    def post(self):

        url = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=puppies"
        result = urllib2.urlopen(url)

        puppies = json.loads(result.read())
        puppiesgif = puppies['data']['image_url']

        pluralnoun1 = self.request.get('pluralnoun1')
        adje = self.request.get('adje')
        pluralnoun2 = self.request.get('pluralnoun2')
        verbing = self.request.get('verbing')
        pluralnoun3 = self.request.get('pluralnoun3')
        verbing2 = self.request.get('verbing2')
        pluralnoun4 = self.request.get('pluralnoun4')
        verbing3 = self.request.get('verbing3')

        # listOfWords = self.request.GET(
        #     'pluralnoun4', 'pluralnoun3', 'pluralnoun2', 'pluralnoun1',
        #     'adje', 'verbing', 'verbing2', 'verbing3'
        # )
        dict_words = {
            'pluralnoun1': pluralnoun1,
            'adje':adje,
            'pluralnoun2':pluralnoun2,
            'verbing':verbing,
            'pluralnoun3':pluralnoun3,
            'verbing2':verbing2,
            'pluralnoun4':pluralnoun4,
            'verbing3':verbing3,
            'puppiesgif':puppiesgif
            }
        page = jinja_environment.get_template('templates/response.html')
        self.response.write(page.render(dict_words))

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/response', ResponseHandler),
    ('/byebye', ByeByeHandler)
], debug=True)
