from blog.newpost import NewPostHandler

__author__ = 'siavash'
import webapp2

application = webapp2.WSGIApplication([('/newpost', NewPostHandler)], debug=True)
