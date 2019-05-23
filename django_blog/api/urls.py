from django.urls import path
from .views import *

urlpatterns = [
    path('articls/', ArticleInfo.as_view(), name='articles')
]