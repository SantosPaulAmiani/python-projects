from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns
    path('add-admin/', views.add_admin, name='add_admin'),
]
