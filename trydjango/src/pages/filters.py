import django_filters

from .models import *

class tenantFilter(django_filters.FilterSet):
    class Meta:
        model= tenant
        fields= '__all__'
        exclude=['Auditor','date','done']#excluding these attributes from the model
