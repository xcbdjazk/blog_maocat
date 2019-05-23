from rest_framework import serializers
from backend import models


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()


class ArticleSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"
        depth = 1
        # fields = ['id', 'title']