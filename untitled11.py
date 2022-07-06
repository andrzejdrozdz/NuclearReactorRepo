# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:12:31 2022

@author: andrz
"""
from bs4 import BeautifulSoup
import csv
import requests
 
page_url = 'https://www.gov.pl/web/polski-atom/lista-reaktorow-jadrowych'
page = requests.get(page_url)
	

### parsing raw data from the Web
 
soup = BeautifulSoup(page.content, 'html.parser')
 
reactors_raw = soup.find_all(class_='hide')[0].get_text()

# reactors_cleaned

reactors_list_parsed = (
    reactors_raw
    .replace('{"sourceType":"FILE","description":"Zapraszamy do zapoznania się ze szczegółowymi informacjami dotyczącymi reaktorów jądrowych na świecie.","data":"','')
    .replace('\\r\\n','$\r\n')
    .split('$')
    )


#create csv file
filename = 'reaktory1.csv'

    

list_length = len(reactors_list_parsed)
with open(filename, 'w', newline=('\r\n')) as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows([reactors_list_parsed[:list_length-1]])

