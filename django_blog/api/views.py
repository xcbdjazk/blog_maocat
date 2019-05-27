from rest_framework.views import APIView
from backend import models
from .serializers import ArticleSerializer
from .serializers import ArticleSerializerModel
import json
from django.http import JsonResponse


class ArticleInfo(APIView):

    def get(self, req, *args, **kwargs):
       atcs = models.Article.objects.order_by('-create_time').all()
       asr = ArticleSerializerModel(instance=atcs, many=True)
       return JsonResponse(asr.data, safe=False)

