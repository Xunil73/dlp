
# diese Funktion zerlegt eine CSV mit mehreren Logs aus DreamLog in
# einzelne Logs
# Rückgabewert: eine Liste mit den einzelnen Logs 
def splitTextfileByBlankLines(file):

  with open(file, 'r') as f:
    content=f.read()
    f.close()
    content_list=content.splitlines()

  # wir schneiden hier die Headerzeilen der CSV-Datei(en) ab
  # hier müssen wir Einträge die mit 'FREQ' anfangen aus der Liste löschen...
  removeContent = [x for x in content_list if x.startswith('FREQ')]
  for i in removeContent:
    if i in content_list:
      content_list.remove(i)


  part=[]  # collects ONE related data set
  parts=[] # collects the different data sets,
           # including empty entries that result from blank lines in the source file
  for element in content_list:
    if element == '':
      parts.append(part)
      part=[]
    else:
      part.append(element)
  parts.remove([])

  newContents=[]
  for element in parts:
    if element != []:
      newContents.append('\n'.join(element))

  return newContents



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
