# tests/test_request_factory.py

import pytest
from factories.request_factory import RequestFactory
from pathlib import Path

def test_create_request():
    #  Define the correct path to the template directory
    BASE_DIR = Path(__file__).resolve().parent.parent
    templates_dir = BASE_DIR / 'templates'
    
    factory = RequestFactory(template_dir=str(templates_dir))
    context = {
        'task_id': 'test_001',
        'description': 'Test description',
        'priority': 'Low'
    }
    request_xml = factory.create_request('request_template.xml.jinja2', context)
    assert '<TaskID>test_001</TaskID>' in request_xml
    assert '<Description>Test description</Description>' in request_xml
    assert '<Priority>Low</Priority>' in request_xml
