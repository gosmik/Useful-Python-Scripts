import json
from pprint import pprint

with open('jsonfile.json') as f:
    jsonObject = json.load(f)

def parseJson(_value):
    if isinstance(_value,dict):
        for k1,v1 in _value.items():
            if isinstance(v1,dict) or isinstance(v1,list):
                print(k1)
                parseJson(v1)
            else:
                print("\t"+ k1 + " " + str(v1))
    elif isinstance(_value,list):
        for it in _value:
            if isinstance(it,dict) or isinstance(it,list):
                parseJson(it)
            else:
                print("list\t"+ str(it))
    else:
        print("***************NOT HANDLED CASE***************")
    return

def findInJson(_value, _find):
    if isinstance(_value,dict):
        for k1,v1 in _value.items():
            if(k1 == _find):
                print("FOUND")
            elif isinstance(v1,dict) or isinstance(v1,list):
                findInJson(v1, _find)
    elif isinstance(_value,list):
        for it in _value:
            if isinstance(it,dict) or isinstance(it,list):
                findInJson(it, _find)
    else:
        print("***************NOT HANDLED CASE***************")
    return


#for key, value in jsonObject.items():
# parseJson(jsonObject)
findInJson(jsonObject, "pSozlesmeTarih")


#pprint(jsonObject)