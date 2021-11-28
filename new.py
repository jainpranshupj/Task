import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1&brand=winchester"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find('div',class_='product')

#bprint(results)

datas = soup.find_all("div", class_="product")

for data in datas:
    
    price = data.find("span", class_="price").text.strip()
    title = data.find("a", class_="catalog-item-name").text.strip()
    stock = data.find("span", class_="out-of-stock").text.strip()
    manuf = data.find("a", class_="catalog-item-brand").text.strip()
    
   	
    
    task={'Price':price,
    	'Title':title,
    	'Stock':stock,
    	'Manufacturer':manuf

    }
    print(task)
   # print('Price:',price.text.strip())
    #print('Title:',title.text.strip())
    #print('Status:',stock.text.strip())
    #if stock==class_:
    #	print('Stock:',True)
    ##	print('Stock',False)
    #print('Manufacturer:',manuf.text.strip())
   #b print(job_element)
    print('')

#python_jobs = results.find_all("h2", string="Python")

	