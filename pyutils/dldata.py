# this is a class holding data for dreamlog plot

import csv

class Dldata():
  def __init__(self, csvdata, txtdata):
    self.date=list()
    self.time=list()
    self.snr=list()
    self.audiook=list()
    self.doppler=list()
    self.delay=list() 
    for line in csvdata.splitlines():
      dta=line.split(',') 
      self.date.append(dta[1])
      self.time.append(dta[2])
      self.snr.append(dta[3])
      self.audiook.append(dta[8])
      self.doppler.append(dta[9])
      self.delay.append(dta[10])
    
    self.headerData=txtdata

  @property
  def getDate(self):
    return self.date

  @property
  def getTime(self):
    return self.time

  @property
  def getSnr(self):
    return self.snr

  @property
  def getAudiook(self):
    return self.audiook

  @property
  def getDoppler(self):
    return self.doppler

  @property
  def getDelay(self):
    return self.delay

  @property
  def getHeader(self):
    return self.headerData
