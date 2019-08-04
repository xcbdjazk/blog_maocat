from rest_framework.views import APIView
from backend import models
from .serializers import ArticleSerializer
from .serializers import ArticleSerializerModel
from .serializers import UserSerializerModel
from .serializers import TagsSerializerModel
import json
from django.http import JsonResponse


class ArticleInfo(APIView):

    def get(self, req, *args, **kwargs):
       atcs = models.Article.objects.filter(is_active=True).order_by('-create_time').all()
       asr = ArticleSerializerModel(instance=atcs, many=True)
       return JsonResponse(asr.data, safe=False)


class ArticleDetail(APIView):

    def get(self, req, id, *args, **kwargs):
       atcs = models.Article.objects.get(id=id)
       asr = ArticleSerializerModel(instance=atcs)
       return JsonResponse(asr.data, safe=False)


class UserProfile(APIView):

    def get(self, req, *args, **kwargs):
       user = models.Admin.objects.first()
       usr = UserSerializerModel(instance=user)
       return JsonResponse(usr.data, safe=False)


class Tags(APIView):

    def get(self, req, *args, **kwargs):
       atcs = models.Article.objects.filter(is_active=True).order_by('-create_time').all()
       tags = []
       [tags.extend(i.tag.all()) for i in atcs]
       asr = TagsSerializerModel(instance=set(tags), many=True)
       return JsonResponse(asr.data, safe=False)