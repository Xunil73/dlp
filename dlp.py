#!/usr/bin/env python3

import sys
import csv
import tempfile
import matplotlib as plt
from pyutils.fileSplit import splitTextfileByBlankLines, parseDLtxtToDict
from pyutils.dldata import Dldata

csvContents=splitTextfileByBlankLines(sys.argv[1])


textContent=parseDLtxtToDict(sys.argv[2])


logs=list()

length=len(csvContents)
i=0
while i < length:
  logs.append(Dldata(csvContents[i], textContent[i]))
  i+=1

print(logs[2].getDate)
print(logs[2].getTime)
header=logs[2].getHeader
for key, value in header.items():
  print(key, ': ', value)

