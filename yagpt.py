from bs4 import BeautifulSoup
import requests

url = 'https://docs.google.com/spreadsheets/u/0/d/e/2PACX-1vRhj_GboHBv0JQokn0SXqdnXme1czw7kXGQhaFUiqW5MfPkpguG4kYvDMrpnGAVaG3nn22xyDmjxJKQ/pubhtml/sheet?gid=94594447'
response = requests.get(url)
#print(response)
bs = BeautifulSoup(response.text,"lxml")
temp = bs.findAll('body', class_="docs-gm")
filt = []
#print(bs)
for data in temp:
    if data.find('tr') is not None:
        filt.append(data.text)
print(filt)

print('************************************************************************************************************************************************')
