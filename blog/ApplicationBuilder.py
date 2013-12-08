from newpost import NewPostHandler
from mainpage import MainPageHandler
import webapp2

application = webapp2.WSGIApplication([('/newpost', NewPostHandler),('/blog', MainPageHandler)], debug=True)

