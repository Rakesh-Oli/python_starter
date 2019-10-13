from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Realtor, RealtorAdmin)

# Register your models here.
