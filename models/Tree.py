import pymongo

class Tree(Document):
    title = StringField(required=True, max_length=200)
    nome_pop = StringField(required=True, max_length=150)
    nome_cie = StringField()
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)
