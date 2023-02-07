from caseprocessing import *
from patternfuncs import *
from auxfuncs import *

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

def selectAll(casetree):
    for item in casetree.get_children():
        casetree.selection_add(item)

def clearAll(casetree):
    for item in casetree.get_children():
        casetree.selection_remove(item)
