from templatehandler import TemplateHandler
from entities import BlogPost
from json_utils import DateTimeEncoder
import webapp2, json

class Permalink(TemplateHandler):
    templatename = 'blog.html'
    def get(self, post_id):
        post = BlogPost.get_by_id(int(post_id))
        template_values = {'blogposts': [post], 'id':post_id}
        self.render(self.templatename, template_values)
        
class PermalinkJson(webapp2.RequestHandler):
    def get(self, post_id):
        post = BlogPost.get_by_id(int(post_id))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(post.to_dict(), cls=DateTimeEncoder))