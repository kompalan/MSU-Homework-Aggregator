'''
Made By Anurag Kompalli

The purpose of this script is to aquire the necessary credentials 
from login.msu.edu to access all websites that utilize MSU's
sentinel single sign-on and print relevant data from various MSU
Homework Websites

'''

import requests
import logging
import lxml.html
import contextlib

from lxml import etree

import webwork

from prettytable import PrettyTable
from datetime import date

import stdiomask
import sys

netid = input("NetID: ")
password = stdiomask.getpass(prompt='Password: ', mask='')

sys.stdin.flush()
login_data = {
    "AlternateID":netid
}

#Logging requests httplib to see the http headers and data
try:
    from http.client import HTTPConnection # py3
except ImportError:
    from httplib import HTTPConnection # py2

def debug_requests_on():
    '''Switches on logging of the requests module.'''
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def debug_requests_off():
    '''Switches off logging of the requests module, might be some side-effects'''
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False

@contextlib.contextmanager
def debug_requests():
    '''Use with 'with'!'''
    debug_requests_on()
    yield
    debug_requests_off()

debug_requests_off()

with requests.Session() as sess:
    loginpage = sess.get('http://login.msu.edu')
    doc = lxml.html.fromstring(loginpage.content)
    pwdname = str(doc.xpath('//*[@id="pswd"]/@name')[0])
    encryptedstamp = str(doc.xpath('/html/body/form/table/tr[3]/td[2]/input[2]/@value')[0])
    login_data[pwdname] = password
    login_data["EncryptedStamp"] = encryptedstamp
    login_data["App"] = "MSUNet"
    login_data["submit"] = "Login"
    login_data["AuthenticationMethod"] = "MSUNet"
    authenticated = sess.post('https://login.msu.edu/Login', data=login_data)

    #Call webwork script to get webwork data
    workList = webwork.getWebworkPracticeTables(sess)
    learning_sets_list = workList[0]
    assessing_sets_list = workList[1]

    x = PrettyTable()
    x.field_names = ["Learning Set Name", "Due Date"]
    print('=====================WeBWork============================')
    for l in learning_sets_list:
        if((l[1]-date.today()).days <= 3):
            x.add_row([l[0], "(!!!) "+str(l[1])])
        else:
            x.add_row([l[0], str(l[1])])
    x.align["Due Date"] = "r"
    print(x)

    y = PrettyTable()
    y.field_names = ["Assessing Set Name", "Due Date"]

    for a in assessing_sets_list:
        if((a[1]-date.today()).days <= 3):
            y.add_row([a[0], "(!!!) "+str(a[1])])
        else:
            y.add_row([a[0], str(a[1])])
    print("\n")
    y.align["Due Date"] = "r"
    print(y)
    print("\n")
    print("========================================================")
    #Call D2L Script to get D2L Data


    #Call TopHat Script to get TopHat Data (NOT Sentinel Single Sign On)
    
