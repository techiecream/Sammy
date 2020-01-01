#!/usr/bin/python2.7
#import the libraries
#Stationary Assistant
import requests
from multiprocessing.pool import ThreadPool
import urllib2
import time
import re
import os
import os.path
import pyttsx
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
from time import strftime
from datetime import date, timedelta
import selenium
from selenium import webdriver
import sys
import sqlite3 as lite
#configure the speakers
# Set properties _before_ you add things to say
engine = pyttsx.init()
engine.setProperty('rate', 150) # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1
#configure the files 
#UL=os.getenv('username')
CurrentTime=strftime("%d%b%Y")
FileName=CurrentTime+".txt"
FilePDF=CurrentTime+"TODAY.pdf"
FFilePDF=CurrentTime+"FULL.pdf"
NewsFile=CurrentTime+".html"
Tipsheet="FST"+CurrentTime+".html"
TopicsForBlog="BlogPosts"+CurrentTime+".html"
Blogs=open(TopicsForBlog,'a+')
TipsList=open(Tipsheet,'a+')
TipsList.write('============='+'\n')
DaysNewsList=open(FileName,'a+')
DaysNewsList.write('============='+'\n')
conn=lite.connect('central.sqlite')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS NewsHeadlines("Date" Text, Headline Text)')
cursor.execute('CREATE TABLE IF NOT EXISTS Reminders("Date" Text, Activity Text)')
conn.text_factory = lite.OptimizedUnicode
conn.commit
#confirm that we are online
engine.say('We are waiting for internet connections.')
engine.runAndWait()
time.sleep(1)
result = time.localtime()
def ArticlesToWrite():
    for row in cursor.execute('SELECT * FROM NewsHeadlines WHERE Date=? and Headline like "%education%"', t):
        print row
        Blogs.write(str(row)+'\n')
    Blogs.close()
    
def tips():
    try:
        #Download todays offer
        url = 'https://www.fortebet.ug/pdf/offer_data_today.pdf'
        myfile = requests.get(url)
        #create local todays offer file
        open(FilePDF, 'wb').write(myfile.content)
        #Download full offer
        url = 'https://www.fortebet.ug/pdf/offer_data_full.pdf'
        myfile = requests.get(url)
        #Create local full offer file
        open(FFilePDF, 'wb').write(myfile.content)
        # run firefox webdriver from executable path of your choice
        
    except Exception as e:
            print(e)
    TipsList.close()
def headlines():
    try:
        f=open(NewsFile,"rb")
        t=f.readlines()
        for r in t:
            ty=''.join([char if ord(char) < 128 else '' for char in r])
            cursor.execute("insert into NewsHeadlines values(?,?)",(CurrentTime,ty))
        f.close()
        conn.commit()
    except Exception as e:
        print e
def news(): 
    #Check for new headlines and write them to a text file
    try:
        #UG News  
        news_url="https://news.google.com/news/rss" # the link to location spec news
        print news_url
        Client=urlopen(news_url) # open link for processing
        xml_page=Client.read() #read the xml
        Client.close() #close the opened link
        soup_page=soup(xml_page,"xml") #proccess the xml
        news_list=soup_page.findAll("item") #extract important elements
        DaysNewsList.write("<title>===========UG news=========</title>"+'\n')
        for news in news_list: #loop through the elements
            TodaysList=DaysNewsList.write(str(news)+'\n')   #add them to a local file for future reference

        # US News
        news_url="https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========US news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-ZW&gl=ZW&ceid=ZW:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========SG news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-SG&gl=SG&ceid=SG:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========NG news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-NG&gl=NG&ceid=NG:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========KE news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-KE&gl=KE&ceid=KE:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========NA news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-NA&gl=NA&ceid=NA:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========MY news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-MY&gl=MY&ceid=MY:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========LV news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
            
        # US News
        news_url="https://news.google.com/rss?hl=en-LV&gl=LV&ceid=LV:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========PH news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')

        # US News
        news_url="https://news.google.com/rss?hl=en-PH&gl=PH&ceid=PH:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========BW news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')

        # US News
        news_url="https://news.google.com/rss?hl=en-BW&gl=BW&ceid=BW:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========ZAQ news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-ZA&gl=ZA&ceid=ZA:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========ET news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-ET&gl=ET&ceid=ET:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========NZ news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-NZ&gl=NZ&ceid=NZ:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========TZ news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-TZ&gl=TZ&ceid=TZ:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========CA news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-CA&gl=CA&ceid=CA:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========PK news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-PK&gl=PK&ceid=PK:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========ID news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-ID&gl=ID&ceid=ID:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========GH news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-GH&gl=GH&ceid=GH:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========IL news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-IL&gl=IL&ceid=IL:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========IN news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========AU news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-AU&gl=AU&ceid=AU:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========IE news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        # US News
        news_url="https://news.google.com/rss?hl=en-IE&gl=IE&ceid=IE:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        DaysNewsList.write("<title>===========GB news=========</title>"+'\n')
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
            
        #UK News
        news_url="https://news.google.com/rss?hl=en-GB&gl=GB&ceid=GB:en" # the link to location spec news
        print news_url
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        for news in news_list:
            TodaysList=DaysNewsList.write(str(news)+'\n')
        f=open(FileName,"rb")
        rt=open(NewsFile,'a+')
        t=f.readlines()
        for r in t:
            i= re.findall("<title>.*</title>",r)
            for y in i:
                i=y.strip("<title>").strip()
                k=i.strip("</title>").strip()
                rt.write(str(k)+'\n'+'<br/>')
        rt.close()
    except Exception as e:
            print(e)
    DaysNewsList.close()

loop_value = 1
while (loop_value == 1):
    try:
        urlopen("http://google.com")
    except urllib2.URLError, e:
        engine.say('Network currently down.')
        engine.runAndWait()        
        os.exit()
    else:
        print "Up and running."
        engine.say('We are online.')
        engine.runAndWait()
       
        loop_value = 0
        #Lets start by greeting the users
        day_time = int(strftime('%H'))
        if day_time < 12:
            engine.say('Good morning.')
            engine.runAndWait()
            news()
            tips()
            headlines()
            engine.say('We are done.')
            engine.runAndWait()            
        elif 12 <= day_time < 18:
            engine.say('Good Afternoon.')
            engine.runAndWait()
            news()
            tips()
            headlines()
            engine.say('We are done.')
            engine.runAndWait() 
        else:
            engine.say('Good evening')
            engine.runAndWait()
            engine.runAndWait()
            news()
            tips()
            headlines()
            engine.say('We are done.')
            engine.runAndWait() 
