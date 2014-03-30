from signup import SignupHandler
from login import LoginHandler
from logout import LogoutHandler
from welcomehandler import WelcomeHandler
from edit import EditHandler
from wikipage import WikiPageHandler
from history import HistoryPageHandler

import webapp2

DEBUG = True
PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
application = webapp2.WSGIApplication([('/signup', SignupHandler),
                               ('/login', LoginHandler),
                               ('/logout', LogoutHandler),
                               ('/welcome',WelcomeHandler),
                               ('/_edit' + PAGE_RE, EditHandler),
                               ('/_history' + PAGE_RE, HistoryPageHandler),
                               (PAGE_RE, WikiPageHandler),
                               ],
                              debug=DEBUG)