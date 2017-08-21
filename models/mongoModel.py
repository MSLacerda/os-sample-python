from mongoengine import *
import datetime

# connect(host='mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')

connect('proj', host='localhost', port=27017)

class Loc(Document):
    lat = StringField(unique=False, required=True)
    lng = StringField(unique=False, required=True)


class Tree(Document):
    nome_pop = StringField(unique=False, required=True)
    nome_cie = StringField(unique=False, required=True)
    familia =  StringField(unique=False, required=False)
    categoria= StringField(unique=False, required=False)
    origem = StringField(unique=False, required=False)
    clima = StringField(unique=False, required=False)
    luminosidade = StringField(unique=False, required=False)
    altura = StringField(unique=False, required=False)
    info = StringField(unique=False, required=False)
    tags = ListField( ReferenceField(Loc) )


    # meta = {'db_alias': 'user-db'}




Tree(nome_pop="nome", nome_cie="oiii").save()  # Saves in the default d
va = Tree.objects()
print (va[0].nome_pop)

# with switch_db(User, 'archive-user-db') as User:
#     User(name='Ross').save()  # Saves the 'archive-user-db'




