#!/usr/bin/python

import sys
import os
import xml.etree.ElementTree

xmp_dir = sys.argv[1]
xmp_files = os.listdir(xmp_dir)

def parse_xmp(xmp_path):
	data = {}
	xmp_tree = xml.etree.ElementTree.parse(xmp_path)
	xmp_root = xmp_tree.getroot()
	data['rating'] = xmp_root[0][0].attrib['{http://ns.adobe.com/xap/1.0/}Rating']
	data['label'] = xmp_root[0][0].attrib['{http://ns.adobe.com/xap/1.0/}Label']
	return data

data = {}
for xmp_file in xmp_files:
	data[xmp_file[:-4]] = parse_xmp(os.path.join(xmp_dir, xmp_file))

print(data)
