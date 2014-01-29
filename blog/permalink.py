from templatehandler import TemplateHandler
from entities import BlogPost
from json_utils import DateTimeEncoder
import webapp2, json, datetime, math
from google.appengine.api import memcache

class Permalink(TemplateHandler):
    templatename = 'blog.html'
    def get(self, post_id):
        post = memcache.get(post_id)
        lastUpdate = memcache.get('lastUpdate_'+post_id)
        if not post or not lastUpdate:
            post = BlogPost.get_by_id(int(post_id))
            memcache.add(post_id,post)
            lastUpdate = datetime.datetime.now()
            memcache.add('lastUpdate_'+post_id,lastUpdate)
            
        age = int(math.ceil((datetime.datetime.now() - lastUpdate).total_seconds()-1))    
        ageString = 'Queried {} seconds ago'.format(age)
               
        template_values = {'blogposts': [post], 'id':post_id, 'age': ageString}
        self.render(self.templatename, template_values)
        
        
class PermalinkJson(webapp2.RequestHandler):
    def get(self, post_id):
        post = BlogPost.get_by_id(int(post_id))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(post.to_dict(), cls=DateTimeEncoder))