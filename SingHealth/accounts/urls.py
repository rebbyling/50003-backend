from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('tenants/', views.tenants, name="tenants"),
    path('staff/<str:pk>/', views.staff, name="staff"),
    path('create_audit/', views.createAudit, name="create_audit"),
    path('update_audit/', views.updateAudit, name="update_audit"),
    path('checklist/',views.checklist_view, name="checklist"),
    path('chart/',views.tenantchartview.as_view(),name='chart'),
    path('export_excel',views.export_excel,name='export'),
    

]