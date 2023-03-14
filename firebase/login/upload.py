import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import storage

def upload_to_firebase(file):
    client=storage.Client()
    bucket=client.bucket('images')
    blob=bucket.blob(file)
    blob.upload_from_file(file)
    blob.make_public()
    url=blob.public_url
    return url







cred = credentials.Certificate("D:\login\secretkey.json")
firebase_admin.initialize_app(cred)


db=firestore.client()

data={
    "name":"Riss",
    "age":19,
    "pass":"rishiriss"
}

doc_ref=db.collection('aliens').dicument()
doc_ref.set(data)

print("completed")