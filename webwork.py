import requests
import logging
import lxml.html
import contextlib

import re
import datetime

def getWebworkPracticeTables(sess):
    #Responsible For Only Getting the Practice Sets for WebWork
    mathpage = sess.get('https://ww3.math.msu.edu/webwork2/mth_133_fs19_97n4yc')
    doc = lxml.html.fromstring(mathpage.content)
    homework_sets = doc.xpath('//*[@id="hws0"]/div/table/tr')
    learning_sets = []
    homework_sets.pop(0)
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
            learning_sets.append(assignment_data)
            #print(assignment_data, end=" ")
        
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
    return [learning_sets, assessing_sets_list]
