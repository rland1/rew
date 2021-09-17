# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests 
from webdriver_manager.chrome import ChromeDriverManager


# %%
# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# Visit the rew site
url = 'https://www.rew.ca/properties/areas/ucluelet-bc'
browser.visit(url)


# %%
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

listings_title = news_soup.find('h1', class_= 'searchheader-title')
print(listings_title)


# %%
listings = news_soup.find('div', class_= 'displaypanel-content')
print(listings)

browser.quit()
