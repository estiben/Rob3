import xml.sax

class RoomSAXContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.paramList = []
        self.currentElement = ''
        self.currentClass = ''

    def startElement(self, name, attrs):
        self.currentElement = name
        if name == 'tile':
            print('tile')
        elif name == 'object':
            self.currentClass = attrs.getValue('class')
 
    def endElement(self, name):
        if name == 'object':
            eval(self.currentClass + '()')
            self.paramList = []
 
    def characters(self, content):
        if self.currentElement == 'param':
            self.paramList.append(content)
 
def loadRoom(name):
    roomFilePath = os.path.join('data', 'rooms', name) +'.xml'
    source = open(roomFilePath,'r')
    
    xml.sax.parse(source, RoomSAXContentHandler())
    source.close()
 
