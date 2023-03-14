import firebase_admin
from firebase_admin import credentials,storage
from firebase_admin import db

def fireconnect(cred):
    cred=credentials.Certificate('D:\login\secretkey.json')
    firebase_admin.initialize_app(cred,{
    'databaseURL':"https://console.firebase.google.com/project/studio-5f946/database/studio-5f946-default-rtdb/data/~2F"

    })
    ref = db.reference('D:\photos\wallpapers')
    print(ref.get())
  