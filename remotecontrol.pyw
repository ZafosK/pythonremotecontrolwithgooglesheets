# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:26:58 2021
@author: ZafosK
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from time import sleep

def shutdown():
    os.system("shutdown /s /t 1")    
    
def shutdownwithtime():
    time= commandsheet.acell('A2').value
    sleep(time)
    os.system("shutdown /s /t 1")  

def opensheet():
    pass

scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
commandlist={"shutdown":shutdown,"opensheet":opensheet,"shutdownwithtime":shutdownwithtime}
  
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\files\json.json', scope) 	#the location of the json file used for oauth authentication. 
																						#This should not be in the startup location 
 
client = gspread.authorize(creds)  

commandsheet = client.open("nice").sheet1 
lastcommand='tempname'

while(True):
    command= commandsheet.acell('A1').value
    if command != lastcommand:
        commandlist[command]()
        
    lastcommand=command
    sleep(30)
    