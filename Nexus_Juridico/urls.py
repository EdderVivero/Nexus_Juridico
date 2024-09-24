from django.urls import path
from .views import login_view
from .views import registro
from .views import dashboard_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
