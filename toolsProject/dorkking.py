import requests
from bs4 import BeautifulSoup
import re
import os
import os
import pandas as pd 

class tolol():
    def __init__(self):
        self.data = []


    def file(self):
        data = pd.read_csv('./dorks.csv')
        # data['dork']
        for i in range(len(data['dork'])):
            self.data.append(data['dork'][i])

    def dork(self):
        for i in range(len(self.data)):
            drk = self.data[i]
            # print(drk)
            url = f"https://www.google.com/search?q={drk}"
            # print(url)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                urls = []
                for item in soup.find_all('h3'):
                    link_tag = item.find_parent('a')

                    if link_tag and 'href' in link_tag.attrs:
                        link = link_tag['href']
                        urls.append(link)

                http_urls = [url for url in urls if re.match(r'^https?://', url)]

                for url in http_urls:
                    print(url)

                with open('urls.txt', 'w') as f:
                    for url in http_urls:
                        f.write(url + '\n')

            else:
                print("Error:", response.status_code)
data = tolol()
data.file()
data.dork()
