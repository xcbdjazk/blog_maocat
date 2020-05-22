from django.urls import path
from .views import *

urlpatterns = [
    path('articles/', ArticleInfo.as_view(), name='articles'),
    path('article/<id>', ArticleDetail.as_view(), name='article_detail'),
    path('user/profile', UserProfile.as_view(), name='user_profile'),
    path('tags', Tags.as_view(), name='tags'),
    path('images', Images.as_view(), name='tags')
]