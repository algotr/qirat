from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('funeral.urls', namespace='funeral')),

    url(r'^login/$', 'account.views.login', name='login'),
    url(r'^logout/$', 'account.views.logout', name='logout'),
    url(r'^register/$', 'account.views.register', name='register'),
    url(r'^profile/$', 'account.views.profile', name='profile'),
    url(r'^search/', include('haystack.urls')),
]
