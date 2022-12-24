import re

    # ^ The Case ID is  [a-zA-Z][a-zA-Z] \d\d \d*\s*$
    # (next pattern is to find line with case caption)
    # ^\s*.*\sv\.\s.*$
    # ^ Classification: (Misdemeanor|Felony|Statute)\s*$
    # ^ Filed on \d\d\/\d\d\/\d\d\d\d\s*by the (County|District) Prosecutor\s*$
    # ^ This case is (Closed|Open) as of \d\d\/\d\d\/\d\d\d\d\s*$
    # ^    It was disposed as  .*$

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