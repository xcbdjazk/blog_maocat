
from rest_framework import serializers
from backend import models


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField()


class ArticleSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"
        depth = 1
        # fields = ['id', 'title']


class TagsSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"


class UserSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        exclude = ('password_hash',)


class ImagesSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = models.ImagesModel
        fields = "__all__"
