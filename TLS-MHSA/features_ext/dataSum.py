#!/bin/usr/python
#Tag: json to csv
import argparse
import csv
import demjson
import datetime
import operator 
import numpy 
import pandas 



startTime = datetime.datetime.now()
#PART A
"""
with open('good.csv','r',encoding='utf-8') as g1:
    g1Reader=csv.DictReader(g1)
    with open('good2.csv','r',encoding='utf-8') as g2:
        g2Reader=csv.DictReader(g2)
        with open('good3.csv','r',encoding='utf-8') as g3:
            g3Reader=csv.DictReader(g3)
            with open('normal.csv','w',encoding='utf-8',newline='') as nor:
                norWriter=csv.DictWriter(nor,g1Reader.fieldnames)
                norWriter.writerow(dict(zip(g1Reader.fieldnames, g1Reader.fieldnames)))
                for items in g1Reader:
                    norWriter.writerow(items)
                for items in g2Reader:
                    norWriter.writerow(items)
                for items in g3Reader:
                    norWriter.writerow(items)
"""

# PART B
"""
flag=0
with open('normal.csv','r',encoding='utf-8') as nor:
    with open('malware_stratosphere.csv','r',encoding='utf-8') as ms:
        with open('train.csv','w',encoding='utf-8',newline='') as tr:
            with open('test.csv','w',encoding='utf-8',newline='') as test:
                noReader=csv.DictReader(nor)
                msReader=csv.DictReader(ms)
                trWriter=csv.DictWriter(tr,noReader.fieldnames)
                testWriter=csv.DictWriter(test,noReader.fieldnames)
                trWriter.writerow(dict(zip(noReader.fieldnames,noReader.fieldnames)))
                testWriter.writerow(dict(zip(noReader.fieldnames,noReader.fieldnames)))
                for items in noReader:
                    if(flag<2000):
                        testWriter.writerow(items)
                    else:
                        trWriter.writerow(items)
                    flag+=1
                flag=0
                for items in msReader:
                    if(flag<2000):
                        testWriter.writerow(items)
                    else:
                        trWriter.writerow(items)
                    flag+=1
"""
# PART C
with open('trainRandomClear.csv','r',encoding='utf-8') as tr:
    with open('traindata.csv','w',encoding='utf-8',newline='') as trd:
        with open('testdata.csv','w',encoding='utf-8',newline='') as tsd:
            flag=0 # number of split
            trReader=csv.DictReader(tr)
            trdWriter=csv.DictWriter(trd,trReader.fieldnames)
            tsdWriter=csv.DictWriter(tsd,trReader.fieldnames)
            trdWriter.writerow(dict(zip(trReader.fieldnames,trReader.fieldnames)))
            tsdWriter.writerow(dict(zip(trReader.fieldnames,trReader.fieldnames)))
            for items in trReader:
                if(flag<4000):
                    tsdWriter.writerow(items)
                else:
                    trdWriter.writerow(items)
                flag+=1
endTime = datetime.datetime.now()
usedTime=(endTime-startTime).seconds
print("Used:{}s".format(usedTime))


