from django.urls import path
from ..views.admin import home

urlpatterns = [
    path(r'', home)
]