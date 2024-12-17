import db.config as db_config
import json
from db.models import Author, Quote


def load_authors():
    with open("data/authors.json", "r", encoding="utf-8") as f:
        authors_data = json.load(f)
    for author in authors_data:
        Author(
            fullname=author["fullname"],
            born_date=author["born_date"],
            born_location=author["born_location"],
            description=author["description"]
        ).save()

def load_quotes():
    with open("data/quotes.json", "r", encoding="utf-8") as f:
        quotes_data = json.load(f)
    for quote in quotes_data:
        author = Author.objects(fullname=quote["author"]).first()
        if author:
            Quote(
                tags=quote["tags"],
                author=author,
                quote=quote["quote"]
            ).save()
