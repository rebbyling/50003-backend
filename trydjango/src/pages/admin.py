from django.contrib import admin

# Register your models here.

from .models import tenants

admin.site.register(tenants)
