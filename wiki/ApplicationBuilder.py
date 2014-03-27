from signup import SignupHandler
from login import LoginHandler
from logout import LogoutHandler

import webapp2

DEBUG = True
PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
app = webapp2.WSGIApplication([('/signup', SignupHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler),
                               ('/_edit' + PAGE_RE, EditPage),
                               (PAGE_RE, WikiPage),
                               ],
                              debug=DEBUG)