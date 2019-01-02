#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# txt
from urllib.request import urlopen
# textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
# print(textPage.read())

# csv
from io import StringIO
import csv
# data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii',errors='ignore')
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
# for row in csvReader:
	# print(row)

# dictReader = csv.DictReader(dataFile)	 # ['Name', 'Year']
# print(dictReader.fieldnames)
# for row in dictReader:
# 	print(row)		# OrderedDict([('Name', "Monty Python's Flying Circus"), ('Year', '1970')])

# word
# 
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
# print(xml_content.decode('utf-8'))
wordObj = BeautifulSoup(xml_content.decode('utf-8'),"lxml")
# print(type(wordObj))
textStrings = wordObj.findAll("w:t")
# print(textStrings)
for textElem in textStrings:
	for textElem in textStrings:
		closeTag = ""
		try:
			style = textElem.parent.previousSibling.find("w:pstyle")
			if style is not None and style["w:val"] == "Title":
				print("<h1>")
				closeTag = "</h1>"
		except AttributeError:     #不打印标签
			pass
		print(textElem.text)
		print(closeTag)
