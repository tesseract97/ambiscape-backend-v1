from pymongo import MongoClient
import user_methods
import experience_methods


client = MongoClient("mongodb://tesseract:0722velociraptor@cluster0-shard-00-00.xc17a.mongodb.net:27017,"
                     "cluster0-shard-00-01.xc17a.mongodb.net:27017,cluster0-shard-00-02.xc17a.mongodb.net:27017/"
                     "ambiscape?ssl=true&replicaSet=atlas-10qz81-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['ambiscape']

user = db.get_collection('user')


#experience_methods.get_playlist(db, 'melancholy')

#user_methods.create_user(db, "Tessa")

#username = user_methods.get_user(db)
#print(username)




'''try:
    dbs = client.list_database_names()
    print(dbs)
    db = client['ambiscape']
    list = db.list_collections()
    #list = client.list_database_names()
    print(list)

except Exception:
    print("Server not available")


db = client.ambiscape'''
