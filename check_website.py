import requests
import bs4

producturl="******"

res =  requests.get(producturl, timeout=20)
#print(res)
if res.status_code != 200:
    pass



soup = bs4.BeautifulSoup(res.text,'html.parser')
element = soup.select('body > main > div.featuredSection > div.small-12.columns.discover-block.p-0 > div > div > div > div.register-block > li.menuItem.register.btn.btn-blue > a') #put your selector here
print(element)
