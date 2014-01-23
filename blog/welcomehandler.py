import webapp2
from entities import User
from hashing import hasher

class WelcomeHandler(webapp2.RequestHandler):
    hasher = hasher()
    def get(self):
        userid_cookie = self.request.cookies.get('userid')
        userid = int(userid_cookie.split("|")[0])  
        user = User.get_by_id(userid)
        if self.hasher.check_secure_val(userid_cookie):
            self.response.write("Welcome "+user.username+" !")
