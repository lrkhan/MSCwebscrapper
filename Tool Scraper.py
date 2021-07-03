from os import sep
import pandas as pd
import numpy as np
import time
from selenium import webdriver
from time import sleep


def importData():
    datIn = pd.read_csv('tools.csv')
    return datIn

def getCat(itemNum='44078335'):
    browser = webdriver.Edge()
    browser.get('https://www.mscdirect.com/product/details/'+itemNum)

    sleep(5)
    
    site = browser.find_elements_by_tag_name('body')[0].text

    browser.quit()

    start = int(site.find('Home'))
    end = int(site.find('Email'))-2
    items = list(site[start:end].replace(" ", "").split('/'))
    print(items)
    
    if len(items) == 1:
        return ["",""]
    
    return [items[1],items[-2]]

def seperate(datIn, type):    
    if type == 'msc':
        datOut = datIn[datIn['MSC#'] != '']
        datOut = datOut[datOut['Supplier'] != 'Central']
    
    elif type == 'central':
        #incomplete
        0
        #datOut = datOut[datOut['Supplier'] != 'MSC']
    
    return datOut

def main():
    start_time = time.time()
    MSCimport = importData()

    print("MSC tool info has been imported")
    
    mscOnly = seperate(MSCimport.fillna(''),'msc')
    
    print('Importated data has been sorted to tools that only have MSC numbers')

    
    for i in range(len(mscOnly.index)-1):
        if mscOnly.iloc[i,2].isdigit():
            cat = getCat(mscOnly.iloc[i,2])
            mscOnly.iloc[i,3] = cat[0]
            mscOnly.iloc[i,4] = cat[1]

    mscOnly.to_csv(r'C:\Users\lkhan\Documents\Webscraper\MSC Tools\output.csv')
    print("--- %s ---" % (time.time() - start_time))
    return 0

if __name__ == '__main__':
    main()
