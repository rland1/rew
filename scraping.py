# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=True)
    
    listings_title, listing_paragraph = listings(browser)

    data = {
        "listings_title": listings_title,
        "listing_paragraph": listing_paragraph
    }
    browser.quit()
    return data

def listings(browser):

    # Scrape REW
    # Visit the REW site
    url = 'https://www.rew.ca/properties/areas/ucluelet-bc'
    browser.visit(url)

    # Optional delay for loading the page
    #browser.is_element_present_by_css('div.list_text', wait_time=1)
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        listings_title = news_soup.find('h1', class_= 'searchheader-title').get_text()
#        print(listings_title)
        # Use the parent element to find the paragraph text
        #print('***')
       # listing_paragraph = news_soup.find('div', class_='col-xs-12 col-md-8').get_text()
       # print(listing_paragraph)
        for listing_paragraph in news_soup.select('.displaypanel-body'):
	        try:
		        print('**********')
		        print(listing_paragraph)

	        except Exception as e:
		#raise e
		        print('')
    except AttributeError:
        return None, None

    return listings_title

if __name__ == "__main__":
    print(scrape_all())