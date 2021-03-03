from django.shortcuts import render
from .models import Tenant
from django.http import Http404


def home(request):
    tenants = Tenant.objects.all()
    return render(request, 'home.html', {
        'tenants': tenants,

    })

    # return HttpResponse('<p>home view</p>')


def tenant_detail(request, tenant_id):
    try:
        tenant = Tenant.objects.get(id = tenant_id)
    except Tenant.DoesNotExist:
        raise Http404('tenant not found')
    return render(request, 'tenant_detail.html',{
        'tenant': tenant,
    })

    # return HttpResponse(f'<p>tenant_detail view with id {tenant_id}</p>')
