from urllib import request
import requests
from bs4 import BeautifulSoup



request = requests.get('http://www.dowellcomputer.com/main.jsp')

html = BeautifulSoup(html.text,"html.parser")
print(html)

links = html.select("td>a")
print(links[0])
print(links[1])

tails = html.select(".tail")
print(tails)