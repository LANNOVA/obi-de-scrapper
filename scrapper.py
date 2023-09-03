
#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

import requests
from bs4 import BeautifulSoup
import json
import re
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
wtos = input('item name -')
url = 'https://www.obi.de/search/'+ wtos + '/'

OB = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(OB.content, "html.parser")

name = soup.find_all("span", attrs={'class':'description'})

#pricediv = soup.find_all("div", attrs={'data-ui-name':'find-preise-preisprominent'})
priceunfiltered = soup.find_all("span", attrs={'class':'price-new'})
itemlink = soup.find_all("a", attrs={'class':'product-wrapper wt_ignore'})
print(len(priceunfiltered))
count = 0
while (count<len(name)):
    print(count+1)
    print(name[count].text.strip())
    print(priceunfiltered[count].get('data-csscontent'))
    itemlinkit = 'https://www.obi.de' + itemlink[count].get('href')

    print(itemlinkit)
    parts = itemlinkit.split('/')
    product_id = parts[-1]
   
    ratingsreq = requests.get('https://api.bazaarvoice.com/data/statistics.json?apiversion=5.4&passkey=caTR7pgF45nGChPx9FgPrUI37pr9vEbumf513k0pnEk14&stats=Reviews&filter=ContentLocale:de_DE,de*&filter=ProductId:'+ product_id, headers=HEADERS)
    descriptionreq = requests.get('https://api.bazaarvoice.com/data/products.json?resource=products&filter=id%3Aeq%3A'+ product_id + '&filter_reviews=contentlocale%3Aeq%3Ade*%2Cde_DE%2Cde_DE&filter_reviewcomments=contentlocale%3Aeq%3Ade*%2Cde_DE%2Cde_DE&filteredstats=Reviews&stats=Reviews&passkey=caTR7pgF45nGChPx9FgPrUI37pr9vEbumf513k0pnEk14&apiversion=5.5&displaycode=10524-de_de', headers=HEADERS)
    ratings = json.loads(ratingsreq.text)
    rating = ratings['Results'][0]['ProductStatistics']['ReviewStatistics']['AverageOverallRating']
    descriptions = json.loads(descriptionreq.text)
    description = descriptions['Results'][0]['Description']
    thumbnail = descriptions['Results'][0]['ImageUrl']
    ean = descriptions['Results'][0]['EANs'][0]
    try:
        manufacturer = descriptions['Results'][0]['Brand']['Name']
    except:
        manufacturer = 'n/a'
    print(rating)
    print(description)
    print(ean)
    print(thumbnail)
    print(manufacturer)
    count += 1
    print('')

#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572
