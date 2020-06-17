from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView

class TokenView(ObtainAuthToken, GenericAPIView):
    pass