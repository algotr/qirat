from django.conf.urls import url

from .views import index, add_funeral, delete_funeral, update_funeral, tag_funerals

urlpatterns = [
    url('^$', index, name='home'),
    url('^add/$', add_funeral, name='add'),
    url('^delete/$', delete_funeral, name='delete'),
    url('^update/(?P<funeral_id>[0-9]+)/$', update_funeral, name='update'),
    url('^show/(?P<tag_name>[^/]+)/$', tag_funerals, name='tag_funerals'),
]
