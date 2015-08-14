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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Comments(ndb.Model):
	username = ndb.StringProperty()
	date_created = ndb.DateTimeProperty(auto_now_add=True)
	text = ndb.StringProperty()

class Post(ndb.Model):
	username = ndb.StringProperty()
	date_created = ndb.DateTimeProperty(auto_now_add=True)
	text = ndb.StringProperty()
	likes = ndb.IntegerProperty()
	dislikes = ndb.IntegerProperty()
	comments = ndb.StructuredProperty(Comments, repeated=True)


class BlogHandler(webapp2.RequestHandler):
	def post(self):
		#update blog
		post = Post(username='Splenda', text='Sugar is sweet', likes=0, dislikes=1, comments='')
		post.put()

	def get(self):
		#display all the posts
		post = Post(username='Splenda', text='Sugar is sweet', likes=0, dislikes=1, comments='')
		post.put()		
		posts = Post.query().fetch()
		template = JINJA_ENVIRONMENT.get_template('/templates/posts.html')
		template_vars = {'posts': posts}
		self.response.write(template.render(template_vars))

		#a box for a new post (if you are the signed in user)

JINJA_ENVIRONMENT = jinja2.Environment(loader=
	jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', BlogHandler)
], debug=True)
