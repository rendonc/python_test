import requests
import os
import time
import difflib

def scrapWebpage(url,fileName):
  with requests.get(url) as resp:
    text=resp.text
    with open(fileName,"r",encoding=resp.encoding) as f:
      prev=f.read()
      dataCompare(prev,text)
    
  with open(fname,"w",encoding=resp.encoding) as f:
    print("writing to file...")
    f.write(resp.text)
    
def dataCompare(prev,new):
  # initiate the Differ object
  d = difflib.Differ()
 
  # calculate the difference between the two texts
  diff = d.compare(prev, new)

  # output the result
  print ('\n'.join(diff))

url="https://news.google.com/"
dname="logs/"
fname=dname+"news.html"

exist=os.access(dname,os.F_OK)

if not os.access(dname,os.F_OK):
  os.mkdir(dname)

if not os.access(fname,os.F_OK):
  with open(fname,"w") as f:
    pass


for i in range(10):
  scrapWebpage(url,fname)
  time.sleep(2)


