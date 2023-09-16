import xml.dom.minidom

domtree=xml.dom.minidom.parse('data.xml')

group=domtree.documentElement
persons=group.getElementByTagName('person')

for person in persons:
    print('---PERSON----')
    if person.hasatttribute('Id'):
        print('ID :{}'.format(person.getAttribute('id')))

    print('NAME: {}'.format(person.getElementByTagName('name')[0].childNodes[0].data))