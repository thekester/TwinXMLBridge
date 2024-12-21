# factories/request_factory.py

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class RequestFactory:
    def __init__(self, template_dir=None):
        if template_dir is None:
            # Define BASE_DIR as the project's root directory
            BASE_DIR = Path(__file__).resolve().parent.parent  # TwinXMLBridge/
            template_dir = BASE_DIR / 'templates'
        self.env = Environment(loader=FileSystemLoader(str(template_dir)))
    
    def create_request(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)
