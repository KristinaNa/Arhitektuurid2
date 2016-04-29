from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.radio_list, name='radio_list'),
    url(r'^radio/s$', views.radio_list),
    url(r'^radio/edit$', views.change_radio),
    #url(r'^radio/s?id=(?P<radio_id>\d+)$', views.change_radio, name='change_radio'),

  #  url(r'^$', views.cats_list, name='cats_list'),
  #  url(r'^cat/add$', views.add_cats, name='add_cats'),
  #  url(r'^cat/create/$', views.Create_cat.as_view()),
]