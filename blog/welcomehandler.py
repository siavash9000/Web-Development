import webapp2
from entities import User
from hashing import hasher

class WelcomeHandler(webapp2.RequestHandler):
    hasher = hasher()
    def get(self):
        userid_cookie = self.request.cookies.get('userid')
        if userid_cookie and len(userid_cookie) > 0:
            userid = int(userid_cookie.split("|")[0])  
            user = User.get_by_id(userid)
            if not user:
                self.response.headers.add_header('Set-Cookie','userid=;Path=/')
                self.response.write("Welcome!")        
            else:
                if self.hasher.check_secure_val(userid_cookie):
                    self.response.write("Welcome "+user.username+" !")
        else:
            self.response.write("Welcome Cookie-less Stranger!")

