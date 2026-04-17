
# diese Funktion zerlegt eine CSV mit mehreren Logs aus DreamLog in
# einzelne Logs
# Rückgabewert: eine Liste mit den einzelnen Logs 
def splitTextfileByBlankLines(file):

  with open(file, 'r') as f: 
    content=f.read() # wir lesen die Datei so wie sie ist in die Variable content ein.
    f.close()
    content_list=content.splitlines() #hier bekommen wir die Datei in einer Liste mit Zeilen:
                    # so: ['Zeile1', 'das ist Zeile 2', 'zeile3']


  part=[]  # collects ONE related data set
  parts=[] # collects the different data sets,
           # including empty entries that result from blank lines in the source file
  for element in content_list: # hier gehen wir Zeile für Zeile durch die Datei
    if element == '': # wenn eine Leerzeile in der CSV steht taucht sie als leeres Element in 
      parts.append(part) # unserer Liste auf. Das bedeutet automatisch: hier beginnt ein neues Log.
      part=[] # ...und wir fangen von Null an interessante Zeilen zu sammeln.
    else:
      part.append(element) # ist es keine Leerzeile ist es eine die wir brauchen und sammeln sie in die Liste ein.
  parts.remove([]) # wenn alles fertig ist entfernen wir leere Einträge die durch Leerzeichen entstanden.

  newContents=[] # wir wollen eine Liste haben mit allen Logs, aufgetrennt nach Log und in Textform
  for element in parts: # wir durchforsten alle Logs 
    if element != []:
      newContents.append('\n'.join(element)) # und bauen schliesslich alles wieder zu einem Textstring zusammen.

  return newContents # den Textstring (inclusive Zeilenumbruchzeichen) geben wir dem Aufrufer zurück



# diese Funktion extrahiert aus der Textfile von DreamLog (mit mehreren Logs)
# alle Werte und speichert diese in ein Dictionary ab.
# Rückgabewert: eine Liste die ein Dictionary pro Logaufzeichnung enthält.
# Inhalt eines Dicts: siehe "keylist" sowie zusätzlich den key "Dream"
def parseDLtxtToDict(file):

  with open(file, 'r') as f:
    content=f.read()
    f.close()
    content_list=content.splitlines()

  # the key 'Dream' is not in the list because it belongs to the value of the following field in content_list:
  # Pseudocode:  dreamlogHeaderData['Dream'] = content_list[FIELD FOLLOWING THE STRING 'Dream'] 
  keylist=['Starttime (UTC)', 'Frequency', 'Latitude', 'Longitude', 'Label', 'Bitrate', 'Mode', 'Bandwidth', 'SNR', 'CRC:']

  headerDatas=[]
  dreamlogHeaderData=dict()

  i=-1
  for cl in content_list:
    i+=1
    if cl == 'Dream':
      dreamlogHeaderData['Dream']=content_list[i+1]
    elif cl == '<<<<':
      headerDatas.append(dreamlogHeaderData)
      dreamlogHeaderData={}
    else:
      for kl in keylist:
        if cl.startswith(kl):
          dreamlogHeaderData[kl]=cl.replace(kl, ' ').strip()

  return headerDatas
