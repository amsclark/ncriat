# Created by Alexander Clark of Metatheria, LLC
# Creative Commons CC0 v1.0 Universal Public Domain Dedication. No Rights Reserved
# Version 0.1


import tkinter as tk
from tkinter import *
from functools import partial
import sys
import datetime
from tkinter.ttk import Treeview
import urllib
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import lxml
import csv
from openpyxl import load_workbook

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
  

def selectAll(casetree):
    for item in casetree.get_children():
        casetree.selection_add(item)

def clearAll(casetree):
    for item in casetree.get_children():
        casetree.selection_remove(item)

def constructFilterWindow(root, search_button, retrieve_button, select_all_button, clear_all_button, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry, casetree, caselistbox_frame, def_frame, first_entry_label, first_name, last_entry_label, last_name):
  root.title("Nebraska Criminal Record Information Automation Tool | Filter")
  # remove all the elements from the previous view
  cred_frame.grid_remove()
  search_button.grid_remove()
  user_entry_label.grid_remove()
  user_entry.grid_remove()
  pass_entry_label.grid_remove()
  pass_entry.grid_remove()
  def_frame.grid_remove()
  first_entry_label.grid_remove()
  first_name.grid_remove()
  last_entry_label.grid_remove()
  last_name.grid_remove()
  #add new elements for this view
  caselistbox_frame.grid(row=0, column=1, rowspan=5, columnspan=30, padx=10, pady=10)
  casetree.grid(row=0, column=0, sticky="W")
  caseList = getCaseList(first_name, last_name, user_entry, pass_entry)
  for case in caseList:
      casetree.insert('', END, values=case)
  retrieve_button.grid(row=7, column=1, sticky="W", padx=10, pady=10)
  select_all_button.grid(row=7, column=2, sticky="W", padx=10, pady=10)
  clear_all_button.grid(row=7, column=3, sticky="W", padx=10, pady=10)

  

def constructMainWindow(root, search_button, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry, def_frame, first_entry_label, first_name, last_entry_label, last_name):
  root.title("Nebraska Criminal Record Information Automation Tool | Login") 
  cred_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10)
  user_entry_label.grid(row=0, column=0, sticky="W")
  user_entry.grid(row=0, column=1, sticky="W")
  pass_entry_label.grid(row=1, column=0, sticky="W")
  pass_entry.grid(row=1, column=1, sticky="W")

  def_frame.grid(row=0, column=2, rowspan=5, padx=10, pady=10)
  first_entry_label.grid(row=0, column=0, sticky="W")
  first_name.grid(row=0, column=1, sticky="W")
  last_entry_label.grid(row=1, column=0, sticky="W")
  last_name.grid(row=1, column=1, sticky="W")

  search_button.grid(row=7, column=1, sticky="W", padx=10, pady=10)


root = tk.Tk()

#buttons to press
retrieve_button = tk.Button(text="Retrieve Cases", command=lambda: getCases(casetree))
select_all_button = tk.Button(text="Select All", command=lambda: selectAll(casetree))
clear_all_button = tk.Button(text="Clear Selection", command=lambda: clearAll(casetree))
search_button = tk.Button(text="Search Cases", command=lambda: constructFilterWindow(root, search_button, retrieve_button, select_all_button, clear_all_button, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry, casetree, caselistbox_frame, def_frame, first_entry_label, first_name, last_entry_label, last_name))

# credentials
cred_frame = LabelFrame(root, text="Justice Login Credentials", padx=5, pady=5, relief=RIDGE)
user_entry_label = Label(cred_frame, text="Username")
user_entry=Entry(cred_frame)
pass_entry_label = Label(cred_frame, text="Password")
pass_entry=Entry(cred_frame)
pass_entry.config(show="*")

# defendant name
def_frame = LabelFrame(root, text="Defendant Name", padx=5, pady=5, relief=RIDGE)
first_entry_label = Label(def_frame, text="First Name")
first_name=Entry(def_frame)
last_entry_label = Label(def_frame, text="Last Name")
last_name=Entry(def_frame)


# case list
caselistbox_frame = LabelFrame(root, text = "Cases list", padx=5, pady=5, relief=RIDGE)


columns = ("party_name", "party_type", "DOB", "county", "case_num", "caption", "judge", "attorney")
casetree = Treeview(caselistbox_frame, columns=columns, show='headings')
casetree.heading('party_name', text="Party Name")
casetree.heading('party_type', text="Party Type")
casetree.heading('DOB', text="DOB")
casetree.heading('county', text="County")
casetree.heading('case_num', text="Case Number")
casetree.heading('caption', text="Caption")
casetree.heading('attorney', text="Judge")
casetree.heading('attorney', text="Attorney")

constructMainWindow(root, search_button, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry, def_frame, first_entry_label, first_name, last_entry_label, last_name)

root.mainloop()
