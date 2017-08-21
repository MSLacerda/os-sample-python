from mongoengine import *
import datetime

# connect(host='mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')

connect('proj', host='mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd', port=15915)

class Loc(Document):
    lat = StringField(unique=False, required=True)
    lng = StringField(unique=False, required=True)


class Tree(Document):
    nome_pop = StringField(unique=False, required=True)
    nome_cie = StringField(unique=False, required=False)
    familia =  StringField(unique=False, required=False)
    categoria= StringField(unique=False, required=False)
    origem = StringField(unique=False, required=False)
    clima = StringField(unique=False, required=False)
    luminosidade = StringField(unique=False, required=False)
    altura = StringField(unique=False, required=False)
    info = StringField(unique=False, required=False)
    tags = ListField( ReferenceField(Loc) )


    # meta = {'db_alias': 'user-db'}



teste = "teste"
Tree("eita", "oi").save()  # Saves in the default d
for va in Tree.objects():
    print (va.nome_pop)

# with switch_db(User, 'archive-user-db') as User:
#     User(name='Ross').save()  # Saves the 'archive-user-db'




