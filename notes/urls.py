app_name='notes'

from django.contrib import admin
from django.urls import path
from django.urls import URLPattern
from django.urls import include
from django.conf.urls import url

from notes.views import index_view,add_note,add_tag,tag_search
from django.views.generic.base import TemplateView
urlpatterns=[
    path('',index_view,name="index"),
    path('addnote/',add_note,name='addnote'),
    path('addtag/',add_tag,name='addtag'),
    url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='tagsearch'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'),
]