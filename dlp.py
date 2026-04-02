#!/usr/bin/env python3

import sys
import csv

with open(sys.argv[1]) as csvfile:
    csv_reader_object=csv.reader(csvfile, delimiter=',')
    print(csv_reader_object)


