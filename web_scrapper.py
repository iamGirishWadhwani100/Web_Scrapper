import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the quote elements on the page
quotes = soup.find_all('div', class_='quote')

# Create a list to store the quotes
quotes_list = []

# Loop through each quote element
for quote in quotes:
    # Extract the text and author of the quote
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    
    # Add the quote to the list
    quotes_list.append({
        'text': text,
        'author': author
    })

# Print the quotes
for quote in quotes_list:
    print(f"Quote: {quote['text']}")
    print(f"Author: {quote['author']}")
    print("---")