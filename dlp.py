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

print('Hey Old Man, wir haben ', length, 'Logs')
inpt=input('welches willst du sehen? ')
l=int(inpt)
l=l-1
if l < 0 or l > length:
  print('Auswahl nicht verfügbar')
  sys.exit()

import matplotlib.pyplot as plt

# 1. Daten (in Listenform) an die Kurven übergeben
x = logs[l].getTime #Gemeinsame x-Achse (optional)
y1 = logs[l].getAudiook
y2 = logs[l].getSnr
y3 = logs[l].getDoppler
y4 = logs[l].getDelay

# 2. Plot erstellen
# label= dient dazu, die Legende später zu beschriften
plt.plot(x, y1, label='Audiook', color='red', linestyle='-')
plt.plot(x, y2, label='SNR', color='blue', linestyle='--')
plt.plot(x, y3, label='Doppler', color='green', linestyle=':')
plt.plot(x, y4, label='Delay', color='purple', linestyle='-.')

# 3. Diagramm beschriften und verschönern
plt.title("Frequenz: %s" % logs[l].getHeader["Frequency"])
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.legend() # Zeigt die Legende an
plt.grid(True) # Blendet ein Gitter ein

# 4. Diagramm anzeigen
plt.show()

