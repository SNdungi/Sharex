#Intra-Day closing share price

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import datetime as dt
from lxml import etree, html

response= requests.get("https://afx.kwayisi.org/nse/")
web_page=response.text
tree=html.fromstring(html=web_page)

soup=bs(web_page, "html.parser")

table=soup.find_all(name="div", class_="t")

co_data=tree.xpath("//tbody/tr/td[4]")
share_price=[p.text for p in co_data ]
nse_list=[]
nse_url=[]
for tb in table:
  company_name=tb.find_all(name="a")
  company_price=tb.find_all("td")
  
  for c in company_name:
    company_list=c.getText()
    company_info=c.get("href")
    nse_list.append(company_list)
    nse_url.append(company_info)

nse_codes=[nse_list[i] for i in range(0,len(nse_list),2)]
nse_companies=[nse_list[i] for i in range(1,len(nse_list),2)]
nse_sites=[nse_url[i] for i in range(0,len(nse_url),2)]


#Create a DataFram
date=dt.today().date().strftime("%d/%m/%Y")
df = pd.DataFrame(list(zip(nse_codes,nse_companies,share_price,nse_sites)), columns=["ID", "NAME",f"PRICE-{date}", "URL"])
# print(df)

date_doc=dt.today().date().strftime("%d%m%Y")
print(df)
df.to_csv(f"shares {date_doc}.csv")

