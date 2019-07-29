from django.urls import path
from ..views.admin import home
from ..views.admin import index
from ..views import article
from ..views import upload
from ..views import user

urlpatterns = [
    path(r'', home, name="home"),
    path(r'index', index, name="index"),
    path(r'article/index', article.index, name="article_index"),
    path(r'article/edit/<id>', article.article_edit, name="article_edit"),
    path(r'article/article_active/<id>', article.article_active, name="article_active"),
    path(r'tag/add', article.tag_add, name="tag_add"),
    path(r'tag/list', article.tag_list, name="tag_list"),
    path(r'tag/edit/<id>', article.tag_edit, name="tag_edit"),
    path(r'tag/tag_ajax', article.tag_ajax, name="tag_ajax"),
    path(r'edit/user', user.edit_user, name="edit_user"),
    path(r'upload', upload.upload, name="upload"),
]