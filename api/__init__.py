from api.config import get_settings, get_firebase_app
firebase_app = get_firebase_app()
print(firebase_app.name)