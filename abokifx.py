import time

import bs4 as bs
import urllib.request


class FX(object):
    def __init__(self, source):
        
        site = urllib.request.urlopen(source).read()
        self.soup = bs.BeautifulSoup(site,  'lxml')
        
        self.body = self.soup.body
        
        #print(self.body.prettify())
        
        #with open('aboki-fx.txt', 'w') as f:
            #f.writelines(str(self.body.prettify()))
     
    def display(self):
        txt = []
     
        print('*'*60)
        print('\t  FX of the Naira against USD, GBP, EUR')
        print()
        
    def header(self):
          val = self.body.find_all('table',  class_="grid-table")  
          
          heading = val[0].find_all('th')
          #print(val)
          heading = [h.get_text().replace('\n', ' ').strip().split(' ') for h in heading]
          heading = [h[0] for h in heading]
          print('*'*60)
          print(f'{heading[0]}\t\t{heading[1]}\t\t{heading[2]}\t\t{heading[3]}')
          print(f'\t\tbuy / sell\tbuy / sell\tbuy / sell')
          print('*'*60)
          
    def currency(self):
        row =[]
        date = []
        usd = []
        gbp = []
        eur = []
        body = self.body.find_all('tr', class_="table-line") 
        
        body = body[:3]
        
        body = [b.find_all('td') for b in body]
        
        for x in body:
            for y in x:
                row.append(y.get_text().replace('\n', ' ').strip())
        
        for a in range(len(row)):
            if a % 4 == 0:
                date.append(row[a])
                usd.append(row[a+1])
                gbp.append(row[a+2])
                eur.append(row[a+3])
            
        for x in range(len(date)):
            print(f'{date[x]}\t{usd[x]}\t{gbp[x]}\t{eur[x]}')
            time.sleep(0.5)

                                                            
                  
site = 'https://abokifx.com/home'
fx = FX(site)  

time.sleep(0.5)
fx.display()
time.sleep(0.5)
fx.header()

fx.currency()
