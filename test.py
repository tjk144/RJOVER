import datetime 
from time import sleep
from threading import Thread
import numpy as np

def running_gr(filename):
    while True:
        #run gr script for data collection. Must send this script the filename.

print("Insert desired filename and file path below. It must start from /home (By default the year,date, and time will be placed before whatever name you choose, to disable this enter 0):")
filename=input()
Flag=False;
if filename!="0":
    print("Filename accepted")
else:
    print("No default dating will be applied")
    print("Insert desired filename and file path below. It must start from /home:")
    Flag=True;
    filename=input()
    print("Filename accepted")

print("How long would you like to have each time period last for? Please enter a double number for the hours below.")
periodhours=input()
periodseconds=periodhours*3600;
print("How many days would you like to run for? Please insert an integer atleast 1 below.")
days=input()
if Flag=False:
    loc=np.zeros(len(filename));
    for d in range(0,len(filename):
        loc[d]=filename.find("/",d,len(filename));
    indexslash=max(loc);

for d in range(1,days):
    if Flag==False:
        dtime=datetime.datetime.utcnow() #Need to fix formatting here to not be annoying and chop seconds
        filename=filename[:indexslash] +dtime +filename[indexslash:]; # Year,Month,Day,Hour,Minute is 12 digits
   t=Thread(target=running_gr(filename))
   t.daemon = True
   t.start()
   sleep(periodseconds)
