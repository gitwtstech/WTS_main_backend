from django.contrib import admin

from families.models import Factory, Category, Family, FamilyImage, RevitFamily, RevitType, ThreeDSMaxFamily

admin.site.register(Factory)
admin.site.register(Category)
admin.site.register(Family)
admin.site.register(FamilyImage)
admin.site.register(ThreeDSMaxFamily)


class RevitTypeInline(admin.StackedInline):
    model = RevitType


@admin.register(RevitFamily)
class RevitFamilyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in RevitFamily._meta.fields]
    inlines = [RevitTypeInline]
