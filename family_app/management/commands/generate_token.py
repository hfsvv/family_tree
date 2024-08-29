from django.core.management.base import BaseCommand
import jwt
import datetime
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        SECRET_KEY = settings.SECRET_KEY

        payload = {
            'user_id': 123,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        print({"token":token})