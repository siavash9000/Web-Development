from templatehandler import TemplateHandler
from entities import WikiPage
from json_utils import DateTimeEncoder
import webapp2, json, datetime, math
from google.appengine.api import memcache

class HistoryPageHandler(TemplateHandler):
    templatename = 'history.html'
    def get(self, page_url):
        page_query = WikiPage.query(WikiPage.url == page_url).order(-WikiPage.date)
        pages = page_query.fetch()
        if len(pages)==0:
            self.redirect("/_edit"+page_url)
            return
        else:
            template_values = {'id':page_url, 'history':pages,'editlink':'/_edit'+page_url,'viewlink':page_url}
            self.render(self.templatename, template_values)
        
        
class PermalinkJson(webapp2.RequestHandler):
    def get(self, post_id):
        post = BlogPost.get_by_id(int(post_id))
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(post.to_dict(), cls=DateTimeEncoder))