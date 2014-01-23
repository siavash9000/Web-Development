from newpost import NewPostHandler
from mainpage import MainPageHandler
from permalink import Permalink
from signup import SignupHandler
from welcomehandler import WelcomeHandler
import webapp2

application = webapp2.WSGIApplication([('/blog/newpost', NewPostHandler),('/blog', MainPageHandler),('/blog/(\d+)',Permalink),('/signup', SignupHandler),('/welcome',WelcomeHandler)], debug=True)

