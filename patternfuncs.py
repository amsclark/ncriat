import re


def getCountyOrDistrict(docket_block):
  pattern = "In the (County|District) Court of .* County"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not identify court"
  else:
    matching_line = x.group()
    return matching_line.strip().split('In the ')[1].split(' Court of ')[0]
  
def getCountyFromCaption(docket_block):
  pattern = "In the (County|District) Court of .* County"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not identify County from Caption"
  else:
    matching_line = x.group()
    return matching_line.strip().split('Court of ')[1].split(' County')[0]
  
def getCaseNumber(docket_block):
  pattern = "The Case ID is  [a-zA-Z][a-zA-Z] \d\d \d*"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not identify case number"
  else:
    matching_line = x.group()
    #print(matching_line)
    return matching_line.strip().split('Case ID is ')[1].strip()
  
def getCaseTitle(docket_block):
  pattern = "\s*.*\sv\.\s.*"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not find case title"
  else:
    matching_line = x.group()
    #print(matching_line)
    return matching_line.strip()
  
def getClassification(docket_block):
  pattern = "Classification: (Misdemeanor|Felony|Statute)"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not identify classification"
  else:
    matching_line = x.group()
    return matching_line.split("Classification: ")[1].strip()
  
def getFilingDate(docket_block):
  pattern = "Filed on \d\d\/\d\d\/\d\d\d\d\s*by (the County|the District|City) Prosecutor"
  x = re.search(pattern, docket_block)  
  if (x is None):
    return "Could not identify filing date"
  else:
    matching_line = x.group()
    return matching_line.split('by ')[0].split('Filed on')[1].strip()
  
def getProsecutor(docket_block):
  pattern = "Filed on \d\d\/\d\d\/\d\d\d\d\s*by (the County|the District|City) Prosecutor"
  x = re.search(pattern, docket_block)  
  if (x is None):
    return "Could not identify prosecutor"
  else:
    matching_line = x.group()
    return matching_line.split('by')[1].strip()
  
def getCaseStatus(docket_block):
  pattern = "This case is (Closed|Open) as of \d\d\/\d\d\/\d\d\d\d"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not identify case status"
  else: 
    matching_line = x.group()
    return matching_line.split("case is")[1].split("as of")[0].strip()
  
def getStatusDate(docket_block):
  pattern = "This case is (Closed|Open) as of \d\d\/\d\d\/\d\d\d\d"
  x = re.search(pattern, docket_block)
  if (x is None):
    return "Could not identify case status date"
  else: 
    matching_line = x.group()
    return matching_line.split("as of")[1].strip()

def getDisposition(docket_block):
  pattern = "It was disposed as  .*\s"
  x = re.search(pattern, docket_block)
  if (x is None):
    return ""
  else:
    matching_line = x.group()
    return matching_line.split('disposed as')[1].strip()


def getRegisterFinesPaid(docket_block):
  pattern = "\d\d\/\d\d\/\d\d\d\d Payment in Full"
  x = re.search(pattern, docket_block)
  if (x is None):
    return ""
  else: 
    matching_line = x.group()
    return matching_line.strip()
  
def getFines(docket_block):
  pattern = "\$(\d|,)*.\d\d"
  x = re.search(pattern, docket_block)
  if (x is None):
    return ""
  else:
    y = re.finditer(pattern, docket_block)
    fines_string = ""
    for fine in y:
      fines_string = fines_string + " " + fine.group() + ","
    fines_string = fines_string.strip(",").strip()
    return fines_string
  
def getJailSentence(docket_block):
  #this is broken, not matching across line breaks
  pattern = "(Jail Sentence|Cust Dept Corrections)\s*Start Date \d\d\/\d\d\/\d\d\d\d\s*Term of\s*\d*\s(Days|Weeks|Months|Years|days|weeks|months|years)"
  x = re.search(pattern, docket_block)
  if (x is None):
    return ""
  else:
    y = re.finditer(pattern, docket_block)
    jail_string = ""
    for sentence in y:
      jail_string = jail_string + " " + sentence.group() + ","
    jail_string = jail_string.strip(",").strip()
    return jail_string