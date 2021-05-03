import os
from rest_framework import serializers
from database.models.post import Comment, Post
from love_post.serializer.base import Base
from love_user.serializer.user_serializer import UserModelSerializer
from babel.dates import datetime
import timeago, datetime

class PostSerializer(Base):
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)

    def get_fields(self,*args, **kwargs):
        fields = super(PostSerializer, self).get_fields(*args, **kwargs)
        return fields

    def create(self, val):
        if self.context['args'] == "create":
            return self.c_p(val)
        return val

    def c_p(self,val):
        create = Post(content=val.get('content'),photo=val.get('photo'),author=val.get('author'))
        create.save()
        return create

    def update(self, ins, val):
        if self.context:
            if self.context['args'] == 'comment':
                return self.create_comment(ins,val)
        if val.get('photo'):
            if ins.photo:
                split = str(ins.photo).split("/")
                path = 'media/photo/%s' % split[len(split) - 1]
                os.system('rm %s' % path)
            ins.photo = val.get('photo')
        ins.content = val.get('content')
        ins.save()
        return ins

    def create_comment(self,ins, val):
        create = Comment(comment=val.get('comment'),user=val.get('author'))
        create.save()
        ins.comment.add(create)
        return ins



class PostModelSerializer(serializers.ModelSerializer):
    author = UserModelSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
    time = serializers.SerializerMethodField("get_time_display")

    def get_time_display(self,post):
        date = datetime.datetime(year=post.createAt.year,month=post.createAt.month,day=post.createAt.day,minute=post.createAt.minute,hour=post.createAt.hour,second=post.createAt.second)
        now = datetime.datetime.now() + datetime.timedelta(seconds=60*3.4)
        return timeago.format(date,now,'in_ID')
