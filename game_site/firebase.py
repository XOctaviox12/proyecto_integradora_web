import firebase_admin
from firebase_admin import credentials, firestore
import os
from django.conf import settings

# -------------------------------------------
#   USAR LAS CREDENCIALES DESDE SETTINGS.PY
#   (que vienen de Render)
# -------------------------------------------

service_account_info = settings.FIREBASE_SERVICE_ACCOUNT

if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_info)
    firebase_admin.initialize_app(cred)

# Cliente Firestore
db = firestore.client()
