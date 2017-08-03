from mongoengine import *
import datetime

connect(host='mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')

SIZE = (('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'))

class User(Document):
    name = StringField()
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)

    size = StringField(max_length=3, choices=SIZE)

    tags = ListField(StringField(max_length=50))

    content = StringField()

    meta = {'db_alias': 'user-db'}


class SurveyResponse(Document):
    date = DateTimeField()
    user = ReferenceField(User)


User(name='test').save()  # Saves in the default db


# with switch_db(User, 'archive-user-db') as User:
#     User(name='Ross').save()  # Saves the 'archive-user-db'




