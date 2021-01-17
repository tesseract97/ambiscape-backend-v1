from pymongo import MongoClient
from ambiscape_methods import color_methods as color, experience_methods as exp, user_methods as user, \
    soundcloud_playlist_methods as sound


def call_mongodb():
    client = MongoClient("mongodb://tesseract:0722velociraptor@cluster0-shard-00-00.xc17a.mongodb.net:27017,"
                         "cluster0-shard-00-01.xc17a.mongodb.net:27017,cluster0-shard-00-02.xc17a.mongodb.net:27017/"
                         "ambiscape?ssl=true&replicaSet=atlas-10qz81-shard-0&authSource=admin&retryWrites=true&w="
                         "majority")
    db = client['ambiscape']
    return db


def create_experiences_menu(db):
    menu = exp.get_all_experiences(db)
    return menu


def get_playlist_from_experience(db, experience_name):
    playlist_name = exp.get_playlist(db, experience_name)
    return sound.get_playlist(playlist_name)


# TODO
# def get_color_scheme_from_experience(db, experience_name):
#   color_scheme = exp.get_color(db, experience_name)
#   return color.get_playlist(playlist_name)
