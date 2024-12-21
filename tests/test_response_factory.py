# tests/test_response_factory.py

import pytest
from factories.response_factory import ResponseFactory
from pathlib import Path

def test_create_response():
    #  Define the correct path to the template directory
    BASE_DIR = Path(__file__).resolve().parent.parent
    templates_dir = BASE_DIR / 'templates'
    
    factory = ResponseFactory(template_dir=str(templates_dir))
    
    # Enter the individual variables expected by the template
    context = {
        'task_id': 'test_001',
        'status': 'Success',
        'message': 'Task created successfully'
    }
    
    # Generate response XML
    response_xml = factory.create_response('response_template.xml.jinja2', context)
    
    # Assertions to check that variables are correctly injected
    assert '<TaskID>test_001</TaskID>' in response_xml
    assert '<Status>Success</Status>' in response_xml
    assert '<Message>Task created successfully</Message>' in response_xml
