#!/usr/bin/env python3

import sys
import csv
import tempfile
import matplotlib as plt
from pyutils.fileSplit import splitTextfileByBlankLines

csvContent=splitTextfileByBlankLines(sys.argv[1])

for element in csvContent:
  print(element)


