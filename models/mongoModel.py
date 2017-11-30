from mongoengine import *
import datetime

# connect(host='mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')

connect('proj', host='mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd', port=15915)

class User(Document):
    email = StringField(unique=True, required=True)
    nome = StringField(unique=False, required=True)

    # meta = {'db_alias': 'user-db'}


#
# teste = "teste"
#
# e = Tree("eita", "oi").save()
# Tree().update()
# Tree().delete()
# Tree().objects(pk='')
#
# for va in Tree.objects():
#     print (va.nome_pop)

# with switch_db(User, 'archive-user-db') as User:
#     User(name='Ross').save()  # Saves the 'archive-user-db'




