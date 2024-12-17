from dotenv import load_dotenv
from os import getenv
from mongoengine import connect

load_dotenv()
url = getenv("URL")

connect(
    host=url,
    alias="default"
)
