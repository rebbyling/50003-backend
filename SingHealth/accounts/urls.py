from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
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
    #path('delete_tenant/', views.deleteTenant, name="delete"),
    path('tenant_only/',views.userPage,name="user-page"),
    path('chart/',views.tenantchartview.as_view(),name='chart'),
    path('export_excel/',views.export_excel,name='export_excel'),
    path('upload_image/',views.uploadImage, name='upload_image'),
    path('search/',views.search, name='search'),
    path('tenantsD/<str:pk>/',views.audit_details, name='tenantsDetail'),
    path('send_mail_plain_with_file',views.send_mail_plain_with_file,name='plain_email'),
    path('mail/',views.email,name='mail'),
    path('send_plain_mail',views.send_plain_mail,name='plain_email'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
