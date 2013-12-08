from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    subject = ndb.StringProperty(indexed = True)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)