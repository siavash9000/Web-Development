import webapp2
from templatehandler import TemplateHandler

class LogoutHandler(TemplateHandler):

    def get(self):
        self.response.headers.add_header('Set-Cookie','user_id=;Path=/')
        self.redirect("/signup")