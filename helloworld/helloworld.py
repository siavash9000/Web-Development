import webapp2

form = """<form method="post" action="/testform">
<input name = "q">
<input type = "submit">
</form>"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)


class TestHandler(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        q = self.request.get("q")
        #self.response.write(q)

        self.response.write(self.request)

application = webapp2.WSGIApplication([('/', MainPage),('/testform', TestHandler)], debug=True)
