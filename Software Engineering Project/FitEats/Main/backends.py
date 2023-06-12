
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

"""class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        users = UserModel.objects.all()

        for user in users:
            print(user.email)
        print(username)
        print("burası pass")
        print(password)
        try:

            user = UserModel.objects.get(email=username)
            print(user.email)
        except UserModel.DoesNotExist:
            print("burası none")
            return None

        if user.check_password(password):
            return user
        

    def get_user(self, user_email):  # Parametre adı 'user_email' olarak değiştirildi
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(email=user_email)
        except UserModel.DoesNotExist:
            return None
        """
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None