from django.urls import path
from ..views.admin import home
from ..views.admin import index

urlpatterns = [
    path(r'', home, name="home"),
    path(r'/index', index, name="index")
]