# Created by Alexander Clark of Metatheria, LLC
# Creative Commons CC0 v1.0 Universal Public Domain Dedication. No Rights Reserved
# Version 0.2

from uifuncs import *
from casefuncs import *

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
