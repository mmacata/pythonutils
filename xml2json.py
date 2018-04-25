#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Requirements:
  * pip install xmltodict
  * if you prefer a virtualenvironment:
    * virtualenv -p python3.5 venv
    * . venv/bin/activate


example xml for testing: https://eome.mundialis.de/eome/opensearch.action?q=satellite%3D%27landsat8%27&count=1


Workflow:
  * save xml to file (e.g. with curl):
    * curl -o myxml.xml 'https://eome.mundialis.de/eome/opensearch.action?q=satellite%3D%27landsat8%27&count=1'
  * start virtualenvironment if wanted (see above)
  * call script with "python xml2json.py myxml.xml outputjson.json"


"""

import sys
import json
import pprint

import xmltodict

xmlfilename = sys.argv[1]
jsonfilename = sys.argv[2]

with open(xmlfilename) as xmlfile:
    print("reading xml file: " + xmlfilename)
    xml = xmlfile.read()
    dict = xmltodict.parse(xml)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dict)

    json = json.dumps(dict)

    with open(jsonfilename, 'w') as jsonfile:
        print("writing json file: " + jsonfilename)
        jsonfile.write(json)
