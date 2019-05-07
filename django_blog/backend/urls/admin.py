from django.urls import path
from ..views.admin import home
from ..views.admin import index
from ..views.admin import upload

urlpatterns = [
    path(r'', home, name="home"),
    path(r'index', index, name="index"),
    path(r'upload', upload, name="index")
]