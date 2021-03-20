from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AuditForm, CreateUserForm, checklistForm
from .filters import AuditFilter
from django.contrib.auth.forms import UserCreationForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    audits = Audit.objects.all()
    #staff = Staff.objects.all()
    tenants = Tenant.objects.all()

    #total_audits = audits.count()
    #passed = audits.filter(status='Pass').count()
    #pending = audits.filter(status='Pending').count()
    context = {'audits': audits, 'tenants':tenants}

    return render(request, 'accounts/dashboard.html', context)


def tenants(request):
    tenants = Tenant.objects.all()

    return render(request, 'accounts/tenants.html', {'tenants': tenants})


@login_required(login_url='login')
def staff(request, pk):
    staff = Staff.objects.get(id=pk)
    audits = staff.audit_set.all()
    myFilter = AuditFilter(request.GET, queryset=audits)
    audits = myFilter.qs

    audit_count = audits.count()
    context = {'staff': staff, 'audits': audits, 'audit_count': audit_count, 'myFilter': myFilter}
    return render(request, 'accounts/staff.html', context)


def createAudit(request):
    form = AuditForm()
    if request.method == 'POST':
        form = AuditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/audit_form.html', context)


def updateAudit(request):
    form = AuditForm()

    # audit = Audit.objects.get(id=pk)
    # form = AuditForm(instance=audit)
    context = {'form': form}
    return render(request, 'accounts/audit_form.html', context)

def checklist_view(request):
    score = 0
    form = checklistForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            health1 = form.cleaned_data['health1'] #return true if the health1 is checked
            health2 = form.cleaned_data['health2']
            health3 = form.cleaned_data['health3']
            safety1 = form.cleaned_data['safety1']
            safety2 = form.cleaned_data['safety2']
            # adding up the score by brutal force
            if health1:
                score += 1
            if health2:
                score += 1
            if health3:
                score += 1
            if safety1:
                score += 1
            if safety2:
                score += 1
            print("score =" + str(score))
    else:
        form = checklistForm()
    context = {}
    context['checklist'] = checklistForm()

    return render(request, 'checklist.html', context)
