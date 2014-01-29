from templatehandler import TemplateHandler
from entities import BlogPost;
from time import mktime
from json_utils import DateTimeEncoder
import json, webapp2, datetime, math
from google.appengine.api import memcache

class BlogHandler(TemplateHandler):
    templatename = 'blog.html'
    
    def get(self):
        posts_query = BlogPost.query()
        blogposts = memcache.get('blogposts')
        lastUpdate = memcache.get('lastUpdate')
        if not blogposts or not lastUpdate:
            blogposts = posts_query.fetch(15)
            memcache.add('blogposts',blogposts)
            lastUpdate = datetime.datetime.now()
            memcache.add('lastUpdate',lastUpdate)
             
        
        age = int(math.ceil((datetime.datetime.now() - lastUpdate).total_seconds()-1))    
        ageString = 'Queried {} seconds ago'.format(age)
        template_values = {'blogposts': blogposts, 'age': ageString}
        #print datetime.datetime.now()
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