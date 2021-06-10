#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Extractor de encuestas electorales"""

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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urllib.error import HTTPError
import csv


def buscarcodigos():
    codigosUrl = []
    with open(PROPERTIES.INPUTFILE, newline='') as f:
        reader = csv.DictReader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            # print(row['LINK'])
            codigosUrl.append(row['LINK'])
            traerInfo(row)
    return codigosUrl


def traerInfo(renglon):
    driver = webdriver.Chrome(executable_path=PROPERTIES.PATH_DRIVER_CHROME)
    #login first
    driver.get(PROPERTIES.URL)
    driver.find_element_by_name("userName").send_keys(PROPERTIES.MAIN_USER)
    driver.find_element_by_name("password").send_keys(PROPERTIES.MAIN_PASS+Keys.RETURN)

    basicPath="https://capacitacionvirtualine.brightspace.com/d2l/lms/survey/admin/stats/survey_view_overall.d2l?si="
    intermPath="&cft=u&ou="
    finalPath='&prcd=1&sd=&ed=&d2l_stateScopes=%7B%221%22%3A%5B%22gridpagenum%22,%22search%22,%22pagenum%22%5D,%222%22%3A%5B%22lcs%22%5D,%223%22%3A%5B%22grid%22,%22pagesize%22,%22htmleditor%22,%22hpg%22%5D%7D&d2l_stateGroups=&d2l_statePageId=195&d2l_change=0'
    finalurl=basicPath+renglon['ID_survey']+intermPath+renglon['Codigo']+finalPath

    print(finalurl)

    driver.get(finalurl)
    htmlObtenido = driver.page_source
    beautifulSoup=BeautifulSoup(htmlObtenido, "lxml")
    driver.close()



if __name__ == '__main__':
    codigosUrl = []
    codigosUrl = buscarcodigos()
    
