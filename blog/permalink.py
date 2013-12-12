from templatehandler import TemplateHandler
from entities import BlogPost;

class Permalink(TemplateHandler):
    templatename = 'mainpage.html'
    def get(self, post_id):
        post = BlogPost.get_by_id(int(post_id))
        template_values = {'blogposts': [post], 'id':post_id}
        self.render(self.templatename, template_values)