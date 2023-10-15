from django.db import models

from core.models import BaseModel


class Factory(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256, blank=True)
    email = models.EmailField(blank=True)
    description = models.TextField(max_length=512, blank=True)
    address = models.CharField(max_length=256, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f'Name: {self.name}, id: {self.id}'


class Category(models.Model):
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Family(BaseModel):
    factory = models.ForeignKey(Factory, on_delete=models.PROTECT, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


class FamilyImage(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


class RevitFamily(BaseModel):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='revit_families')
    file = models.FileField(upload_to='files')

    def __str__(self):
        return f'{self.family.name}: {self.name}'


class RevitType(models.Model):
    name = models.CharField(max_length=256)
    revit_family = models.ForeignKey(RevitFamily, on_delete=models.CASCADE, related_name='revit_types')


class ThreeDSMaxFamily(BaseModel):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='threedsmax_families')
    file = models.FileField(upload_to='files')
