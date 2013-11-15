import webapp2
import cgi
import re

form = """
<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="">
          </td>
          <td class="error">
            %(usernameerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="">
          </td>
          <td class="error">
            %(passworderror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="">
          </td>
          <td class="error">
            %(passwordverifyerror)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="">
          </td>
          <td class="error">
            %(emailerror)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.redirect("/signup")

class SignupHandler(webapp2.RequestHandler):

    usernameregex = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    passwordregex = re.compile("^.{3,20}$")
    emailregex = re.compile("^[\S]+@[\S]+\.[\S]+$")

    def write_from(self,usernameerror="", passworderror="", passwordverifyerror="", emailerror=""):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form % {"usernameerror":usernameerror,"passworderror":passworderror
        ,"passwordverifyerror":passwordverifyerror,"emailerror":emailerror})

    def get(self):
        self.write_from()

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        username = self.request.get("username")
        password = self.request.get("password")
        passwordverify = self.request.get("verify")
        email = self.request.get("email")
        if not username or not self.usernameregex.match(username):
            self.write_from("invalid username")
        elif not password or not self.passwordregex.match(password):
            self.write_from("","invalid password")
        elif not passwordverify or not passwordverify == password:
            self.write_from("","","passwordverify does not match password")
        elif email and not self.emailregex.match(email):
            self.write_from("","","","invalid email")
        else:
            self.redirect("/welcome"+"?username="+username)

class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome "+username+"!")

application = webapp2.WSGIApplication([('/', MainPage),('/signup', SignupHandler),('/welcome',WelcomeHandler)], debug=True)
