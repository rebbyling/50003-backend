from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .forms import AuditForm, CreateUserForm ,ScoreForm
from .filters import AuditFilter
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from .decorators import  unauthenticated_user, allowed_users,admin_only
import xlwt
from django.core.mail import send_mail, EmailMessage
from SingHealth.settings import EMAIL_HOST_USER


import datetime

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')

            group=Group.objects.get(name='tenant')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)




@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username Or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    audits = Audit.objects.all()
    #staff = Staff.objects.all()
    tenants = checklist.objects.all()

    #total_audits = audits.count()
    #passed = audits.filter(status='Pass').count()
    #pending = audits.filter(status='Pending').count()
    context = {'audits': audits, 'tenants':tenants}

    return render(request, 'accounts/dashboard.html', context)
#def home(request):
    #audits = Audit.objects.all()
    #staff = Staff.objects.all()
   # tenants = Tenant.objects.all()

    #total_audits = audits.count()
    #passed = audits.filter(status='Pass').count()
    #pending = audits.filter(status='Pending').count()
    #context = {'audits': audits, 'tenants':tenants}

   # return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@admin_only
def tenants(request):
    tenants = Tenant.objects.all()

    return render(request, 'accounts/tenants.html', {'tenants': tenants})


@login_required(login_url='login')
@admin_only
def staff(request, pk):
    staff = Staff.objects.get(id=pk)
    audits = staff.audit_set.all()
    myFilter = AuditFilter(request.GET, queryset=audits)
    audits = myFilter.qs

    audit_count = audits.count()
    context = {'staff': staff, 'audits': audits, 'audit_count': audit_count, 'myFilter': myFilter}
    return render(request, 'accounts/staff.html', context)

@login_required(login_url='login')
@admin_only
def createAudit(request):
    form=AuditForm()
    if request.method == 'POST':
        form = AuditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'accounts/audit_form.html', context)

@login_required(login_url='login')
@admin_only
def updateAudit(request):
    form = AuditForm()

    # audit = Audit.objects.get(id=pk)
    # form = AuditForm(instance=audit)
    context = {'form': form}
    return render(request, 'accounts/audit_form.html', context)

@login_required(login_url='login')
def uploadImage(request):
    context={}
    if request.method=="POST":
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)

    return render(request, 'accounts/upload_image.html',context)

@login_required(login_url='login')
def userPage(request):
    audits = Audit.objects.all()


    return render(request,'accounts/tenant_only.html',{'audits':audits})

#def deleteTenant(request):
#    audit = Audit.objects.all()
#    if request.method=="POST":
 #       audit.delete()
 #       return redirect('/')
 #   context = {'item':audit}
 #   return render(request,'accounts/delete.html',context)

def search(request):
    audits = Audit.objects.all()
    myFilter = AuditFilter(request.GET, queryset=audits)
    audits = myFilter.qs

    context = {'audits': audits,'myFilter': myFilter}

    return render(request, 'accounts/search.html', context)


class tenantchartview(TemplateView):
    #view for tenants graph
    template_name='accounts/chart.html'
    
    

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]= checklist.objects.all()
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

    columns=['Tenant','Score','Date Audited'] ##the header names of the column what should be exported?

    for column_number in range(len(columns)):
        ws.write(row_num,column_number,columns[column_number],font_style )
        #writing the name of the contents into the column header  into the workbook in 135 
    font_style=xlwt.XFStyle()

    #rows = tenant_score.objects.all().values_list('name','score')
    rows = checklist.objects.all().values_list('tenant__name','score','date_audited')#checklist attribute foreign key tenant .name tenant_name = checklist.tenant.name

    for row in rows:
        row_num+=1

        for column_number in range(len(row)):
            ws.write(row_num,column_number,str(row[column_number]),font_style)

        
    workbook.save(response)
    
    return response

def audit_details(request, pk):
    tenants = Tenant.objects.get(id=pk)
    audits = tenants.audit_set.all()
    context = {
            'tenants' : tenants,
            'audits' : audits
            }
    return render(request,'accounts/tenantsdetails.html', context)
    
#This email can type commments and attach file
@login_required(login_url='login')
def send_mail_plain_with_file(request):
    message=request.POST.get('message','')
    subject=request.POST.get('subject','')
    mail_id=request.POST.get('email','')
    email = EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
    email.content_subtype='html'
    
    file =request.FILES["file"]#in the html email name ='file'
    email.attach(file.name,file.read(),file.content_type)
    email.send()
    return redirect('http://127.0.0.1:8000/mail/')

#This  email can only type  comments 
@login_required(login_url='login')
def send_plain_mail(request):
    message=request.POST.get('message','')
    subject=request.POST.get('subject','')
    mail_id=request.POST.get('email','')
    email = EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
    email.content_subtype='html'
    email.send()
    return redirect('http://127.0.0.1:8000/mail/')

@login_required(login_url='login')
def email(request):
    return render(request,"accounts/email.html")




#def calculate(request):
    #form=ScoreForm(request.POST)
    #formc = ScoreForm(request.POST)
    #if request.method=="POST":
        #checked = form.cleaned_data['items']
        #score = checked.count()
        #score_object = ChecklistScore(score = score)
        #score_object.save()
        #score_object.checked = list(checked.values_list('description', flat=True))
        #score_object.unchecked = list(set(formc.fields['items'].queryset.values_list('description', flat=True)) - set(score_object.checked))
        #score_object.save()
        #context['score'] = score
        #context['checked'] = score_object.checked
        #context['test'] = score_object.unchecked
    #return redirect('http://127.0.0.1:8000/checklist/')
def checklist_view(request):
    context={}
    if request.method =='POST':
        form =ScoreForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.Staff=request.user
            instance.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form=ScoreForm()
    context['form']=form
    return render(request,"accounts/checklistform.html",context)


