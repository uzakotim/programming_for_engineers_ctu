import csv

from attr import field
class Util:
  #static fields of a class
  unitNames   = [ 'k', 'K', 'm', 'M', 'g', 'G', 't', 'T', 'p', 'P' ]
  unitValues  = { 'k': 10**3,   'K': 10**3,  \
                  'm': 10**6,   'M': 10**6,  \
                  'g': 10**9,   'G': 10**9,  \
                  't': 10**12,  'T': 10**12, \
                  'p': 10**15,  'P': 10**15  }

   
  @staticmethod
  # returns specific value (None, 0, etc)  when the string is not decoded 
  def strValue( str ):
    specValue = 0
    
    if str in [None, ""]: return specValue
    str = str.strip()  # remowe leading/trailing whitespaces, tabs
    # no unit 
    if str[-1].isdigit():
      try:
        value = int( str )
        return value
      except:
        return specValue
    # unit specified
    else: 
      unitChar = str[-1]
      # unit unknown
      if not unitChar in Util.unitNames:
        return specValue
      # unit known
      try:
        value  =  float( str[:-1] ) 
        return  round( value * Util.unitValues[unitChar] )
      except:
        return specValue
      

# ---------------------------

filename = "../csvdata/net_users_num.csv"

fieldNames = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fieldNames = next(csvreader)
    for row in csvreader:
        rows.append(row)

index = fieldNames.index('2015')
for row in rows:
    rvals = [ Util.strValue(s) for s in row[1:]]
    if rvals[index] < 100000:   
        print(row[0], rvals[index])
# print(fieldNames[index])
