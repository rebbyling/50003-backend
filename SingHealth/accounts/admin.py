from django.contrib import admin

# Register your models here.
from .models import *



admin.site.register(Staff)
admin.site.register(Tenant)
admin.site.register(Audit)

admin.site.register(checklist)
