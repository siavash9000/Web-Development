import webapp2
import os
import jinja2
from entities import BlogPost;
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('mainpage.html')
        posts_query = BlogPost.query()
        blogposts = posts_query.fetch(15)
        
        template_values = {
            'blogposts': blogposts,
        }

        self.response.write(template.render(template_values))