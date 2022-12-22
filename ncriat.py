# Created by Alexander Clark of Metatheria, LLC
# Creative Commons CC0 v1.0 Universal Public Domain Dedication. No Rights Reserved
# Version 0.1

import tkinter as tk
from tkinter import *
import sys
import datetime
import urllib
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import csv
import winsound

def getCaseList():
  pass

def updateCaseList():
  pass

def getCases():
  pass

def getCase():
  pass

def extractInfo():
  pass

def createSpreadsheet():
  pass

def constructMainWindow(root):
  root.title("Nebraska Courts E-Services Scraper") 
  # date options area
  date_frame = LabelFrame(root, text="Target Date", padx=5, pady=5, relief=RIDGE)
  label1 = Label(date_frame, text="Please enter a date \n in mm/dd/yyyy format.")
  entry1=Entry(date_frame)

  # county options area
  options_frame = LabelFrame(root, text="Choose a County Option", padx=5, pady=5, relief=RIDGE)
  c_option = tk.StringVar(None, "1")
  option1 = Radiobutton(options_frame, text="Douglas, Lancaster and Sarpy Only", variable=c_option, value="1")
  option2 = Radiobutton(options_frame, text="All Nebraska Counties", variable=c_option, value="2")  

  #button to press
  button1 = tk.Button(text="Scrape Justice", command=scrapeCalendar)

  # credentials
  cred_frame = LabelFrame(root, text="Justice Login Credentials", padx=5, pady=5, relief=RIDGE)
  user_entry_label = Label(cred_frame, text="Username")
  user_entry=Entry(cred_frame)
  pass_entry_label = Label(cred_frame, text="Password")
  pass_entry=Entry(cred_frame)
  pass_entry.config(show="*")

  date_frame.grid(row=0, column=1, rowspan=5, padx=10, pady=10)
  label1.grid(row=0, column=0)
  entry1.grid(row=1, column=0)

  options_frame.grid(row=0, column=2, rowspan=5, padx=10, pady=10)
  option1.grid(row=0, column=0, sticky="W")
  option2.grid(row=1, column=0, sticky="W")

  cred_frame.grid(row=0, column=3, rowspan=5, padx=10, pady=10)
  user_entry_label.grid(row=0, column=0, sticky="W")
  user_entry.grid(row=0, column=1, sticky="W")
  pass_entry_label.grid(row=1, column=0, sticky="W")
  pass_entry.grid(row=1, column=1, sticky="W")

  button1.grid(row=7, column=1, sticky="W", padx=10, pady=10)

root = tk.Tk()
root.mainloop()
