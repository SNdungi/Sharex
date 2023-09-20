from investment import Investment as inv
#rate of growth of buying price is inversely proportional to the square of charge on transaction of shares
#assuming that the charge on buying and selling charges are same and are a %of the Amount invested/sold otherwise its the product of the 2
# k=1/charge**2, k is the minimum rate of growth of the price.
#so now i can define an input figure of expected ROI nas set the system t buy or sell whn attained.
#the question now is how deep to allow the drop (1)historical time analysis (2)derive the minimum threshhold to not make a loss

buying=[30.30]
name=['bkg']
investment=[1000000]
selling=[inv.get_min_sell_price(i,bp,0.0184) for i,bp in zip(investment,buying )]
sell_set=[40]
sp=[]

for i in range(len(name)):

  test_investment=inv(name=name[i],value=investment[i],sell_price=sell_set[i],buy_price=buying[i])
  try_investment=inv(name=name[i],value=investment[i],sell_price=selling[i],buy_price=buying[i])


  profit= test_investment.expected_ROI()

  print(f'shares:{test_investment.share_volume()} for {name[i]}')
  print(test_investment.inv_txn_charge())
  print(test_investment.purchase_residual())
  print(f'share sell price: {test_investment.share_sp}')
  print(f'net sale value:{test_investment.sell_value()}')
  print('profit',profit)
  print(test_investment.share_volume())
  print(test_investment.inv_txn_charge())




































# from bs4 import BeautifulSoup as bs
# import requests
# import pandas as pd
# from datetime import datetime as dt
# from lxml import etree, html

# response= requests.get("https://afx.kwayisi.org/nse/")
# web_page=response.text
# tree=html.fromstring(html=web_page)
# soup=bs(web_page, "html.parser")

# table=soup.find_all(name="div", class_="t")

# co_data=tree.xpath("//tbody/tr/td[4]")
# share_price=[p.text for p in co_data ]
# nse_list=[]
# nse_url=[]
# for tb in table:
#   company_name=tb.find_all(name="a")
#   company_price=tb.find_all("td")
  
#   for c in company_name:
#     company_list=c.getText()
#     company_info=c.get("href")
#     nse_list.append(company_list)
#     nse_url.append(company_info)

# nse_codes=[nse_list[i] for i in range(0,len(nse_list),2)]
# nse_companies=[nse_list[i] for i in range(1,len(nse_list),2)]
# nse_sites=[nse_url[i] for i in range(0,len(nse_url),2)]


# #Create a DataFram
# date=dt.today().date().strftime("%d/%m/%Y")
# df = pd.DataFrame(list(zip(nse_codes,nse_companies,share_price,nse_sites)), columns=["ID", "NAME",f"PRICE-{date}", "URL"])
# print(df)

# date_doc=dt.today().date().strftime("%d%m%Y")
# df.to_csv(f"Daily_shares: {date_doc}.csv")


  