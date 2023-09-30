from rest_framework import serializers

from families.models import Family, Category, RevitFamily, RevitType, ThreeDSMaxFamily, Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RevitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevitType
        exclude = ['id', 'revit_family']


class RevitFamilySerializer(serializers.ModelSerializer):
    revit_types = RevitTypeSerializer(many=True)

    class Meta:
        model = RevitFamily
        exclude = ['family', 'id']


class ThreeDSMaxFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreeDSMaxFamily
        exclude = ['family', 'id']


class FamilySerializer(serializers.ModelSerializer):
    factory = FactorySerializer()
    category = CategorySerializer()
    revit_families = RevitFamilySerializer(many=True)
    threedsmax_families = ThreeDSMaxFamilySerializer(many=True)
    creator = serializers.CharField(source='creator.username')
    editor = serializers.CharField(source='creator.username')

    class Meta:
        model = Family
        fields = ['name', 'created_at', 'updated_at', 'creator', 'editor', 'category', 'factory', 'revit_families',
                  'threedsmax_families',]
