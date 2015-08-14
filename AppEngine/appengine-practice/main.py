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

############################# NOTES #####################################
#Client/ Server
# 1. (broswer) client makes a request
# 2. server processess
# 3. Server responds
# 4. client redners
# POST - sending data out , GET - requesting a link
# How do we attach this to html and the front-back
# When we want to send a lot of data we use a POST
# a GET method has a limit of only 255 characters. Because it uses the URLsere.
import webapp2
import math
import logging
import jinja2
import os
import time

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'timeofday': time.asctime(),
            'filepath': os.path.dirname(__file__)
            }

        template = jinja_environment.get_template('templates/hello.html')
        self.response.write(template.render(template_vars))
        # self.response.write('<a href ="add?left=41&right=23">ADD</a>')
        # self.response.write('<a href ="subtract?left=41&right=23">SUBTRACT</a>')
        # self.response.write('<a href ="mod?left=41&right=23">MOD</a>')

class FormHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('realname', default_value='Friend')
        self.response.write('Hi '+ name)


class Calculator(webapp2.RequestHandler):
    def post(self):
        # form = cgi.FieldStorage()
        number1 = self.request.get('number1')
        number2 = self.request.get('number2')
        number1 = float(number1)
        number2 = float(number2)
        operations = self.request.get('operations')
        if operations == 'add':
            self.response.write((int(number1)) + (int((number2))))
        elif operations == 'subtract':
            self.response.write((int(number1)) - (int((number2))))
        elif operations == 'multiply':
            self.response.write((int(number1)) * (int((number2))))
        elif operations == 'divide':
            self.response.write((int(number1) / (int(number2))))



jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/formhandler', FormHandler),
    ('/calculator', Calculator)
], debug=True)
