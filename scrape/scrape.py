import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    quotes = []
    authors_info = {}
    base_url = "http://quotes.toscrape.com"
    next_page = "/page/1/"

    while next_page:
        response = requests.get(base_url + next_page)
        soup = BeautifulSoup(response.text, "html.parser")

        # Scraping quotes and authors
        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]

            quotes.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

            # Scraping author details if not already scraped
            if author not in authors_info:
                author_link = quote.select_one("a[href^='/author/']")["href"]
                authors_info[author] = scrape_author_details(base_url + author_link)

        # Check for next page
        next_btn = soup.select_one(".next a")
        next_page = next_btn["href"] if next_btn else None

    return quotes, list(authors_info.values())


def scrape_author_details(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, "html.parser")

    fullname = soup.select_one(".author-title").get_text(strip=True)
    born_date = soup.select_one(".author-born-date").get_text(strip=True)
    born_location = soup.select_one(".author-born-location").get_text(strip=True)
    description = soup.select_one(".author-description").get_text(strip=True)

    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    }
