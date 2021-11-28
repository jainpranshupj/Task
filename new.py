import requests
from bs4 import BeautifulSoup
import json



URL = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1&brand=winchester"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


datas = soup.find_all("div", class_="product")


for data in datas:
    
    price = data.find("span", class_="price").text.strip() 
    title = data.find("a", class_="catalog-item-name").text.strip()
    stock = data.find("span", class_="status")
    if stock:  
        stocks=format(stock.find("span", {"class": "out-of-stock"}).text.strip()) 
        stk=False
    else:
        stk=True
    manuf = data.find("a", class_="catalog-item-brand").text.strip()
    
   	
    
    task={'Price':price,
    	'Title':title,
    	'Stock':stk,
    	'Manufacturer':manuf

    }
    print(task)
 
    print('')



	