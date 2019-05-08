from django.urls import path
from ..views.admin import home
from ..views.admin import index
from ..views import article
from ..views import upload

urlpatterns = [
    path(r'', home, name="home"),
    path(r'index', index, name="index"),
    path(r'article/index', article.index, name="article_index"),
    path(r'upload', upload.upload, name="upload"),
]