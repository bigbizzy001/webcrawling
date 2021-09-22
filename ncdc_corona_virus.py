import bs4 as bs
import urllib.request


class Covid(object):
    def __init__(self, source):
        
        site = urllib.request.urlopen(source).read()
        self.soup = bs.BeautifulSoup(site,  'lxml')
        
        self.body = self.soup.body
        
        #print(self.body.prettify())
        
        with open('covid-site.txt', 'w') as f:
            f.writelines(str(self.body.prettify()))
        
            
    def title(self):
        t = self.body.find('h1', class_= 'text-black')   
        return t.get_text()
        
    def overview(self):
        values = []
        c = self.body.find_all('h6', class_="text-white")     
        
        cases= [x.get_text() for x in c]
        
        val = self.body.find_all('h2', class_="text-right text-white")
        
        for x in range(len(val)):
            if x == 0:
                values.append(val[x].get_text()[1:])
            else:
                values.append(val[x].get_text())
        
        print('  An overview of Nigerians Corona Virus cases & casualties')
        print('*'*60)
        print('*'*60)
        print()
        for x in range(len(cases)):
            print(f'  {cases[x]} ------ {values[x]}') 
            print('-'*40)
            
        
        
    def state_sum(self):
        state = []
        cases_confirmed  = []
        cases_admission = []
        discharged = []
        death = []
        head =['states', 'cases', 'admission', 'discharged', 'death']
        header = self.body.find_all('th')
        header = [x.get_text() for x in header]
        val = self.body.find_all('table', id='custom1')  
        
        st = self.body.find_all('td')
        st = [x.get_text().replace('\n', ' ').strip() for x in st]
        
        for v in range(len(st)):
            if v%5 == 0:
                state.append(st[v])
                cases_confirmed.append(st[v+1])
                cases_admission.append(st[v+2])
                discharged.append(st[v+3])
                death.append(st[v+4])  
                
        print('Covid-19 Cases by State')  
        print('*'*60)
        print()     
        print(f'{head[0]}\t\t |{head[1]}\t |{head[2]} |{head[3]} |{head[4]}')
        print('-'*60)
        for a in range(len(death)):
            if a == 9 or a ==15:
                print(f'{state[a]}\t {cases_confirmed[a]}\t {cases_admission[a]}\t    {discharged[a]}\t{death[a]}')
                print('*'*60)
            elif a == 32:
                print(f'{state[a]}\t {cases_confirmed[a]}\t {cases_admission[a]}\t    {discharged[a]}\t\t{death[a]}')
                print('*'*60)    
            elif a == 29 or a == 30 or a == 31 or a == 33 or a == 34 or a ==35 or a == 36 or a == 37:   
                print(f'{state[a]}\t\t {cases_confirmed[a]}\t {cases_admission[a]}\t    {discharged[a]}\t\t{death[a]}')
                print('*'*60) 
            else:
                print(f'{state[a]}\t\t {cases_confirmed[a]}\t {cases_admission[a]}\t    {discharged[a]}\t{death[a]}')
                print('*'*60)

    def highlights(self):
        state = []
        light = self.body.find_all('ul', style="text-align: justify")
        
        light = [x.get_text() for x in light[0].find_all('li')]
        
        cases = light[2][46:].split(',')
        c2 = cases[len(cases)-1].strip()[4:]
        cases[len(cases)-1] = c2
        cases = [cas.strip().split('(') for cas in cases]
        
        state = [x[0].strip() for x in cases]
        value = [int(y[1][:len(y[1])-1]) for y in cases]
        
                
        '''
        print(state)
        print()
        print(value)
        print()
        '''
        print(f'  {"*"*5} Highlights of Corona Virus cases in Nigeria {"*"*5}')
        print('*'*60)
        print(f'  1. {light[0]}')
        print()
        print(f'  2. {light[2][:-185]}:')
        print()
        print(f'  \tState\t\t|Cases')
        print(f'  \t{"*"*21}')
        
        for x in range(len(value)):
            if len(state[x]) < 6:
                print(f'  \t{state[x]}\t\t{value[x]}')
            elif len(state[x]) > 8:
                print(f'  \t{state[x]}\t{value[x]}')    
            else:
                print(f'  \t{state[x]}\t\t{value[x]}')
        
        '''print(f'  2. {light[2][46:]}')
        print()
        print(cases)
        print()
        
        print()
        print(c2)
        print()
        print(f'  2. {light[2]}')
        print()
        '''
     
                         
                                                
                        
            
        
        
        
        
        
                         
                                                           
        

        
                
                        
site = 'https://covid19.ncdc.gov.ng/'
covid = Covid(site)  

print(f'  {covid.title()} - "STATISTICS"')
print()

def display():
    print(f'  Enter (1) - Overview (2) - State Cases (3) - Daily Highlights')
    hl = input()

    if hl == '1':
        covid.overview()
        display()
    elif hl == '2':
        covid.state_sum()
        display()
    elif hl == '3':
        covid.highlights()    
        display()
    else:
        display()         
    
#covid.overview()  
#print(covid.title())

#covid.state_sum() 
#covid.highlights()      
display()                                                             
        
