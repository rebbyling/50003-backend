from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AuditForm, CreateUserForm
from .filters import AuditFilter
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
import xlwt

import datetime

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





class tenantchartview(TemplateView):
    #view for tenants graph
    template_name='accounts/chart.html'
    
    

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]= tenant_score.objects.all()
        ## this qs will be passed into the chart.html template , the model used will be changed with sky's model, this model is empty and does not have any data, hence the graph displays nothing
        ##url link is /chart/
        ##
        return context 


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename = "SinghealthAudit'+str(datetime.datetime.now())+'.xls"'
    # file format when i download the object Singhealthaudit+datetime.xls

    workbook=xlwt.Workbook(encoding='utf-8')#this is to add the sheets into the workbook
    ws=workbook.add_sheet('SinghealthAudit')

    #row number for excel sheet
    row_num =0
    font_style=xlwt.XFStyle()
    #making the first row bold

    columns=['Name','Status','Category','date_created','description'] ##the header names of the column what should be exported?

    for column_number in range(len(columns)):
        ws.write(row_num,column_number,columns[column_number],font_style )
        #writing the name of the contents into the column header  into the workbook in 135 
    font_style=xlwt.XFStyle()

    rows = Tenant.objects.all().values_list('name','status','category','date_created','description')

    for row in rows:
        row_num+=1

        for column_number in range(len(row)):
            ws.write(row_num,column_number,str(row[column_number]),font_style)

        
    workbook.save(response)
    
    return response
