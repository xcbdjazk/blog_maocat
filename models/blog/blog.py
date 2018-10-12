from config import mongo
from mongoengine import *
import datetime


class TagBlog(mongo.DynamicDocument):
    meta = {"collection": "tag_blog"}

    alias_id = SequenceField()
    name = StringField(required=True)
    father = ReferenceField("self")
    create_time = DateTimeField(default=datetime.datetime.now())
    update_time = DateTimeField(default=datetime.datetime.now())

    def edit_update_time(self):
        self.update_time = datetime.datetime.now()
        self.save()


class NavigationBlog(mongo.DynamicDocument):
    meta = {"collection": "navigation_blog"}

    alias_id = SequenceField()
    name = StringField(required=True)
    url = StringField()
    endpoint = StringField()
    father = ReferenceField("self")

    def all_children(self):
        return NavigationBlog.objects(father=self).all()


class ArticleBlog(mongo.DynamicDocument):
    meta = {"collection": "articleBlog_blog"}
    class STATUS:
        on = 1
        off = 0


    alias_id = SequenceField()
    title = StringField(required=True)
    body = StringField(required=True)
    tags = ListField(ReferenceField(TagBlog))
    page_view = IntField(default=0)
    status = IntField(default=STATUS.on)
    create_time = DateTimeField(default=datetime.datetime.now())
    update_time = DateTimeField(default=datetime.datetime.now())

    def page_view_incr(self):
        self.page_view += 1
        self.save()