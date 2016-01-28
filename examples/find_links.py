#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DHTMLParserPy example how to find every link in document.
"""

import urllib.request
import dhtmlparser

f = urllib.request.urlopen("http://google.com")
data = f.read().decode("utf-8", "replace")
f.close()

dom = dhtmlparser.parseString(data)

for link in dom.find("a"):
	if "href" in link.params:
		print(link.params["href"])
