'''
Made By Anurag Kompalli

The purpose of this script is to aquire the necessary credentials 
from login.msu.edu to access all websites that utilize MSU's
sentinel single sign-on and print relevant data from various MSU
Homework Websites

'''

import requests
import lxml.html
from lxml import etree

import webwork

import stdiomask
import sys
import time

netid = input("NetID: ")
password = stdiomask.getpass(prompt='Password: ', mask='')

start_time = time.time()
sys.stdin.flush()
login_data = {
    "AlternateID":netid
}

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
    print("Grabbing WebWorK Data...")
    workList = webwork.getWebworkPracticeTables(sess)
    learning_table = workList[2]
    assessing_table = workList[3]
    
    print('=====================WeBWork============================')
    print(learning_table)
    print("\n")
    print(assessing_table)
    print("========================================================")
    sess.close()
    
    #MasteringPhysics

    #Call D2L Script to get D2L Data


    #Call TopHat Script to get TopHat Data (NOT Sentinel Single Sign On)
    print("--- %s seconds ---" % (time.time() - start_time))
