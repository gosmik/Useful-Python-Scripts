import xml.etree.cElementTree as ET
import json
from pprint import pprint

tree = ET.ElementTree(file='doc2.xml')
root = tree.getroot()
print("Root: %s \n" %root.tag)

def parseXml(_node):
    print (_node.tag, _node.text)
    for it1 in _node:
        for it2 in it1:
            parseXml(it2)

# parseXml(root)

for elem in root.iter():
    print (elem.tag, elem.text)

# for elem in root.iter("pSozlesmeTarih"):
#     for elem2 in elem.iter("Gun"):
#         print (elem2.tag , elem2.text)