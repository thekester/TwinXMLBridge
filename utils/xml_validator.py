from lxml import etree

class XMLValidator:
    def __init__(self, xsd_path):
        with open(xsd_path, 'rb') as f:
            schema_doc = etree.parse(f)
            self.schema = etree.XMLSchema(schema_doc)
    
    def validate(self, xml_content):
        try:
            doc = etree.fromstring(xml_content.encode('utf-8'))
            self.schema.assertValid(doc)
            return True, None
        except etree.DocumentInvalid as e:
            return False, str(e)
