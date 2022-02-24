#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

import datetime
import os
import sys
import time
import requests
import json
import ast
import smtplib
import schedule
import mysql.connector
from string import Template
from datetime import datetime
from datetime import timedelta
from datetime import date

def read_template(filename):
    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
    
#print( "Connecting to mysql database")

# some string constants
SINGLE_HASH = "#"
HASHES = "########################################"
SLASH_N = "\n"

#connect to the database. Enter your host, username and password
#cnx = mysql.connector.connect(user='user', password='password', host='host', database='database')
#cursor = cnx.cursor()

def main():
    if True:
       print(HASHES)
       #connect to the database. Enter your host, username and password
       print("Connecting to MySQL database")
       cnx = mysql.connector.connect(user='user', password='password', host='host', database='database')
       cursor = cnx.cursor()    
       today = date.today()
       print("Downloading forecast data from Open Weather")
       url4cast = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&units=metric&appid={APIKEY}')
       json_data = json.loads(url4cast.text)
       observe = format(json.dumps(json_data))
       a=json.loads(observe)
       b=a['daily']
       c = format(json.dumps(b))
       d = json.loads(c)
       e0 = d[0]
       e1 = d[1]
       e2 = d[2]
       e3 = d[3]
       e4 = d[4]
       e5 = d[5]
       e6 = d[6]
       e7 = d[7]
       if not e0.get('rain') is None:
              r0 = e0['rain']
       else:
              r0 = 0
       if not e1.get('rain') is None:
              r1 = e1['rain']
       else:
              r1 = 0
       if not e2.get('rain') is None:
              r2 = e2['rain']
       else:
              r2 = 0
       if not e3.get('rain') is None:
              r3 = e3['rain']
       else:
              r3 = 0
       if not e4.get('rain') is None:
              r4 = e4['rain']
       else:
              r4 = 0
       if not e5.get('rain') is None:
              r5 = e5['rain']
       else:
              r5 = 0
       if not e6.get('rain') is None:
              r6 = e6['rain']
       else:
              r6 = 0
       if not e7.get('rain') is None:
              r7 = e7['rain']
       else:
              r7 = 0
       f0 = e0['temp']
       f1 = e1['temp']
       f2 = e2['temp']
       f3 = e3['temp']
       f4 = e4['temp']
       f5 = e5['temp']
       f6 = e6['temp']
       f7 = e7['temp']
       g0 = format(json.dumps(f0))
       g1 = format(json.dumps(f1))
       g2 = format(json.dumps(f2))
       g3 = format(json.dumps(f3))
       g4 = format(json.dumps(f4))
       g5 = format(json.dumps(f5))
       g6 = format(json.dumps(f6))
       g7 = format(json.dumps(f7))
       h0 = json.loads(g0)
       h1 = json.loads(g1)
       h2 = json.loads(g2)
       h3 = json.loads(g3)
       h4 = json.loads(g4)
       h5 = json.loads(g5)
       h6 = json.loads(g6)
       h7 = json.loads(g7)
       v0 = h0
       v1 = h1
       v2 = h2
       v3 = h3
       v4 = h4
       v5 = h5
       v6 = h6
       v7 = h7
       insert_Forecast0 = "INSERT INTO Forecast0(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast1 = "INSERT INTO Forecast1(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast2 = "INSERT INTO Forecast2(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast3 = "INSERT INTO Forecast3(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast4 = "INSERT INTO Forecast4(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast5 = "INSERT INTO Forecast5(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast6 = "INSERT INTO Forecast6(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       insert_Forecast7 = "INSERT INTO Forecast7(validTimeLocal,temperatureMax,temperatureMin,precipTotal) VALUES (%s, %s, %s, %s)"
       j0 = date.today()
       j1 = date.today()+timedelta(days=1)
       j2 = date.today()+timedelta(days=2)
       j3 = date.today()+timedelta(days=3)
       j4 = date.today()+timedelta(days=4)
       j5 = date.today()+timedelta(days=5)  
       j6 = date.today()+timedelta(days=6)  
       j7 = date.today()+timedelta(days=7)         
       print('Recording values in Data Bases')
       val0 = (j0, v0['max'], v0['min'], r0)
       val1 = (j1, v1['max'], v1['min'], r1)
       val2 = (j2, v2['max'], v2['min'], r2)
       val3 = (j3, v3['max'], v3['min'], r3)
       val4 = (j4, v4['max'], v4['min'], r4)
       val5 = (j5, v5['max'], v5['min'], r5)
       val6 = (j6, v6['max'], v6['min'], r6)
       val7 = (j7, v7['max'], v7['min'], r7)
       cursor.execute(insert_Forecast0, val0)
       cursor.execute(insert_Forecast1, val1)
       cursor.execute(insert_Forecast2, val2)
       cursor.execute(insert_Forecast3, val3)
       cursor.execute(insert_Forecast4, val4)
       cursor.execute(insert_Forecast5, val5)
       cursor.execute(insert_Forecast6, val6)
       cursor.execute(insert_Forecast7, val7)
       cnx.commit()
 
       print(today.strftime("%d/%m/%Y"),'-> Values written into Data Bases')

# ============================================================================
# here's where we start doing stuff
# ============================================================================
print(SLASH_N + HASHES)
print(SINGLE_HASH, "Forecast QA from OpenWeather      ", SINGLE_HASH)
print(SINGLE_HASH, "By Pablo Blanco-Gomez             ", SINGLE_HASH)
print(HASHES)

# Now see what we're supposed to do next
if __name__ == "__main__":
   schedule.every().day.at("08:10").do(main)
   while True:
       schedule.run_pending()
       time.sleep(1)
