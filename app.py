import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for

app = Flask(__name__)

def scrape_websites():
    websites = [
        {
            "name": "The Hacker News",
            "url": "https://thehackernews.com/",
            "class": "home-title"
        },
        {
            "name": "Krebs on Security",
            "url": "https://krebsonsecurity.com/",
            "class": "entry-title"
        }
        # Add more websites here in the same format if needed
    ]

    all_data = []

    for site in websites:
        # Send a GET request to the URL
        response = requests.get(site["url"])

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all the divs with the specified class
            posts = soup.find_all("h2", class_=site["class"])

            # Iterate over each post
            for post in posts:
                title = post.text.strip()
                all_data.append({"website": site["name"], "title": title})
        else:
            print(f"Failed to retrieve the webpage for {site['name']}")

    return all_data

@app.route('/')
def index():
    # Scrape websites
    website_data = scrape_websites()
    return render_template('index.html', data=website_data)

@app.context_processor
def inject_static_url():
    return {'static_url': url_for('static', filename='')}

if __name__ == '__main__':
    app.run(debug=True)









