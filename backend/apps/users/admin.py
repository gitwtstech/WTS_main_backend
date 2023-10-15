from django.contrib import admin

from users.models import WTSUser, Company

admin.site.register(WTSUser)
admin.site.register(Company)