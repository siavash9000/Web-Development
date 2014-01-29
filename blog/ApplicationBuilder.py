from newpost import NewPostHandler
from blog import BlogHandler, BlogHandlerJson
from permalink import Permalink, PermalinkJson
from signup import SignupHandler
from welcomehandler import WelcomeHandler
from login import LoginHandler
from logout import LogoutHandler
from flush import FlushHandler
import webapp2

application = webapp2.WSGIApplication([('/blog/newpost', NewPostHandler),('/blog', BlogHandler),('/', BlogHandler),
                                       ('/blog/(\d+)',Permalink),('/blog/(\d+).json',PermalinkJson),
                                       ('/blog/signup', SignupHandler),('/blog/welcome',WelcomeHandler),('/blog/login',LoginHandler),
                                       ('/blog/logout',LogoutHandler),('/blog/.json', BlogHandlerJson),('/blog/flush', FlushHandler)], debug=True)