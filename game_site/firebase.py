import firebase_admin
from firebase_admin import credentials, firestore
import os

# Ruta al archivo de credenciales
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, "serviceAccountKey.json")

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()
