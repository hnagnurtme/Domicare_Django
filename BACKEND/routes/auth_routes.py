from controllers import auth_controller
from django.urls import path

urlpatterns = [
    path('login', auth_controller.login, name='login'),
    path('logout', auth_controller.logout, name='logout'),
]