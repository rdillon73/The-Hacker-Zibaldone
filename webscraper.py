# webscraper.py
import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the information you need from the page with BeautifulSoup
# For example, find all the links on the page and save their URLs
links = soup.find_all('a')
urls = [link.get('href') for link in links]

# Save the information in a CSV file
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])
    for url in urls:
        writer.writerow([url])

print(‘Scraping complete’)
