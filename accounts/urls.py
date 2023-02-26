from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('register/<str:user_type>', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('send/email/verification', views.send_email_verification_code, name='send_email_verification_code'),
    path('email/verify', views.verify_email, name='verify_email'),
    path('logout', views.logout, name='logout')
    
]