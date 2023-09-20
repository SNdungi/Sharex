# Create a database for the focused shares
# The list of shares comes from the Shar_portfolio excel template

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from lxml import etree, html
import re
import matplotlib.pyplot as plt
from tqdm import tqdm

def get_portfolio_shares(file='share_portfolio_watch&focuss.xlsx'):
    excel_file = pd.read_excel(file)
    column_entries = excel_file["Code"].tolist()
    share_names=list(map(str.lower, column_entries))
    return share_names

share_name= get_portfolio_shares()

def share_sim_data():
    main_df= pd.DataFrame()
    for name in tqdm(share_name, desc='Processing shares', unit='share'):
        graph_url = f"https://afx.kwayisi.org/chart/nse/{name}"
        response = requests.get(graph_url)
        soup=bs(response.content, "lxml")

        p_tag_content=soup.find('p').text
        data_start = p_tag_content.find('data:[')
        data_end = p_tag_content.find(',]}]});})')

        data_section = p_tag_content[data_start + len('data[['):data_end].strip()
        data_points = [point.strip().split(',') for point in data_section.split('],[')]
        for point in data_points:
            point[0] = point[0].replace('d("', '').replace('")', '')   
        data_points[0][0]=data_points[0][0].replace("[","",)

        valid_data_points = []

        # Loop through the original data points and attempt to convert and append valid data points
        for date_str, price_str in data_points:
            try:
                date = pd.to_datetime(date_str)
                price = float(price_str)
                valid_data_points.append([date, price])
            except ValueError:
                pass  # Skip rows with invalid data
            

        df = pd.DataFrame(valid_data_points, columns=['Date', name])
        df.set_index('Date',inplace=True)

        if main_df.empty:
            main_df=df
        else:
            main_df=main_df.join(df,how='outer')
    main_df.reset_index(inplace=True)
    main_df.set_index('Date',inplace=True)
    return main_df
