'''
This file is the WebWorK module.
It is responsible for taking an authenticated session from tokengrab.py
and authenticating with https://math.msu.edu/Student in order to get
Learning Sets, Assessing Sets and Other Relevant Data From that Page
'''
import requests
import logging
import lxml.html
import contextlib

import re
from datetime import date
import datetime
import sys

from prettytable import PrettyTable

def getWebworkPracticeTables(sess):
    #Responsible For Only Getting the Practice Sets for WebWork
    mathpage = sess.get('https://ww3.math.msu.edu/webwork2/mth_133_fs19_97n4yc')
    doc = lxml.html.fromstring(mathpage.content)
    homework_sets = doc.xpath('//*[@id="hws0"]/div/table/tr')
    learning_sets = []
    try:
        homework_sets.pop(0) #Remove Table Heading
        for h in homework_sets:
            h_children = h.getchildren()
            assignment_data = []
            for c in h_children:
                text_content = c.text_content()
                if "Learning" in text_content:
                    assignment_data.append(text_content)
                elif "due" in text_content:
                    #assignment_data.append(text_content)
                    match = re.search('\d{2}\/\d{2}\/\d{4}', text_content)
                    assignment_data.append(datetime.datetime.strptime(match.group(), '%m/%d/%Y').date())
                #learning_sets.append(assignment_data)
                #print(assignment_data, end=" ")
    except IndexError:
        print("I'm not seeing any homework sets on WebWork For You...")
        learning_sets.append(["NULL", "NULL"])
        
    try: 
        assessing_sets = doc.xpath('//*[@id="qzs0"]/div/table/tr')
        assessing_sets_list = []
        assessing_sets.pop(0)
        for aSets in assessing_sets:
            a_children = aSets.getchildren()
            a_data = []
            for a in a_children:
                if(len(a) != 0):
                    for aa in a.getchildren():
                        a_data.append(aa.text_content())
                else:
                    amatch = re.search('\d{2}\/\d{2}\/\d{4}', a.text_content())
                    a_data.append(datetime.datetime.strptime(amatch.group(), '%m/%d/%Y').date())

               
            assessing_sets_list.append(a_data)
    except IndexError:
        print("I'm not seeing any assessing sets on Webwork For You...")
        assessing_sets_list.append(["NULL", "NULL"])


    x = PrettyTable()
    x.field_names = ["Learning Set Name", "Due Date"]
    
    for l in learning_sets: #This crap needs to be moved to webwork.py
        if not isinstance(l[1], str):
            if((l[1]-date.today()).days <= 3):
                x.add_row([l[0], "(!!!) "+str(l[1])])
            else:
                x.add_row([l[0], str(l[1])])
##        else:
##            x.add_row([l[0], str(l[1])])
    x.align["Due Date"] = "r"

    y = PrettyTable()
    y.field_names = ["Assessing Set Name", "Due Date"]

    for a in assessing_sets_list: #This crap needs to be moved to webwork.py
        if not isinstance(l[1], str):
            if((a[1]-date.today()).days <= 3):
                y.add_row([a[0], "(!!!) "+str(a[1])])
            else:
                y.add_row([a[0], str(a[1])])
##        else:
##            y.add_row([a[0], str(a[1])])
    
    y.align["Due Date"] = "r"
    
    return [learning_sets, assessing_sets_list, x, y]
