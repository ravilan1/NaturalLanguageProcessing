from bs4 import BeautifulSoup
import requests
import lxml
import time

def webscrap():
    print('unfamilier keyskill')
    unfamilier=input('>')
    print(f'flitering out {unfamilier}')
    http_res=requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=4&startPage=1').text
    soup=BeautifulSoup(http_res,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        keySkills=job.find('span',class_='srp-skills').text.replace('\n','')
        if unfamilier not in keySkills:
            companyname=job.find('h3',class_='joblist-comp-name').text.replace('\n','')
            skills=job.find('span',class_='srp-skills').text.replace('\n','')
            posteddate=job.find('span',class_='sim-posted').span.text
            print(f'''
            companyname:{companyname}
            keyskills:{skills}
            posted date:{posteddate}
            ''')
            with open('jobs.txt','a') as file:
                file.write(companyname+' '+keySkills+' '+posteddate+'\n'+'--------------------------------------------------')

def udemyWebscrap():
    udemyurl=requests.get('https://www.udemy.com/courses/search/?src=ukw&q=mule')
    udemySoup=BeautifulSoup(udemyurl.content,'html.parser')
    #for sp in udemySoup.find_all('span',class_='price-text__current'):
        #print(sp)
    print(udemySoup)


#if __name__ == '__main__':
#    while(true):
 #       webscrap()
  #      print('waiting 10mins')
  #      time.sleep(10*60)
udemyWebscrap()
