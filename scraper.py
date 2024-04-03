from bs4 import BeautifulSoup
from selenium import webdriver 
import time 

def get_website_content(url, sleep = False):
    driver = webdriver.Chrome() 
    driver.set_window_size(1920,1080) 

    # Send a get request to the url 
    driver.get(url) 
    if (sleep):
        time.sleep(1)

    return driver.page_source


    
def clean_website_content(content):
    soup = BeautifulSoup(content, 'html.parser')    
    return soup.get_text()

def scrape_herecomestheguide(state, page):
    url = f"https://www.herecomestheguide.com/wedding-venues/{state}?page={page}"
    content = get_website_content(url)
    # get the content under tag with class name "ais-StateResults"
    soup = BeautifulSoup(content, 'html.parser')
    state_results = soup.find("div", class_="ais-StateResults")
    return state_results.get_text()