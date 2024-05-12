from api.config import get_firebase_app
import firebase_admin
from firebase_admin.exceptions import AlreadyExistsError
from firebase_admin import auth
async def create_user(user, firebase):
    
    try:
        #auth = firebase.get_service("auth")
        user = auth.create_user(
            email = user.email,
            password = user.password,
            #firstname = user.firstname,
            #lastname = user.lastname,
            #display_name = f"{user.firstname} {user.lastname}"
        )
        print(f"user create successfully {user.uid}")
        if user.uid:
            #token =  auth.create_custom_token(user.uid)
            return {
                "user" : user,
                #"token": token
            }
        else:
            return {
                "user": user
            }
    except AlreadyExistsError as email_error:
        print('Error creating user:', email_error)
        return None
    except Exception as e:
        print('Error creating user:', e)
        return "Error"

async def log_user(user):
    try:
        userExist = await auth.get_user_by_email(user.email)
        if userExist:
            pass
    except Exception as e:
        print("Error")
    pass