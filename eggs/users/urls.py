from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    #path('client-panel/', views.client_dashboard, name='client_dashboard'),
]
