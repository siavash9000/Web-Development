from templatehandler import TemplateHandler
from entities import BlogPost;

class MainPageHandler(TemplateHandler):
    templatename = 'mainpage.html'
    def get(self):
        posts_query = BlogPost.query()
        blogposts = posts_query.fetch(15)       
        template_values = {'blogposts': blogposts}
        self.render(self.templatename,template_values)