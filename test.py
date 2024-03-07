import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://thehackernews.com/'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Print the entire HTML to see if it's capturing the page correctly
    print(soup.prettify())

    # Find all elements with the specified class (you can inspect the webpage to find the right class)
    articles = soup.find_all('div', class_='article')

    # Loop through each article and extract the title
    for article in articles:
        # Get the title of the article
        title = article.find('h2').text.strip()

        # Print the title
        print(title)
else:
    # If the request was not successful, print an error message
    print('Failed to retrieve page')
