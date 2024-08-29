import jwt
from django.conf import settings
from django.http import JsonResponse


SECRET_KEY = settings.SECRET_KEY

class JWTTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization','')

    
        try:
            if token.startswith('Bearer '):
                token = token[len('Bearer '):]

            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

            request.user_id = payload.get('user_id')

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        response = self.get_response(request)
        return response
