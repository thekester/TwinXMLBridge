# server/twinxml_server.py

import sys
from pathlib import Path

#Define BASE_DIR as the project's root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add BASE_DIR to sys.path
sys.path.append(str(BASE_DIR))

from factories.request_factory import RequestFactory
from factories.response_factory import ResponseFactory
from utils.xml_validator import XMLValidator

from flask import Flask, request, Response

app = Flask(__name__)

class TwinXMLServer:
    def __init__(self, xsd_path, templates_dir='templates'):
        self.request_factory = RequestFactory(template_dir=templates_dir)
        self.response_factory = ResponseFactory(template_dir=templates_dir)
        self.validator = XMLValidator(xsd_path)
        self.setup_routes()
    
    def setup_routes(self):
        @app.route('/', methods=['POST'])
        def handle_request():
            xml_content = request.data.decode('utf-8')
            
            # Validate the XML
            is_valid, error = self.validator.validate(xml_content)
            if not is_valid:
                return Response(f"Invalid XML: {error}", status=400)
            
            # Processing the request
            task_data = self.parse_task_create(xml_content)
            
            # Generate the response XML with the correct template
            response_xml = self.response_factory.create_response('response_template.xml.jinja2', task_data)
            
            # Validate teh response
            is_valid, error = self.validator.validate(response_xml)
            if not is_valid:
                return Response(f"Invalid XML Response: {error}", status=500)
            
            return Response(response_xml, status=200, mimetype='application/xml')
    
    def parse_task_create(self, xml_content):
        # Return a dict with necessary datas
        return {
            'task_id': '12345',
            'status': 'Success',
            'message': 'Task created successfully'
        }
    
    def run(self, host='0.0.0.0', port=5000):
        app.run(host=host, port=port)

def main():
    # Define the absolute path to the schema and templates
    xsd_path = BASE_DIR / 'schemas' / 'schema.xsd'
    templates_dir = BASE_DIR / 'templates'
    
    server = TwinXMLServer(xsd_path=str(xsd_path), templates_dir=str(templates_dir))
    server.run()

if __name__ == '__main__':
    main()
