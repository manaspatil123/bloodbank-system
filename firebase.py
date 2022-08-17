
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/key.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://mini-project-74faf-default-rtdb.firebaseio.com/"})
