# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 18:29:24 2016

@author: os
"""
from bottle import route, run, template,static_file, response 
import  tablegen
import json
import sys
import os

@route('/pdf') 
def getbinimg():
    return 'result'
@route('/generator') 
def generator():
    filename = 'index.htm'
#    return static_file(filename,  root='C:\Users\os\Documents\SpyderWS\Generator' )  
    return static_file(filename,  root='' )  

@route ('/gethtmltable/<inputt>')
def getHtmltable(inputt, method='GET'):
    j=json.loads(inputt) 
    return tablegen.generateHtmlTable(tablegen.getDefinitions(j["input"]))

@route ('/getjtable/<inputt>')
def getjtable(inputt, method='GET'):
    j=json.loads(inputt) 
    return tablegen.generateHtmlTable(tablegen.getDefinitions(j["input"]))
    
@route ('/gettable/<inputt>')
def getTable(inputt, method='GET'):
#    print '0'+inputt
    j=json.loads(inputt)
#    print j["className"]
    inp = """USE [CIS]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[KRTy](
	[KRT_ID] [int] NOT NULL,
	[KRT_ID_FARnosti] [int] NOT NULL,
	[KRT_Kniha] [int] NOT NULL,
	[KRT_Strana] [int] NOT NULL,
	[KRT_PoradoveCislo] [int] NOT NULL,
	[KRT_ID_OSOby] [int] NOT NULL,
	[KRT_Datum] [datetime] NOT NULL,
	[KRT_TitulPred] [nvarchar](50) NULL,
	[KRT_Jmeno1] [nvarchar](100) NULL,
	[KRT_Jmeno2] [nvarchar](100) NULL,
	[KRT_Jmeno3] [nvarchar](100) NULL,
	[KRT_Prijmeni] [nvarchar](100) NOT NULL,
	[KRT_TitulZa] [nvarchar](50) NULL,
	[KRT_Ulice] [nvarchar](100) NULL,
	[KRT_CisloPopisne] [nvarchar](10) NULL,
	[KRT_Obec] [nvarchar](100) NULL,
	[KRT_PSC] [nvarchar](10) NULL,
	[KRT_Stat] [nvarchar](100) NULL,
	[KRT_ID_MISta] [int] NULL,
	[KRT_ID_UDElovatele] [int] NULL,
	[KRT_Krstny1] [nvarchar](100) NULL,
	[KRT_Krstny1Pozn] [nvarchar](200) NULL,
	[KRT_Krstny2] [nvarchar](100) NULL,
	[KRT_Krstny2Pozn] [nvarchar](200) NULL,
	[KRT_Poznamka] [nvarchar](200) NULL,
	[KRT_DatumUlozeni] [datetime] NULL,
	[KRT_ID_UZIvatel] [int] NULL,
	[KRT_DatumPoslAkt] [datetime] NULL,
	[KRT_ID_UZIvatelPoslAkt] [int] NULL
) ON [PRIMARY]

GO


"""
#    return tablegen.createClass(j["input"],j["className"]) 
#    print j["input"]
#    print tablegen.createClass(j["input"],j["className"]) 
#    return tablegen.createClass(j["input"],j["className"]) 

run(host='localhost', port=8080)

#import subprocess    
#
#def runBrowser():
#    url='http://localhost:8080/generator'
#    if sys.platform=='win32':
#        print 'Win32'
#        os.startfile(url)
#    elif sys.platform=='darwin':
#        subprocess.Popen(['open', url])
#    else:
#        try:
#            subprocess.Popen(['xdg-open', url])
#        except OSError:
#                print 'Please open a browser on: '+url
#
#
#
#
#
#import threading
#from threading import Thread
#
#Thread(target = runBrowser()).start()
#Thread(target = run(host='localhost', port=8080)).start()
#
