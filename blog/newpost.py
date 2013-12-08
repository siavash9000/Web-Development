import webapp2
import os
import jinja2
from entities import BlogPost;
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class NewPostHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('newpost.html')
        self.response.write(template.render())

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        subject = self.request.get("subject")
        content = self.request.get("content")
        print (subject + ", " + content)
        self.persist(subject,content)
        self.redirect("/blog")
    
    def persist(self, subject,content):
        newpost = BlogPost();
        newpost.subject = subject;
        newpost.content = content;
        newpost.put()