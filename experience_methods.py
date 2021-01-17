def get_all_experiences(db):
    try:
        experience_collect = db.get_collection('experiences')
        experiences = []
        for ex in experience_collect.find():
            experiences.append(ex['experience_name'])
        return [0, experiences]
    except Exception:
        return [1, []]

def get_exp_params(db, experience_name):
   try:
       experience_collect = db.get_collection('experiences')
       params = list(experience_collect.find_one({"experience_name": experience_name}).values())[1:3]
       return [0, params]
   except Exception:
       return[1, []]

def get_playlist(db, experience_name):
    try:
        experience_collect = db.get_collection('experiences')
        playlist = experience_collect.find_one({"experience_name": experience_name})['playlist']
        return [0, playlist]
    except Exception:
        return[1, []]

def get_color_scheme(db, experience_name):
    try:
        experience_collect = db.get_collection('experiences')
        colors = experience_collect.find_one({"experience_name": experience_name})['color_scheme']
        return [0, colors]
    except Exception:
        return[1, []]
