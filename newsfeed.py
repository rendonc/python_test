import requests
import os
import time
import sys


def scrapWebpage(url,fileName,diffName):
  text=None
  with requests.get(url) as resp:
    text=resp.text
  
  with open(fileName,"r",encoding=resp.encoding) as f:
    diff,data,pos,line=dataCompare(f,text)
      
  if(diff):
    with open(fname,"w",encoding=resp.encoding) as f:
      print("difference detected at line: "+str(line)+" position: "+str(pos))
      print("writing new feed to file...")
      f.write(resp.text)
    with open(diffName,"w",encoding=resp.encoding) as f:
      if(data is not None):
        f.write(data)

      
def dataCompare(dataFile,newData):
  pos=0
  line=1
  
  for prev in dataFile:
    size=len(prev)
    new=newData[pos:pos+size]
    
    pos+=size
    if prev and prev is not new:
      for index, item in enumerate(new):
        if prev[index]!=item:
          return True, newData[0:pos], index,line
    line+=1
          
  if(pos==0):
    return True, None, pos, line
  
  print("no difference detected...")
  return False,None,-1, line

    
#url="https://news.google.com/"
url="https://raw.githubusercontent.com/rendonc/python_test/master/newsfeed.py"

dname="logs/"
fname=dname+"news.html"
diffname=dname+"diff.txt"

if not os.access(dname,os.F_OK):
  try:
    os.mkdir(dname)
  except IOError as e:
    print("Error while creating directory; please, verify paths and permissions: "+dname)
    print(e.errno)
    print(e)
    exit()
     
if not os.access(fname,os.F_OK):
  fp=None
  try:
    fp = open(fname,"w")
  except IOError as e:
    print("Error while opening file; please, verify paths and permissions: "+fname)
    print(e.errno)
    print(e)
    exit()
  finally: 
    fp.close()
  
  
try:  
  while True:
    scrapWebpage(url,fname,diffname)
    print("Thread sleeping..")
    time.sleep(5)
except IOError as e:
  print("Error while opening file: "+fname)
  print(e)
  exit()
except Exception as e:
  print("Error while scrapping site: "+url)
  print(e)
finally:
  exit()
  
