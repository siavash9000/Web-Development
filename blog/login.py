import webapp2
import re
from templatehandler import TemplateHandler
from entities import User
import hashlib
from hashing import hasher
from google.appengine.ext import ndb
import hashlib

class LoginHandler(TemplateHandler):
    templatename = 'login.html'
    usernameregex = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    passwordregex = re.compile("^.{3,20}$")
    hasher = hasher()
    def get(self):
        self.render(self.templatename)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        self.validateForm(username, password)
           
    def validateForm(self,username, password):
        error=""
        user_id=self.find_user(username,password)
        if user_id == None:
            error="invalid login data"
        else:
            hashed_userid = self.hasher.make_secure_val(str(user_id))
            self.response.headers.add_header('Set-Cookie','userid=%s' % hashed_userid)
            self.redirect("/welcome")
        templatevariables = {"error":error}
        self.render(self.templatename,templatevariables)
        
    def find_user(self,username,password):
        if not username or not self.usernameregex.match(username) or not password or not self.passwordregex.match(password):
            return None
        query_result = User.query(User.username == username).fetch(1)
        if len(query_result)==0:
            return None
        user = query_result[0]
        password_input = hashlib.sha256(password).hexdigest()
        if not user.hashed_password == password_input:
            return None
        return user.key.id()