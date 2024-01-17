import requests
from bs4 import BeautifulSoup
import hashlib
import os
import urllib
import re
url = "http://www.mumresults.in/"
response = requests.get(url)
soup = BeautifulSoup(response.content)
y = input("Enter the course keyword ")

it_links = lambda tag: (getattr(tag, 'name', None) == 'a' and
                        'href' in tag.attrs and
                        y in tag.get_text())
results = soup.find(it_links)

if response.status_code == 200:
    with open("op.txt","w") as f:
        print(results.text,file=f)
        
else:
    print("A bit More",response.status_code)
os.system("notepad.exe op.txt")
olp=hashlib.md5(open('op.txt','rb').read()).hexdigest()
a = open("op.txt","r")
x = hashlib.md5()
print(olp)
with open("op.txt","rb") as fr:
    data = fr.read()
    x.update(data)
    if x == olp:
        print("New Update")
    else:
        print("Nothing New")
print(x)
    



    
                        
