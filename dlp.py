#!/usr/bin/env python3

import sys
import csv
import tempfile
import matplotlib as plt
from pyutils.fileSplit import splitTextfileByBlankLines, parseDLtxtToDict
from pyutils.dldata import dldata

csvContents=splitTextfileByBlankLines(sys.argv[1])


textContent=parseDLtxtToDict(sys.argv[2])


logs=list()

length=len(csvContents)
i=0
while i < length:
  logs.append(dldata(csvContents[i], textContent[i]))
  i+=1

print(logs[1].getDate)
print(logs[1].getTime)
header=logs[1].getHeader
for element in header:
  print(element)

