from django.db import models

from users.models import WTSUser


# class BaseModel(models.Model):
#     creator = models.ForeignKey(WTSUser, on_delete=models.PROTECT, related_name='families')
#     editor = models.ForeignKey(WTSUser, on_delete=models.PROTECT, null=True, blank=True, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['-created_at', '-updated_at']
