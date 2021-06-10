#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Clase Comun de logica compartida"""

__author__ = "Gilberto"
__copyright__ = "Free"
__credits__ = ["Gilberto", "Ricardo"]
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "tierbolg@outlook.com"
__status__ = "Development"

import config.PROPERTIES as PROPERTIES
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import csv
import json
from urllib.error import HTTPError

def buscarcodigos():
    codigosUrl=[]
    with open(PROPERTIES.INPUTFILE, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:            
            #print(row['LINK'])
            codigosUrl.append(row['LINK'])
    return codigosUrl



def get_page(url):
    datos = urllib.request.urlopen(url).read()
    print(datos)
    soup = BeautifulSoup(datos, "html.parser")
    

if __name__ == '__main__':
    buscarcodigos()

