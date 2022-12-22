# Created by Alexander Clark of Metatheria, LLC
# Creative Commons CC0 v1.0 Universal Public Domain Dedication. No Rights Reserved
# Version 0.1

import tkinter as tk
from tkinter import *
from functools import partial
import sys
import datetime
import urllib
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import csv

def getCaseList():
  print("getting case list")

def updateCaseList():
  print("updating case list")

def getCases():
  print("getting cases")

def getCase():
  print("getting case ")

def extractInfo():
  print("extracting info from")

def createSpreadsheet():
  print("creating spreadsheet")

def constructFilterWindow(root, button1, button2, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry):
  root.title("Nebraska Criminal Record Information Automation Tool | Filter")
  cred_frame.grid_remove()
  button1.grid_remove()
  user_entry_label.grid_remove()
  user_entry.grid_remove()
  pass_entry_label.grid_remove()
  pass_entry.grid_remove()
  button2.grid(row=0, column=1, sticky="W", padx=10, pady=10)

  

def constructMainWindow(root, button1, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry):
  root.title("Nebraska Criminal Record Information Automation Tool | Login") 
  
  cred_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10)
  user_entry_label.grid(row=0, column=0, sticky="W")
  user_entry.grid(row=0, column=1, sticky="W")
  pass_entry_label.grid(row=1, column=0, sticky="W")
  pass_entry.grid(row=1, column=1, sticky="W")

  button1.grid(row=7, column=1, sticky="W", padx=10, pady=10)


root = tk.Tk()

#button to press
button2 = tk.Button(text="Retrieve Cases", command=getCases)
button1 = tk.Button(text="Get Records", command=lambda: constructFilterWindow(root, button1, button2, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry))

# credentials
cred_frame = LabelFrame(root, text="Justice Login Credentials", padx=5, pady=5, relief=RIDGE)
user_entry_label = Label(cred_frame, text="Username")
user_entry=Entry(cred_frame)
pass_entry_label = Label(cred_frame, text="Password")
pass_entry=Entry(cred_frame)
pass_entry.config(show="*")


constructMainWindow(root, button1, cred_frame, user_entry_label, user_entry, pass_entry_label, pass_entry)

root.mainloop()
