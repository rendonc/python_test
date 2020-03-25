import requests
import os
import time
import sys

def scrapWebpage(url,fileName,diffName):
  text=None
  with requests.get(url) as resp:
    text=resp.text
  
  prev=None
  with open(fileName,"r",encoding=resp.encoding) as f:
      prev=f.read()

  position=0
  diff,data,pos=dataCompare(prev,text)
  
  if(diff):
    with open(fname,"w",encoding=resp.encoding) as f:
      print("difference detected at position: "+str(pos))
      print("writing new feed to file...")
      f.write(resp.text)
    with open(diffName,"w",encoding=resp.encoding) as f:
      f.write(data)

    
def dataCompare(prev,new):

  len1=len(prev)

  len2=len(new)
    
  size=0
  if(len1>len2):
    size=len2
  else:
    size=len1
  
  if(size==0):
    return True, new, 0
  
  for i in range(0,size):
    if(prev[i]!=new[i]):
      return True, new[i:],i
  print("no difference detected...")
  return False,"",-1
  
  
url="https://news.google.com/"
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
except:
  e = sys.exc_info()[0]
  print("Error while scrapping site: "+url)
  print(e)
finally:
  exit()
  
