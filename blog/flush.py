from google.appengine.api import memcache
import webapp2

class FlushHandler(webapp2.RequestHandler):
   
    def get(self):
        memcache.flush_all()
        