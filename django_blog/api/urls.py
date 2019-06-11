from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', ArticleInfo.as_view(), name='articles'),
    path('article/<id>', ArticleDetail.as_view(), name='article_detail')
]