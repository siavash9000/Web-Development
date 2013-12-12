from newpost import NewPostHandler
from mainpage import MainPageHandler
from permalink import Permalink
import webapp2

application = webapp2.WSGIApplication([('/blog/newpost', NewPostHandler),('/blog', MainPageHandler),('/blog/(\d+)',Permalink)], debug=True)

