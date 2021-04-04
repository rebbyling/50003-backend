import django_filters
from django_filters import DateFilter
from .models import *

# class AuditFilter(django_filters.FilterSet):
#     start_date = DateFilter(field_name="date_audited",lookup_expr='gte')
#     end_date = DateFilter(field_name="date_audited", lookup_expr='lte')
#     class Meta:
#         model = Audit
#         fields = '__all__'
#         exclude = ['date_audited', 'staff','comment']


class AuditFilter(django_filters.FilterSet):
    class Meta:
        model = Audit
        fields = '__all__'
        exclude = ['date_audited','status', 'staff','comment','actual_img']