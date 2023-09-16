import xml.sax

class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current=name
        if self.current=='person':
            print('__PERSON__')
            print('ID--:{}'.format(attrs['id']))

    def characters(self, content):
        if self.current=='name':
            self.name=content
            
        elif self.current=='age':
            self.age=content
            
        elif self.current=='weight':
            self.weight=content
            
        elif self.current=='height':
            self.height=content

    def endElement(self, name):
    
        if self.current=='name':
            print('NAME: {}'.format(self.name))
    
        elif self.current=='age':
            print('AGE: {}'.format(self.age))
    
        elif self.current=='height':
            print('HEIGHT: {}'.format(self.height))
        
        elif self.current=='weight':
            print('WEIGHT: {}'.format(self.weight))
        

handler=GroupHandler()
parser=xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')
