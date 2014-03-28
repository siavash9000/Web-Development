from google.appengine.ext import ndb

class WikiPage(ndb.Model):
    url = ndb.StringProperty(indexed = True)
    content = ndb.TextProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
    
class User(ndb.Model):
    username = ndb.StringProperty(indexed = True)
    hashed_password = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed = True)
    date = ndb.DateTimeProperty(auto_now_add=True)