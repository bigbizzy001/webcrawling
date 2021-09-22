import bs4 as bs
import urllib.request


class Crypto(object):
    def __init__(self, source):
        
        site = urllib.request.urlopen(source).read()
        self.soup = bs.BeautifulSoup(site,  'lxml')
        
        self.body = self.soup.body
        
    def title(self):        
        return self.soup.title.get_text()            
                
    def name(self):
        name = []

        c_name = self.body.find_all('span', class_= "price-navigationstyles__CoinName-sc-1xrlgdp-1 eiKird")

        for n in c_name:
            name.append(n.get_text())

        return name                        

    def price(self):
        coin_price = []
        
        val = self.values()
        
        for p in val:
            coin_price.append(p[:-6])
            
        return coin_price            
        
    def gain_loss(self):
        c_gain_loss = []
        
        val = self.values()
        
        for p in val:
            c_gain_loss.append(p[-6:])
            
        return c_gain_loss           
              
    def display(self):
        name = self.name()
        price = self.price()
        c_gl = self.gain_loss()
        
        for i in range(len(name)):
            print(name[i], '\t', price[i], '\t', c_gl[i])
                       
                
    def values(self):
        val =[]

        c_val = self.body.find_all('div', class_= "price-wrapper")

        for g in c_val:
            val.append(g.get_text())                     

        return val                        
                                                  
                
        
site = 'https://www.coindesk.com/data/'
crypto = Crypto(site)

crypto.display()
