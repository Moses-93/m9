import json

from .scrape import scrape_quotes


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_to_file():
    quotes, authors = scrape_quotes()
    save_to_json(quotes, "./data/quotes.json")
    save_to_json(authors, "./data/authors.json")
    