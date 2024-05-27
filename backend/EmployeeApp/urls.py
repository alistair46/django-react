from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Department/', views.departmentApi),
    path('Employee/', views.EmployeeApi),
    
    path('Department/<int:id>/', views.departmentApi, name='delete_department'),
    path('Employee/<int:id>/', views.EmployeeApi, name='delete_Emloyee'),

    path('Employee/Savefiles', views.SaveFile),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
