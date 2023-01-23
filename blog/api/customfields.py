from rest_framework import serializers
from rest_framework.reverse import reverse
from blog.models import Post, Tag
from blango_auth.models import User

class CustomHyperlink(serializers.HyperlinkedRelatedField):
    # We define these as class attributes, so we don't need to pass them as arguments.
    view_name = 'api_post_detail'
    queryset = Post.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'author_email': obj.author,
            'post_id': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
           'user__email': view_kwargs['author_email'],
           'pk': view_kwargs['post_id']
        }
        return self.get_queryset().get(**lookup_kwargs)