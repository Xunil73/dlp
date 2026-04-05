def splitTextfileByBlankLines(file):

  with open(file, 'r') as f:
    content=f.read()
    f.close()
    content_list=content.splitlines()


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
    newContents.append('\n'.join(element))

  return newContents

