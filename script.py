from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup


import os
import csv
import requests
requests.packages.urllib3.disable_warnings()

liest = []
for i in range (5):
	def scrape():
	    session = requests.Session()
	    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}

	    url = 'https://eyeonanime.tv/baccano-episode-'+str(i)+'/'

	    content = session.get(url, verify=False).content

	    soup = BeautifulSoup(content, "html.parser")
	    columns = soup.find_all('div', {'class':'ws-player'})
	    liest.append(columns)
	    print(columns)

	scrape()
print(liest)

for i in range (1,5):
	with open(os.path.join('polls/templates', 'ep-'+str(i)+'.html') , 'w') as myfile:
	    	myfile.write("Baccano Episode"+str(i)+" %s\n" % liest[i]+"<a href=../ep-"+str(i-1)+">previous episode</a>"+"<a href=../ep-"+str(i+1)+">next episode</a>")

	with open(os.path.join('mysite','urls.py'), 'a') as myfile:
	    	myfile.write("	url(r'^ep-"+str(i)+"/$', TemplateView.as_view(template_name='ep-"+str(i)+".html')),\n")
with open(os.path.join('mysite','urls.py'), 'a') as myfile:
	myfile.write("]")
