from templatehandler import TemplateHandler
from entities import BlogPost;

class BlogHandler(TemplateHandler):
    templatename = 'blog.html'
    def get(self):
        posts_query = BlogPost.query()
        blogposts = posts_query.fetch(15)       
        template_values = {'blogposts': blogposts}
        self.render(self.templatename,template_values)