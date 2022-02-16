#This will not run on online IDE
from os import replace
import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
class Scrapper:
    def __init__(self) -> None:
        pass
    
    def scrap_prof_name(self):
            URL = "https://www.swansea.ac.uk/staff/engineering/#associate-professors=is-expanded&lecturers-and-tutors=is-expanded&professors=is-expanded&readers=is-expanded&senior-lecturers=is-expanded"
            r = requests.get(URL)

            soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        
            quotes=[]  # a list to store quotes
            
            table = soup.find('div', attrs = {'id':'professors-contents'}) 
            
            for row in table.find_all():
                quote = {}
                # quote['url'] =re.findall('"([^"]*)"',str(row))

                quote['url'] =row.get('href')
                quote['name'] =row.get_text()
                quotes.append(quote)
            
            filename = 'profile_urls.csv'
            with open(filename, 'w', newline='') as f:
                w = csv.DictWriter(f,['name','url'])
                w.writeheader()
                for quote in quotes:
                    w.writerow(quote)
            print("Information retrived successfully and stored in to 'profile_urls.csv.csv' file")




    def scrap_all_prof_info(self):
        info=pd.read_csv('profile_urls.csv')
        info=info.dropna()
        exps=[]  # a list to store expertise
        for name,url in zip(info.name,info.url):
            
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
               
                table = soup.find('div', attrs = {'class':'staff-profile-areas-of-expertise'}) 
                print(table.get_text())
                exp={}
                exp['name']=name
                res = re.sub(' +', ' ', table.get_text().replace("\n","").replace('Areas Of Expertise',''))
                exp['expertise']=str(res)
                div = soup.find('div', {"class" : "col"})
                text = div.text
                exp['phone']=text.replace(" ","")

                soup = BeautifulSoup(r.content, 'html5lib')
                div = soup.find('div', {"class" : "title-and-body-text title-and-body-text-12"})
                text = div.text
                exp['about']=re.sub(' +', ' ', text.replace("\n","").replace('About',''))

                exps.append(exp)
                # print(exps)
                
            except:
                continue
        print(exps)
        print("\n\n")
        print("Profile information is retrived successfylly and stored in a 'profile_exps.csv' file.")
        filename = 'profile_exps.csv'
        with open(filename, 'w',encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f,['name','expertise','phone','about'])
            w.writeheader()
            for exp in exps:
                w.writerow(exp)
            
             

          
        
           

scrap=Scrapper();

scrap.scrap_prof_name()
scrap.scrap_all_prof_info()



    
