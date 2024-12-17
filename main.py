import sys
from scrape.load import load_to_file
from queries import load_data, search_quotes


def main():
    if not len(sys.argv) != 1:
        print("Invalid arguments.")
        sys.exit(1)
    if sys.argv[1] == "scrape":
        load_to_file()
        print("Quotes and authors have been successfully loaded.")
        sys.exit(0)
    if sys.argv[1] == "load":
        load_data.load_authors()
        load_data.load_quotes()
        print("Authors and quotes have been successfully loaded from JSON files.")
        sys.exit(0)
    if sys.argv[1] == "search":
        search_quotes.search_quotes()
        sys.exit(0)        


if __name__ == "__main__":
    main()
