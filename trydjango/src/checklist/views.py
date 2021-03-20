from django.shortcuts import render
from .models import *

# Create your views here.
def health_view(request):
    context = {}
    context['health'] = healthForm()
    context['safety'] = safetyForm()

    return render(request, "checklist.html", context) 
