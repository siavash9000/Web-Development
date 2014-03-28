from templatehandler import TemplateHandler
from entities import WikiPage;
from google.appengine.api import memcache           
import datetime
class EditHandler(TemplateHandler):
    templatename = 'edit.html'
    def get(self, url):    
        template_values = {"action": "/_edit"+url,"content":self.getContent(url)}  
        self.render(self.templatename,template_values)

    def post(self,url):
        content = self.request.get("content")        
        if (not content):
            template_values = {"error": "Please enter content.","content":content}
            self.render(self.templatename,template_values)
        else:
            self.persist(url,content)
            print url
            self.redirect(url)
    
    def persist(self, url,content):
        page_query = WikiPage.query(WikiPage.url == url)
        page = page_query.fetch(1)
        if len(page)==0:
            newPage = WikiPage()
        else:
            newPage = page[0]
        newPage.url = url
        newPage.content = content
        newPage.put()
        print url
        memcache.add(url,content)
        lastUpdate = datetime.datetime.now()
        memcache.add('lastUpdate_'+url,lastUpdate)
    
    def getContent(self,url):
        page_query = WikiPage.query(WikiPage.url == url)
        page = page_query.fetch(1)
        if len(page)==0:
            return ''
        else:
            return page[0].content