# client/twinxml_client.py

import sys
from pathlib import Path

# Define the project's base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the base directory to sys.path
sys.path.append(str(BASE_DIR))

from factories.request_factory import RequestFactory
from factories.response_factory import ResponseFactory
from utils.xml_validator import XMLValidator

import requests

class TwinXMLClient:
    def __init__(self, server_url, xsd_path, templates_dir='templates'):
        self.server_url = server_url
        self.request_factory = RequestFactory(template_dir=templates_dir)
        self.response_factory = ResponseFactory(template_dir=templates_dir)
        self.validator = XMLValidator(xsd_path)
    
    def send_task_create(self, task_data):
        # Gnerate the XML request
        request_xml = self.request_factory.create_request('request_template.xml.jinja2', task_data)
        
        # Validate the XML
        is_valid, error = self.validator.validate(request_xml)
        if not is_valid:
            raise ValueError(f"XML Request validation failed: {error}")
        
        # Send request to server
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(self.server_url, data=request_xml, headers=headers)
        
        if response.status_code != 200:
            raise ConnectionError(f"Server responded with status code {response.status_code}")
        
        # Validate the answer
        is_valid, error = self.validator.validate(response.text)
        if not is_valid:
            raise ValueError(f"XML Response validation failed: {error}")
        
        # Processing the response
        response_data = self.response_factory.create_response('response_template.xml.jinja2', {
            'task_id': 'test_001',
            'status': 'Success',
            'message': 'Task created successfully'
        })
        return response_data

def main():
    server_url = 'http://localhost:5000/'
    xsd_path = BASE_DIR / 'schemas' / 'schema.xsd'
    templates_dir = BASE_DIR / 'templates'
    
    client = TwinXMLClient(server_url=server_url, xsd_path=str(xsd_path), templates_dir=str(templates_dir))
    
    task_data = {
        'task_id': 'task_001',
        'description': 'Analyze network logs',
        'priority': 'High'
    }
    
    try:
        response = client.send_task_create(task_data)
        print("Server Response:", response)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
