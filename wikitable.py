#====================================================#
# wikitable1.0                                       #
# wikitable is python script to fetch tables from    #
# wikipedia to python list of dictionaries or        #
# pandas DataFrame object.                           #
# author : Arijit Mukherjee                          #
# date   : 17/11/2016                                #
#====================================================#

import pandas
import requests
from bs4 import BeautifulSoup
import sys

def get_tables(url,find_string={ "class" : "wikitable sortable" }):
    data=requests.get(url).text
    soup = BeautifulSoup(data,"html5lib")
    [x.extract() for x in soup.findAll('span',{"style":"display:none"})]
    tables = soup.findAll("table",find_string)
    return tables

def fetch_table(table):
    theads=[]
    for tx in table.findAll('th'):
        theads.append(tx.text)
    data=[]
    tbody=table.find('tbody')
    for rows in tbody.findAll('tr'):
        row={}
        i=0
        for cell in rows.findAll('td'):
            row[theads[i]]=cell.text
            i+=1
        if len(row)!=0:
            data.append(row)
    return data
            
def get_all_tables(url,mode='dict-array',find_string={ "class" : "wikitable sortable" }):
    tables=get_tables(url,find_string)
    data=[]
    dataframe=[]
    for table in tables:
        data.append(fetch_table(table))
    if mode=='dict-array':
        return data
    elif mode=='dataframe':
        for d in data:
            dataframe.append(pandas.DataFrame(d))
        return dataframe
    else:
        return data


if __name__=="__main__":
    if len(sys.argv)<=1:
        url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
    else:
        url=sys.argv[1]
    for df in get_all_tables(url,mode='dataframe'):
        print '================================================================'
        print df.head()
        print ' '
        print ' '

   