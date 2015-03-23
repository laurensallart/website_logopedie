from django.conf.urls import patterns, url
from oefening import views
from django.conf import settings 
from django.conf.urls.static import static 


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_child/$', views.add_child, name='add_child'),
        url(r'^add_opgave/$', views.add_opgave, name='add_opgave'),
        url(r'^add_reeks/$', views.add_reeks, name='add_reeks'),
        url(r'^add_opgave_to_reeks_view/(?P<reeks_name_slug>[\w-]+)/$', views.add_opgave_to_reeks_view, name='add_opgave_to_reeks_view'),
        url(r'^add_opgave_to_reeks/(?P<reeks_name_slug>[-\w\d]+)/(?P<opgave_name_slug>[-\w\d]+)/$', views.add_opgave_to_reeks, name='add_opgave_to_reeks'),
        url(r'^delete_opgave_from_reeks/(?P<reeks_name_slug>[-\w\d]+)/(?P<opgave_name_slug>[-\w\d]+)/$', views.delete_opgave_from_reeks, name='delete_opgave_from_reeks'),
        url(r'^child/(?P<child_userName_slug>[\w-]+)/$', views.child, name='child'),
        url(r'^child/(?P<child_userName_slug>[\w-]+)/resultaten/$', views.resultaten, name='resultaten'),
        url(r'^child/(?P<child_userName_slug>[\w-]+)/show_reeksen/$', views.show_reeksen, name='show_reeksen'),
        url(r'^child/(?P<child_userName_slug>[\w-]+)/(?P<reeks_name_slug>[\w-]+)/$', views.start_oefening, name='start_oefening'),
        url(r'^maak_oefening/(?P<child_userName_slug>[\w-]+)/(?P<reeks_name_slug>[\w-]+)/(?P<resultaat_id>[-\w\d]+)/(?P<count>\d+)/$', views.maak_oefening, name='maak_oefening'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^opgaves/$', views.opgaves, name='opgaves'),
        url(r'^reeksen/$', views.reeksen, name='reeksen'),
        )