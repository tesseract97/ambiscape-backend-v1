def create_user(db, username):
    user=db.get_collection('user')
    if user.count_documents({})==0:
        doc = {"username": username}
        user.insert_one(doc)
        return [0, username]
    else:
        return [1, ""]


def get_user(db):
    user = db.get_collection('user')
    if user.count_documents({})!= 0:
        username = user.find_one()['username']
        return [0, username]
    else:
        return [1, ""]







