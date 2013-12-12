import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class TemplateHandler(webapp2.RequestHandler):
    
    def render(self,templatename,templatevariables=None):
        self.response.headers['Content-Type'] = 'text/html' 
        template = JINJA_ENVIRONMENT.get_template(templatename)
        if templatevariables:
            self.response.write(template.render(templatevariables))
        else:
            self.response.write(template.render())