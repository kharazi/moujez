from mongoengine import StringField, DateTimeField, ListField, URLField


class NewsItem(Document):
    title = StringField(required=True)
    subtitle = StringField(required=True)
    refrence = StringField(max_length=100)
    content = StringField()
    publication_date = DateTimeField()
    news_code = IntField()
    category = StringField()
    tags = ListField(StringField(max_length=20))
    pictures = ListField(URLField(max_length=20))
    link = URLField()