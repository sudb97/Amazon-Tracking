import requests
from bs4 import BeautifulSoup
import re
#from re import sub
#from decimal import Decimal

def tkt_status():                                
    
    url = 'https://webproxy.vpnbook.com/includes/process.php?action=update'     #give the proxy website address
    myobj = {'u':'https://www.amazon.in/Fitbit-Charge-Fitness-Tracker-Non-NFC/dp/B084CQ41M2/ref=sr_1_1?crid=24TPLF0KWISCL&dchild=1&keywords=fitbit+charge+4&qid=1608539121&s=electronics&sprefix=fitbit+char%2Celectronics%2C534&sr=1-1'}    #pass parameter as the website to scrape from
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
    response = requests.post(url,headers=headers,data = myobj)
    soup= BeautifulSoup(response.content,'html.parser')
    #print(soup)
    
    try:
        div = soup.find("span", {"id": "priceblock_ourprice"})
        price=str(div.text)
    except AttributeError:
        div = soup.find("span", {"id": "priceblock_dealprice"})
        price=str(div.text) 
    
    return price


#print(tkt_status())