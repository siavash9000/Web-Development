import webapp2
import re
from templatehandler import TemplateHandler
from entities import User
import hashlib
from hashing import hasher
from google.appengine.ext import ndb

class SignupHandler(TemplateHandler):
    templatename = 'signup.html'
    usernameregex = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    passwordregex = re.compile("^.{3,20}$")
    emailregex = re.compile("^[\S]+@[\S]+\.[\S]+$")
    hasher = hasher()
    def get(self):
        self.render(self.templatename)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        passwordverify = self.request.get("verify")
        email = self.request.get("email")
        self.validateForm(username, password, passwordverify, email)
           
    def validateForm(self,username, password, passwordverify, email=""):
        usernameerror=""
        passworderror=""
        passwordverifyerror=""
        emailerror=""
        if not username or not self.usernameregex.match(username):
            usernameerror="invalid username"
        elif not password or not self.passwordregex.match(password):
            passworderror = "invalid password"
        elif not passwordverify or not passwordverify == password:
            passwordverifyerror="passwordverify does not match password"
        elif email and not self.emailregex.match(email):
            emailerror="invalid email"
        else:
            userid = self.persistUser(username,email,password)
            hashed_userid = self.hasher.make_secure_val(str(userid))
            print "userid : ",hashed_userid
            self.response.headers.add_header('Set-Cookie','userid=%s' % hashed_userid)
            self.redirect("/welcome")
        templatevariables = {"usernameerror":usernameerror,"passworderror":passworderror,
                             "passwordverifyerror":passwordverifyerror,"emailerror":emailerror}
        self.render(self.templatename,templatevariables)
        
    def persistUser(self,username,email,password):
        user = User()
        user.username = username
        user.hashed_password = hashlib.sha256(password).hexdigest()
        user.email = email
        return user.put().id()      