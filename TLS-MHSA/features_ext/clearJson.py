#!/bin/usr/python
#Tag: json to csv
import argparse
import csv
import demjson
import datetime
import operator 
import numpy 
import os
import pandas 

defaultFamily={'normal':1,'win_normal':2,'vawtrak':3,'miuref':4,'dridex':5,'locky':6,'zeus':7,'trickbot':8}

# CODE A
def codeA():
    startTime = datetime.datetime.now()
    with open("xxxx.json", 'r', encoding='utf-8') as Sf:
        with open("record.json",'w',encoding='utf-8') as Df:
            line=Sf.readline()
            while (line):
                try:
                    dic=demjson.decode(line)
                    tls=dic['tls']
                    if (tls.get('s_cert') and tls.get('cs') and tls.get('c_key_length') and tls['s_cert'][0].get('extensions')):
                        Df.writelines(line)
                    line=Sf.readline()
                except:
                    line=Sf.readline()
                    continue
    endTime = datetime.datetime.now()
    usedTime=(endTime-startTime).seconds
    print("Used:{}s".format(usedTime))

def codeB():
    startTime = datetime.datetime.now()
    with open("good.csv",'r',encoding='utf-8') as tR:
        with open("recordClear.csv",'w',encoding='utf-8',newline='') as trc:
            trReader=csv.DictReader(tR)
            trcWriter=csv.DictWriter(trc,trReader.fieldnames)
            trcWriter.writerow(dict(zip(trReader.fieldnames,trReader.fieldnames)))
            for items in trReader:
                family=items['family']
                items.update({'family':defaultFamily.get(family)})
                trcWriter.writerow(items)
    endTime = datetime.datetime.now()
    usedTime=(endTime-startTime).seconds
    print("Used:{}s".format(usedTime))


