import webapp2
import cgi

form = """<form method="post" action="/rot13">
  <h1>Enter some text to ROT13:</h1><br>
    <textarea name='text' cols="50" rows="10">%(rot13)s</textarea>
  </p>
    <input type="submit">
</form>"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form % {"rot13":""})


class Rot13Handler(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        text = self.request.get("text")
        self.response.write(form % {"rot13" : cgi.escape(self.rot13(text), quote='"')})


    def rot13(self, text):
        if text:
            translated = ''
            for c in text:
                if c.isalpha():
                    if c.isupper():
                        translated += chr(ord(c) + 13 if ord(c) + +13 < ord('Z') else ord(c) - 13)
                    else:
                        translated += chr(ord(c) + 13 if ord(c) + +13 < ord('z') else ord(c) - 13)
                else:
                    translated += c
        return translated

application = webapp2.WSGIApplication([('/', MainPage),('/rot13', Rot13Handler)], debug=True)
