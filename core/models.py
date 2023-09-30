from django.db import models

from WTS_backend import settings


class BaseModel(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='%(class)s_created')
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True,
                               related_name='%(class)s_edited', editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return self.name

