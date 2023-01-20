from bs4 import BeautifulSoup
import requests
from datetime import date
import os

def mit_climate_portal():
    today = date.today()
    html_text = requests.get("https://climate.mit.edu/explainers/carbon-capture").text
    soup = BeautifulSoup(html_text, 'lxml')

    title = soup.find("title").text
    heading = soup.find('h1', class_ = 'faux-full-title').text
    content = soup.find('div', class_ = 'clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item').text
    with open(f'feed/{title}-{today}.txt', 'w') as f:
        f.write(f"{heading.strip()} \n")
        f.write(f"{content.strip()} \n")
    print(f"File saved: {title}-{today}.txt")

def netl_doe_gov():
    today = date.today()
    html_text = requests.get("https://netl.doe.gov/carbon-management/carbon-capture").text
    soup = BeautifulSoup(html_text, 'lxml') 
    title = soup.find("title").text
    content = soup.find('div', class_ = 'node node--type-program-factsheet node--view-mode-full ds-1col clearfix').text
    with open(f'feed/{title}-{today}.txt', 'w') as f:
        f.write(f"{content.strip()} \n")
    print(f"File saved: {title}-{today}.txt")

def iea_org():
    today = date.today()
    html_text = requests.get("https://www.iea.org/reports/direct-air-capture").text
    soup = BeautifulSoup(html_text, 'lxml') 
    title = soup.find("title").text
    heading_main = soup.find('h1', class_ = 'f-title-1').text
    intro = soup.find('div', class_ = 'm-intro-report__header').text
    content = soup.find('section', class_ = "m-spacer m-spacer--medium").text
    with open(f'feed/{title}-{today}.txt', 'w') as f:
        f.write(f"{heading_main.strip()} \n")
        f.write(f"{intro.strip()} \n")
        f.write(f"{content.strip()} \n")
    print(f"File saved: {title}-{today}.txt")

netl_doe_gov()
mit_climate_portal()
iea_org()
