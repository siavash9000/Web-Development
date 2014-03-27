from templatehandler import TemplateHandler
from entities import BlogPost;
            
class NewPostHandler(TemplateHandler):
    templatename = 'newpost.html'
    def get(self):               
        self.render(self.templatename)

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")        
        if (not subject or not content):
            template_values = {"error": "Please enter subject and content.","subject":subject,"content":content}
            self.render(self.templatename,template_values)
        else:
            postid = self.persist(subject,content)
            self.redirect("/blog/"+str(postid))
    
    def persist(self, subject,content):
        newpost = BlogPost();
        newpost.subject = subject;
        newpost.content = content;
        newpost.put()
        return newpost.key.id()