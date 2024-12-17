import db.config as db_config
from db.models import Quote, Author

def search_quotes():
    while True:
        query = input("Enter the command (name, tag, tags, exit): ").strip()
        if query == "exit":
            print("Ending the program...")
            break

        try:
            command, value = query.split(":")
            if command == "name":
                # Шукаємо автора за ім'ям
                author = Author.objects(fullname=value.strip()).first()
                if author:
                    # Шукаємо цитати, що належать цьому автору
                    quotes = Quote.objects(author=author)
                    for quote in quotes:
                        print(f"{quote.quote} — {quote.author.fullname}")
                else:
                    print(f"Author with name: {value.strip()} not found!")

            elif command == "tag":
                # Пошук цитат за одним тегом
                quotes = Quote.objects(tags=value.strip())
                for quote in quotes:
                    print(f"{quote.quote} — {quote.author.fullname}")

            elif command == "tags":
                # Пошук цитат за декількома тегами
                tags = [tag.strip() for tag in value.split(",")]
                quotes = Quote.objects(tags__in=tags)
                for quote in quotes:
                    print(f"{quote.quote} — {quote.author.fullname}")

            else:
                print("An unknown command!")
                continue

        except ValueError:
            print("The command format is incorrect. Please try again.")

if __name__ == "__main__":
    search_quotes()
