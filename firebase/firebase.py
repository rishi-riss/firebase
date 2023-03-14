import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate('D:\login\secretkey.json')
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()
