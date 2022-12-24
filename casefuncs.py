def getCaseList(first_name, last_name, user_entry, pass_entry):
  caseListData = []
  first_name_string = first_name.get()
  last_name_string = last_name.get()
  username = user_entry.get()
  password = pass_entry.get()
  print("getting case list for " + first_name_string + " " + last_name_string + " with username " + username + " and password " + password)
  JUSTICE_URL = 'https://www.nebraska.gov/justice/name.cgi'
  data = {
      'party_name': last_name_string + ', ' + first_name_string,
      'indiv_entity_type': 'individual',
      'case_type': [
          'CR',
          'TR',
       ],
      'submit_hidden': '1',
      'sort': 'party_name',
      'order': 'asc',
      'year': '',
      }
  resp = requests.post(JUSTICE_URL, timeout=180, auth=HTTPBasicAuth(username, password), data=data)
  soup = BeautifulSoup(resp.content, 'lxml')
  rows = soup.find_all('tr')
  for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      caseListData.append([ele for ele in cols if ele]) # get rid of empty values
  
  print(caseListData)

  caseList = [("Clark, Alexander", "DEF", "07/18/1998", "69", "C69TR190000257", "City v. Alexander Clark", "Harford, Russell,", "Unknown or None Assigned"), 
            ("Clark, Alexander, J", "DEF", "10/19/1995", "05", "C05CR140001763", "State v. Alexander J Clark", "Vampola, Kenneth,", "Unknown or None Assigned"), 
            ("Clark, Alexander, M", "DEF", "05/31/1985", "69", "C02CR070016284", "State v. Alexander M Clark", "No Judge Assigned", "Unknown or None Assigned")]
  return caseList

def updateCaseList():
  print("updating case list")

def getCases(casetree):
  print("getting cases")
  selected_cases = casetree.selection()
  print(selected_cases)

  

def getCase():
  print("getting case ")

def extractInfo():
  print("extracting info from")

def createSpreadsheet():
  print("creating spreadsheet")
  