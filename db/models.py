from mongoengine import Document, StringField, ReferenceField, ListField


# Модель автора
class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# Модель цитати
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)  # Видалення цитат при видаленні автора
    quote = StringField(required=True)
