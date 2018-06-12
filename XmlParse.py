import xml.etree.cElementTree as ET
import json
from pprint import pprint

tree = ET.ElementTree(file='doc2.xml')
root = tree.getroot()
print("Root: %s \n" %root.tag)

def parseXml(_node):
    print (_node.tag, _node.text)
    for it1 in _node:
        for it2 in it1.getchildren():
            parseXml(it2)

parseXml(root)