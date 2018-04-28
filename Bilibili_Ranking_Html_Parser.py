import requests
import lxml
from bs4 import BeautifulSoup
class Bilibili_Ranking_Html_Parser(object):
    def parse_from_html(self,content):
        if content is None:
            return
        soup=BeautifulSoup(content.decode("UTF-8"),'lxml')
        return self.parse_from_soup(soup)

    def parse_from_soup(self,soup):
        new_urls=set()
        #html=soup.find('div',class_='rank-list-wrap').html
        #print(contents)
        #ranking_html=BeautifulSoup(html,'lxml')
        soup=soup.find('div',class_='rank-list-wrap')
        links=soup.find_all('a',class_='title')
        for link in links:
            url=link['href']
            new_urls.add(url)
        return new_urls


