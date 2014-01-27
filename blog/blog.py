from templatehandler import TemplateHandler
from entities import BlogPost;
from time import mktime
from json_utils import DateTimeEncoder
import json, webapp2, datetime

class BlogHandler(TemplateHandler):
    templatename = 'blog.html'
    def get(self):
        posts_query = BlogPost.query()
        blogposts = posts_query.fetch(15)       
        template_values = {'blogposts': blogposts}
        self.render(self.templatename,template_values)
  
class BlogHandlerJson(webapp2.RequestHandler):
    templatename = 'blog.html'
    def get(self):
        posts_query = BlogPost.query()
        blogposts = posts_query.fetch(15)   
        posts_dict = []
        for post in blogposts:
            posts_dict.append(post.to_dict()) 
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(posts_dict, cls=DateTimeEncoder))