from django.db import models
from django.conf import settings
import hashlib
from .base import Model


class Article(Model):
    class Meta:
        db_table = "article"
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=4096*4)
    desc_txt = models.CharField(max_length=4096*4, null=True)
    is_active = models.BooleanField(default=False)
    tag = models.ManyToManyField("Tag")

    @property
    def tags_name(self):

        return ','.join([i.name for i in self.tag.all()])

'''on_delete attr '''
# 　 models.CASCADE,对就对象删除后，包含ForeignKey的字段也会被删除
#
# 　　models.PROTECT,删除时会引起ProtectedError
#
# 　　models.SET_NULL,注意只有当当前字段设置null设置为True才有效，此情况会将ForeignKey字段设置为null
#
# 　　models.SET_DEFAULT ,同样，当前字段设置了default才有效，此情况会将ForeignKey 字段设置为default 值
#
# 　　moels.SET,此时需要指定set的值
#
# 　　models.DO_NOTHING ,什么也不做


class Tag(Model):
    class Meta:
        db_table = "tag"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
