from rest_framework import viewsets

from families.models import Family
from families.serializers import FamilySerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = (Family.objects.all().select_related('factory', 'category', 'creator', 'editor')
                .prefetch_related('revit_families', 'threedsmax_families', 'revit_families__revit_types'))
    serializer_class = FamilySerializer
