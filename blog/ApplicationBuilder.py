from newpost import NewPostHandler
from blog import BlogHandler
from permalink import Permalink
from signup import SignupHandler
from welcomehandler import WelcomeHandler
from login import LoginHandler
from logout import LogoutHandler
import webapp2

application = webapp2.WSGIApplication([('/blog/newpost', NewPostHandler),('/blog', BlogHandler),('/blog/(\d+)',Permalink),
                                       ('/signup', SignupHandler),('/welcome',WelcomeHandler),('/login',LoginHandler),('/logout',LogoutHandler)], debug=True)