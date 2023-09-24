from django.db import models

from users.models import WTSUser


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


class AbstractFamily(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    creator = models.ForeignKey(WTSUser, on_delete=models.PROTECT, related_name='%(class)s_created')
    editor = models.ForeignKey(WTSUser, on_delete=models.PROTECT, null=True, blank=True,
                               related_name='%(class)s_edited', editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.name


class Family(AbstractFamily):
    factory = models.ForeignKey(Factory, on_delete=models.PROTECT, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


class FamilyImage(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


class RevitFamily(AbstractFamily):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='revit_families')
    file = models.FileField(upload_to='revit_family')

    def __str__(self):
        return f'{self.family.name}: {self.name}'


class RevitType(models.Model):
    name = models.CharField(max_length=256)
    revit_family = models.ForeignKey(RevitFamily, on_delete=models.CASCADE, related_name='revit_types')


class ThreeDSMaxFamily(AbstractFamily):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='threedsmax_families')
    file = models.FileField(upload_to='threedsmax_family')

