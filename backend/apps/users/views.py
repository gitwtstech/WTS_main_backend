from rest_framework.viewsets import ModelViewSet

from users.models import WTSUser
from users.serializers import WTSUserSerializer


class WTSUserViewSet(ModelViewSet):
    queryset = WTSUser.objects.all()
    serializer_class = WTSUserSerializer
