'''
This file is the Pearson Mastering module.
It is responsible for taking an authenticated session from tokengrab.py
and authenticating with https://math.msu.edu/Student in order to get
Upcoming Homework and Other Relevant Data
'''
import requests
import lxml.html
from lxml import etree

##import webwork
##import mastering

import stdiomask
import sys
import time

def getMastering(sess):
    d2l = sess.get('h
    
